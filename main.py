import requests
from dotenv import load_dotenv
import os
import json
from prompt import GEN_RESEARCH_PROMPT


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


def generate_research_prompts(countries, indicators):
    """Generate research prompts for all country-indicator combinations"""
    research_prompts = []

    for country in countries:
        for indicator in indicators:
            print(f"Processing: {country} - {indicator}")
            try:
                generated_prompt = generate_research_prompt(country, indicator)
                if generated_prompt:
                    research_prompts.append(
                        {
                            "country": country,
                            "indicator": indicator,
                            "response": generated_prompt,
                        }
                    )
            except Exception as e:
                print(f"Error processing {country} - {indicator}: {e}")
                continue

    return research_prompts


def research_policies(research_prompts):
    """Research policies using the generated prompts"""
    responses = {}

    for prompt_data in research_prompts:
        try:
            policy_result = research_policy(prompt_data["response"])
            responses[(prompt_data["country"], prompt_data["indicator"])] = (
                policy_result
            )
        except Exception as e:
            print(
                f"Error researching policy for {prompt_data['country']} - {prompt_data['indicator']}: {e}"
            )
            continue

    return responses


def write_results(research_prompts, policy_responses):
    """Write results to output files"""
    # Write prompts to output.json
    with open("output.json", "w") as f:
        json.dump(research_prompts, f, indent=2)

    # Write policy research results to TSV
    with open("policies.tsv", "w") as f:
        f.write("Country\tIndicator\tResult\n")
        for (country, indicator), policy_result in policy_responses.items():
            f.write(f"{country}\t{indicator}\t{policy_result}\n")


def main():
    """Main function to orchestrate the policy research process"""
    try:
        # Load data
        countries, indicators = load_data()

        # Get all leaf indicators
        all_indicators = get_leaf_indicators(indicators)

        # Generate research prompts
        research_prompts = generate_research_prompts(countries[:1], all_indicators[:1])

        # Research policies
        policy_responses = research_policies(research_prompts)

        # Write results
        write_results(research_prompts, policy_responses)

        print(
            f"Completed processing {len(research_prompts)} prompts and {len(policy_responses)} policy research tasks"
        )

    except Exception as e:
        print(f"Error in main: {e}")
        return 1

    return 0


def generate_research_prompt(country: str, indicator: str):
    """Generate research prompt using Perplexity API"""
    SONAR_API_KEY = os.environ.get("SONAR_API_KEY")

    if not SONAR_API_KEY:
        raise ValueError("SONAR_API_KEY environment variable not set")

    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {SONAR_API_KEY}",
        "Content-Type": "application/json",
    }

    prompt = GEN_RESEARCH_PROMPT.replace("{indicator}", indicator, 1)
    prompt = prompt.replace("{country}", country, 1)

    payload = {"model": "sonar-pro", "messages": [{"role": "user", "content": prompt}]}

    try:
        response = requests.post(url, headers=headers, json=payload)
        response.raise_for_status()

        return response.json()["choices"][0]["message"]["content"]

    except requests.exceptions.RequestException as e:
        print(f"API request error for {country} - {indicator}: {e}")
        return None
    except KeyError as e:
        print(f"Unexpected API response format for {country} - {indicator}: {e}")
        return None


def research_policy(prompt: str) -> str:
    """Research policy using Perplexity deep research API"""
    SONAR_API_KEY = os.environ.get("SONAR_API_KEY")

    if not SONAR_API_KEY:
        raise ValueError("SONAR_API_KEY environment variable not set")

    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {SONAR_API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {
        "model": "sonar-deep-research",
        "messages": [{"role": "user", "content": prompt}],
    }

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as e:
        print(f"API request error during policy research: {e}")
        return ""
    except KeyError as e:
        print(f"Unexpected API response format during policy research: {e}")
        return ""


if __name__ == "__main__":
    load_dotenv()
    main()
