# 🛠️ Legacy Code Migrator (Offline AI Tool)

A Python-based CLI tool that uses the **Mistral large language model** (via [Ollama](https://ollama.com)) to automatically modernize legacy code across multiple programming languages — with clear explanations of the changes.

## ✨ Features

- ✅ Detects programming language from file extension (`.py`, `.cpp`, `.java`, etc.)
- 🤖 Uses **Mistral** LLM to refactor legacy code and explain improvements
- 💾 Saves the updated code to an `outputs/` folder
- 🧠 Fully offline and privacy-preserving (runs via Ollama on your machine)
- 📂 Batch processes all files in the `inputs/` directory

## 📁 Folder Structure

```
├── inputs/            # Place your legacy code files here
├── outputs/           # Modernized code will be saved here
├── main.py            # Main Python script
├── README.md          # This file
└── requirements.txt   # Required Python packages
```

## 🚀 Getting Started

### 1. Install Dependencies

You’ll need Python 3.8+ and [Ollama](https://ollama.com) installed.

```bash
pip install -r requirements.txt
```

### 2. Install & Run Mistral via Ollama

```bash
ollama run mistral
```

> Mistral will be downloaded once (~4–6 GB), and then run locally.

### 3. Add Legacy Code Files

Place your legacy code files inside the `inputs/` folder (e.g., `.py`, `.java`, `.cpp`).

### 4. Run the Tool

```bash
python3 main.py
```

✅ You'll see progress logs, and modernized versions will be saved to the `outputs/` folder.

## 🔍 Supported Languages

- Python
- JavaScript
- Java
- C++
- C
- C#
- Ruby
- PHP
- Go
- Rust

> Files with unsupported or unknown extensions will be skipped or labeled `"unknown"`.

## 💡 How It Works

This tool uses the **Mistral 7B LLM** to:
- Understand legacy code context.
- Suggest modern syntax, practices, and improvements.
- Output a step-by-step explanation of changes.

All this is done **fully offline**, making it ideal for:
- Enterprises with security restrictions
- Offline coding environments
- Software maintenance teams

## 📌 Example Prompt Sent to Mistral

```text
Modernize this legacy Python code and explain the changes step by step:

<your legacy code here>
```

## 🧠 Why This Project Matters

Legacy code can be hard to understand and maintain. This tool helps:
- Modernize codebases without rewriting from scratch
- Educate developers by showing the rationale behind updates
- Bridge the gap between old and new code standards using AI

## 🛠️ Future Enhancements (Ideas)
- CLI menu for more interactivity
- Streamlit UI for visual use
- Git diff support to show changes clearly

## 📄 License

MIT License. Use freely.

## 🙋‍♂️ Author

Made by [Your Name], Master's student in AI.  
For inquiries: [your.email@example.com]
