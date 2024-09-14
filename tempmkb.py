import requests

def generate_request(query, max_tokens=500, temperature=0.7, system_prompt="Be Helpful and Friendly. Keep your response straightfoward, short and concise"):
    url = "https://devsdocode-openrouter.hf.space/generate"
    params = {
        "query": query,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "system_prompt": system_prompt
    }
    response = requests.get(url, params=params)
    return response.json()

if __name__ == "__main__":
    # Example usage:
    query = "Write 20 lines about India each in different languages"
    response = generate_request(query, max_tokens=500, temperature=0.7)
    print(response[0]['response'])
