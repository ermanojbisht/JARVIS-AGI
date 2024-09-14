import requests
import json
from typing import Iterable

def process_stream(response: requests.Response) -> None:
    """
    Process a streaming response from the TwitterClone API.

    :param response: The response object
    :return: None
    """
    buffer = ""
    for chunk in response.iter_content(chunk_size=1):
        if chunk:
            chunk = chunk.decode('utf-8')
            buffer += chunk
            if chunk == '\n' and buffer.startswith('data: '):
                try:
                    data = json.loads(buffer[6:])
                    content = data['choices'][0]['delta'].get('content', '')
                    if content:
                        print(content, end='', flush=True)
                except json.JSONDecodeError:
                    pass
                buffer = ""

url = "https://twitterclone-i0wr.onrender.com/api/chat"
headers = {
    "Content-Type": "application/json",
    "Origin": "https://www.aiuncensored.info",
    "Referer": "https://www.aiuncensored.info/",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0"
}
payload = {
    "messages": [
        {
            "role": "system",
            "content": "You are a creative assistant..."
        },
        {
            "role": "user",
            "content": "Write me a paragraph about working of AI."
        }
    ]
}

try:
    with requests.post(url, headers=headers, json=payload, stream=True) as response:
        process_stream(response)
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")
