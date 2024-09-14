import requests
import json

# Define the request URL and headers
url = "https://ap-northeast-2.apistage.ai/v1/web/demo/chat/completions"
headers = {
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    "Origin": "https://console.upstage.ai",
    "Referer": "https://console.upstage.ai/"
}

# Prepare the request payload
payload = {
    "stream": True,
    "messages": [
        {
            "role": "user",
            "content": "Provide practical tips for beginner yoga practitioners, covering basics and common practices."
        }
    ],
    "model": "solar-pro"
}

# Send the POST request
response = requests.post(url, headers=headers, json=payload, stream=True)

# Check if the request was successful
if response.status_code == 200:

    # Manually parse the SSE response
    for line in response.iter_lines():
        if line:
            line = line.decode('utf-8')
            if line.startswith('data: '):
                data = line[6:]  # Remove 'data: ' prefix
                if data != "[DONE]":
                    try:
                        json_data = json.loads(data)
                        content = json_data['choices'][0]['delta'].get('content', '')
                        if content:
                            print(content, end='', flush=True)
                    except json.JSONDecodeError:
                        print(f"Error decoding JSON: {data}")
