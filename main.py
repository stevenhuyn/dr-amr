import requests
from dotenv import load_dotenv
import os
import json

def main():
    # Load countries and indicators from JSON files
    with open('countries.json', 'r') as f:
        countries = json.load(f)
    
    with open('indicators.json', 'r') as f:
        indicators = json.load(f)
    
    # Function to recursively get all leaf node indicators
    def get_leaf_indicators(data, path=""):
        leaf_indicators = []
        if isinstance(data, dict):
            for key, value in data.items():
                current_path = f"{path},{key}" if path else key
                leaf_indicators.extend(get_leaf_indicators(value, current_path))
        elif isinstance(data, list):
            for item in data:
                leaf_indicators.append(f"{path},{item}")
        return leaf_indicators
    
    # Get all leaf indicators
    all_indicators = get_leaf_indicators(indicators)
    
    # Initialize output data structure
    output_data = []
    
    # Cross product: iterate through each country and each indicator


    for country in countries[:1]:
        for indicator in all_indicators[:1]:
            print(f"Processing: {country} - {indicator}")
            result = genResearchPrompt(country, indicator)
            if result:
                output_data.append({
                    "country": country,
                    "indicator": indicator,
                    "response": result
                })
    
    # Write all results to output.json
    with open('output.json', 'w') as f:
        json.dump(output_data, f, indent=2)



def genResearchPrompt(country: str, indicator: str):
    promptTemplate = """
For a given country and a given policy, we are trying to see if that country fufills the policy.

Here is an example bare input (normally more context would be given):
Regulatory Indicators,Technical Dossier Standards,CTD/ACTD Adoption,Mandates ACTD (for generics)
Vietnam


With this input, you will generate an excellent LLM prompt that will be given to Perplexity's Sonar Deep Research to answer whether Vietnam mandates ACTD (for generics).

Below will the the country - policy pair:
"""

    SONAR_API_KEY = os.environ.get("SONAR_API_KEY")

    with open("scope.md") as f:
        scope = f.read()

    # Set up the API endpoint and headers
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {SONAR_API_KEY}",  # Replace with your actual API key
        "Content-Type": "application/json"
    }

    # Define the request payload
    prompt = f"{promptTemplate}\n\n{country}\n{indicator}"
    print(prompt)

    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    # Make the API call
    response = requests.post(url, headers=headers, json=payload)

    # Return the AI's response content
    if response.status_code == 200:
        return response.json()["choices"][0]['message']['content']
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None 
        



if __name__ == "__main__":
    load_dotenv()
    main()
