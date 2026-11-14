# Week 2 - Provider-agnostic LLM client

This project uses one `LLMClient` interface with either a local Ollama model or the optional Gemini API. You can complete the Ollama path without a Gemini API key.

## Requirements
- Python 3.10+
- Ollama installed and running
- The `llama3.2` model downloaded

## Windows PowerShell commands

Open PowerShell in this folder:

```powershell
ollama --version
ollama pull llama3.2
ollama list
```

If Ollama is installed and running, install Python dependencies:

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

Run the program:

```powershell
python main.py
```

Choose `1` for Ollama, then type a prompt.

Run the unit test:

```powershell
python -m unittest -v
```

## Optional Gemini
Put your Gemini API key in `.env` as `GEMINI_API_KEY=your_key_here`, then choose option `2`. Never share your `.env` file.

## Troubleshooting
- If the model is missing: `ollama pull llama3.2`
- If Ollama is not responding: open the Ollama desktop app, then retry.
- Ollama's local API is expected at `http://localhost:11434`.
