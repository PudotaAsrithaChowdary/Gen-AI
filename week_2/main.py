import os
from dotenv import load_dotenv
from llm_client import GeminiProvider, OllamaProvider, LLMClient

load_dotenv()

print("WEEK 2 - PROVIDER-AGNOSTIC LLM CLIENT")
print("1. Ollama (local)")
print("2. Gemini (optional hosted API)")
choice = input("Choose provider (1/2): ").strip()

if choice == "1":
    provider = OllamaProvider(model=os.getenv("OLLAMA_MODEL", "llama3.2"))
elif choice == "2":
    api_key = os.getenv("GEMINI_API_KEY", "").strip()
    if not api_key:
        raise ValueError("Add GEMINI_API_KEY to your .env file to use Gemini.")
    provider = GeminiProvider(api_key)
else:
    raise ValueError("Invalid selection. Enter 1 or 2.")

client = LLMClient(provider)
prompt = input("Enter your question: ").strip()
if not prompt:
    raise ValueError("The prompt cannot be empty.")

print("\nLLM RESPONSE\n")
print(client.generate(prompt))
