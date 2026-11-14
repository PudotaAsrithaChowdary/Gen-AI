# Week 1 - Gemini API Python starter

## Requirements
- Python 3.10 or newer
- A Gemini API key

## Setup (Windows PowerShell)

1. Extract this ZIP and open the `Week_1` folder in VS Code.
2. Open the VS Code terminal (`Terminal` -> `New Terminal`).
3. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

4. Activate it:

   ```powershell
   .\.venv\Scripts\Activate.ps1
   ```

   If PowerShell blocks activation, use Command Prompt and run:
   `.venv\Scripts\activate.bat`

5. Install the packages:

   ```powershell
   py -m pip install -r requirements.txt
   ```

6. Copy `.env.example` to a new file named `.env`.
7. Open `.env` and replace the placeholder with your own Gemini API key.
   Do not share `.env` or upload it to GitHub.
8. Run the program:

   ```powershell
   py main.py
   ```

## Notes
- The program sends the prompt in `main.py` to the Gemini API and prints the response.
- If you get a model-not-found or access error, check the model name in
  `main.py` against the models currently available to your Gemini API key.
- Keep `.env` private. The `.gitignore` file excludes it from Git.
