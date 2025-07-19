# OpenAI Agents SDK

A Python project that leverages the Gemini API (via `openai-agents`) to analyze user moods, suggest activities, provide country information, and recommend products or treatments based on user input. The project is modular, with each script serving a distinct purpose, and is designed for interactive command-line use.

---

## Table of Contents

- [Features](#features)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Environment Variables](#environment-variables)
- [Usage](#usage)
  - [Mood Analyzer](#mood-analyzer)
  - [Country Info Toolkit](#country-info-toolkit)
  - [Product Suggester](#product-suggester)
- [Dependencies](#dependencies)
- [Notes](#notes)
- [License](#license)

---

## Features

- **Mood Analysis & Activity Suggestions:**  
  Analyze a user's mood and suggest personalized activities to improve or maintain their emotional state.

- **Country Information Toolkit:**  
  Retrieve the capital, language(s), and population for any country using AI-powered agents.

- **Product & Treatment Suggestions:**  
  Get product or treatment recommendations based on symptoms described by the user.

---

## Project Structure

```
.
├── mood_handoff.py           # Main mood analysis and activity suggestion script
├── country_info_toolkit.py   # Country information retrieval tool
├── product_suggester.py      # Product/treatment suggestion tool
├── requirements.txt          # Python dependencies
├── pyproject.toml            # Project metadata and dependencies
├── .env                      # Environment variables (API keys, etc.)
├── .gitignore
└── README.md                 # Project documentation
```

---

## Setup & Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd mood-analyzer
   ```

2. **Create and activate a virtual environment (recommended):**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Environment Variables

Create a `.env` file in the project root with the following content:

```
GEMINI_API_KEY=your_gemini_api_key_here
```

- The `GEMINI_API_KEY` is required for all scripts to access the Gemini API via `openai-agents`.

---

## Usage

### Mood Analyzer

Analyze your mood and receive activity suggestions.

```bash
python mood_handoff.py
```

- **Prompt:**  
  `Please share your current mood (e.g., happy, sad, stressed, jolly, annoyed, etc.):`
- **Output:**  
  - Mood analysis
  - Suggested activities tailored to your mood

---

### Country Info Toolkit

Get information about any country (capital, language, population).

```bash
python country_info_toolkit.py
```

- **Prompt:**  
  `Enter a country name to get information:`
- **Output:**  
  - Country name
  - Capital
  - Language(s)
  - Population

---

### Product Suggester

Get product or treatment advice based on your symptoms.

```bash
python product_suggester.py
```

- **Prompt:**  
  `Please describe your symptom (e.g., 'I have a headache'):`
- **Output:**  
  - Suggested product or treatment

---

## Dependencies

- `openai-agents` (>=0.2.2)
- `python-dotenv` (>=1.1.1)
- `asyncio` (>=3.4.3)

All dependencies are listed in `requirements.txt` and `pyproject.toml`.

---

## Notes

- All scripts require a valid Gemini API key in the `.env` file.
- The project uses the `openai-agents` package to interact with the Gemini API, which provides the agent-based architecture for all functionalities.
- The scripts are designed for interactive use in a terminal or command prompt.

---

## License

[MIT License](LICENSE)  

---
