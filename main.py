import requests
from dotenv import load_dotenv
import os

def main():
    SONAR_API_KEY = os.environ.get("SONAR_API_KEY")
    print(SONAR_API_KEY)

    # Set up the API endpoint and headers
    url = "https://api.perplexity.ai/chat/completions"
    headers = {
        "Authorization": f"Bearer {SONAR_API_KEY}",  # Replace with your actual API key
        "Content-Type": "application/json"
    }

    # Define the request payload
    payload = {
        "model": "sonar-pro",
        "messages": [
            {"role": "user", "content": "What were the results of the 2025 French Open Finals?"}
        ]
    }

    # Make the API call
    response = requests.post(url, headers=headers, json=payload)

    # Print the AI's response
    print(response.text)
    print(response.json()) # replace with print(response.json()["choices"][0]['message']['content']) for just the content


if __name__ == "__main__":
    load_dotenv()
    main()
