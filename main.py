import requests
from dotenv import load_dotenv
import os
import json
from prompt import GEN_RESEARCH_PROMPT, SUMMARIZE_REPORT_PROMPT


def load_data():
    """Load countries and indicators from JSON files"""
    with open("countries.json", "r") as f:
        countries = json.load(f)
    with open("indicators.json", "r") as f:
        indicators = json.load(f)
    return countries, indicators


def get_leaf_indicators(indicator_data, path=""):
    """Recursively get all leaf node indicators"""
    leaf_indicators = []
    if isinstance(indicator_data, dict):
        for key, value in indicator_data.items():
            current_path = f"{path} > {key}" if path else key
            leaf_indicators.extend(get_leaf_indicators(value, current_path))
    elif isinstance(indicator_data, list):
        for indicator_item in indicator_data:
            leaf_indicators.append(f"{path} > {indicator_item}")
    return leaf_indicators


def call_sonar_api(prompt, model="sonar-pro"):
    """Make API call to Perplexity Sonar"""
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {os.environ['SONAR_API_KEY']}",
        "Content-Type": "application/json",
    }
    payload = {"model": model, "messages": [{"role": "user", "content": prompt}]}
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]


def generate_research_prompt(country, indicator):
    """Generate research prompt using Perplexity API"""
    prompt = GEN_RESEARCH_PROMPT.replace("{indicator}", indicator, 1).replace(
        "{country}", country, 1
    )
    return call_sonar_api(prompt)


def research_policy(prompt):
    """Research policy using Perplexity deep research API"""
    return call_sonar_api(prompt, "sonar-deep-research")


def summarise_report(content):
    """Extract Yes/No/Partial/Unknown determination from research content"""
    if not content:
        return "Unknown"
    prompt = SUMMARIZE_REPORT_PROMPT.format(content=content)
    return call_sonar_api(prompt).strip()


def extract_content_from_response(policy_result):
    """Extract content string from various response formats"""
    if isinstance(policy_result, dict) and "choices" in policy_result:
        return policy_result["choices"][0]["message"]["content"]
    return str(policy_result)


def generate_research_prompts(countries, indicators):
    """Generate research prompts for all country-indicator combinations"""
    research_prompts = []
    for country in countries:
        for indicator in indicators:
            print(f"Processing: {country} - {indicator}")
            response = generate_research_prompt(country, indicator)
            research_prompts.append(
                {
                    "country": country,
                    "indicator": indicator,
                    "response": response,
                }
            )
    return research_prompts


def research_policies(research_prompts):
    """Research policies using the generated prompts"""
    responses = {}
    for prompt_data in research_prompts:
        policy_result = research_policy(prompt_data["response"])
        responses[(prompt_data["country"], prompt_data["indicator"])] = policy_result
    return responses


def summarize_policy_responses(policy_responses):
    """Summarize policy responses using the summarise_report function"""
    print("Summarizing policy research results...")
    policy_summaries = {}
    for (country, indicator), policy_result in policy_responses.items():
        content = extract_content_from_response(policy_result)
        summary = summarise_report(content)
        policy_summaries[(country, indicator)] = summary
        print(f"Summarized {country} - {indicator}: {summary}")
    return policy_summaries


def write_results(research_prompts, policy_responses, policy_summaries):
    """Write results to output files"""
    # Write prompts to output.json
    with open("output.json", "w") as f:
        json.dump(research_prompts, f, indent=2)

    # Write policy research results to TSV
    with open("policies.tsv", "w") as f:
        f.write("Country\tIndicator\tResult\n")
        for (country, indicator), policy_result in policy_responses.items():
            f.write(f"{country}\t{indicator}\t{policy_result}\n")

    # Write policy summaries to TSV
    with open("policy_summaries.tsv", "w") as f:
        f.write("Country\tIndicator\tSummary\n")
        for (country, indicator), summary in policy_summaries.items():
            f.write(f"{country}\t{indicator}\t{summary}\n")


def main():
    """Main function to orchestrate the policy research process"""
    # Load data
    countries, indicators = load_data()
    indicators = get_leaf_indicators(indicators)

    # Generate research prompts
    research_prompts = generate_research_prompts(countries[:1], indicators[:1])

    # Research policies
    policy_responses = research_policies(research_prompts)

    # Summarize policy responses to Yes/No etc
    policy_summaries = summarize_policy_responses(policy_responses)

    # Write results
    write_results(research_prompts, policy_responses, policy_summaries)

    print(
        f"Completed processing {len(research_prompts)} prompts and {len(policy_responses)} policy research tasks"
    )


if __name__ == "__main__":
    load_dotenv()
    main()
