from abc import ABC, abstractmethod
import requests

try:
    from google import genai
except ImportError:
    genai = None


class LLMProvider(ABC):
    @abstractmethod
    def generate(self, prompt: str) -> str:
        pass


class OllamaProvider(LLMProvider):
    def __init__(self, model="llama3.2", url="http://localhost:11434/api/generate"):
        self.model = model
        self.url = url

    def generate(self, prompt: str) -> str:
        response = requests.post(
            self.url,
            json={"model": self.model, "prompt": prompt, "stream": False},
            timeout=180,
        )
        response.raise_for_status()
        return response.json()["response"]


class GeminiProvider(LLMProvider):
    """Optional hosted provider. Ollama works without a Gemini API key."""
    def __init__(self, api_key: str, model="gemini-2.5-flash"):
        if genai is None:
            raise RuntimeError("Install google-genai to use Gemini.")
        self.client = genai.Client(api_key=api_key)
        self.model = model

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model=self.model,
            contents=prompt,
        )
        return response.text or ""


class LLMClient:
    def __init__(self, provider: LLMProvider):
        self.provider = provider

    def generate(self, prompt: str) -> str:
        return self.provider.generate(prompt)
