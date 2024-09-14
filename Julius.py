import uuid
import requests
import json
from typing import Any, Dict

class Julius:
    AVAILABLE_MODELS = [
        "Llama 3",
        "GPT-4o",
        "GPT-3.5",
        "Command R",
        "Gemini Flash",
        "Gemini 1.5",
        "Claude Sonnet",
        "Claude Opus",
        "Claude Haiku",
        "GPT-4",
        "GPT-4o mini",
        "Command R+",
    ]

    def __init__(
        self,
        timeout: int = 30,
        proxies: dict = {},
        model: str = "Gemini Flash",


    ):
        if model not in self.AVAILABLE_MODELS:
            raise ValueError(f"Invalid model: {model}. Choose from: {self.AVAILABLE_MODELS}")

        self.session = requests.Session()
        self.chat_endpoint = "https://api.julius.ai/api/chat/message"
        self.stream_chunk_size = 64
        self.timeout = timeout
        self.last_response = {}
        self.model = model
        self.headers = {
            "accept": "*/*",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9,en-IN;q=0.8",
            "authorization": "Bearer",
            "content-type": "application/json",
            "conversation-id": str(uuid.uuid4()),
            "dnt": "1",
            "interactive-charts": "true",
            "is-demo": "temp_14aabbb1-95bc-4203-a678-596258d6fdf3",
            "is-native": "false",
            "orient-split": "true",
            "origin": "https://julius.ai",
            "platform": "undefined",
            "priority": "u=1, i",
            "referer": "https://julius.ai/",
            "request-id": str(uuid.uuid4()),
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
            "visitor-id": str(uuid.uuid4())
        }

        self.session.headers.update(self.headers)
        self.session.proxies = proxies

    def ask(
        self,
        prompt: str,
        stream: bool = False,
        raw: bool = False,
    ) -> Dict[str, Any]:
        payload = {
            "message": {"content": prompt, "role": "user"},
            "provider": "default",
            "chat_mode": "auto",
            "client_version": "20240130",
            "theme": "dark",
            "new_images": None,
            "new_attachments": None,
            "dataframe_format": "json",
            "selectedModels": [self.model]
        }

        def for_stream():
            response = self.session.post(
                self.chat_endpoint, json=payload, headers=self.headers, stream=True, timeout=self.timeout
            )

            if not response.ok:
                raise Exception(f"Failed to generate response - ({response.status_code}, {response.reason})")

            streaming_response = ""
            for line in response.iter_lines(decode_unicode=True):
                if line:
                    try:
                        json_line = json.loads(line)
                        content = json_line['content']
                        streaming_response += content
                        yield content if raw else dict(text=streaming_response)
                    except:
                        continue
            self.last_response.update(dict(text=streaming_response))

        def for_non_stream():
            response = self.session.post(
                self.chat_endpoint, json=payload, headers=self.headers, timeout=self.timeout
            )

            if not response.ok:
                raise Exception(f"Failed to generate response - ({response.status_code}, {response.reason})")

            full_content = ""
            for line in response.text.splitlines():
                try:
                    data = json.loads(line)
                    if "content" in data:
                        full_content += data['content']
                except json.JSONDecodeError:
                    pass
            self.last_response.update(dict(text=full_content))
            return self.last_response

        return for_stream() if stream else for_non_stream()

    def chat(
        self,
        prompt: str,
        stream: bool = False,
    ) -> str:
        def for_stream():
            for response in self.ask(prompt, True):
                yield self.get_message(response)

        def for_non_stream():
            return self.get_message(self.ask(prompt, False))

        return for_stream() if stream else for_non_stream()

    def get_message(self, response: dict) -> str:
        assert isinstance(response, dict), "Response should be of dict data-type only"
        return response["text"]

if __name__ == '__main__':
    from rich import print
    ai = Julius()
    response = ai.chat("who is manoj bisht from PWD Uttarakhand")
    for chunk in response:
        print(chunk, end="", flush=True)
