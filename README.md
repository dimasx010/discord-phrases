# 📘 Discord Phrases  
_Elegant, lightweight Phrase Manager for sending phrases to Discord(Python)_
- Run workflows every day (Workflow Job)
- Select phrase from ``phrases.json``
- Send a message to a specific channel of a Discord server

## 🖼 Preview
<img width="527" height="111" alt="image" src="https://github.com/user-attachments/assets/58041e39-492a-4749-8f09-e1e4873d1d44" />



-

---
![Deploy](https://github.com/dimasx010/discord-phrases/actions/workflows/discord-phrase.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
---

## ✨ Overview  
**discord-phrases** is a minimalistic Python utility designed to store, manage, and deliver dynamic phrases for Discord bots.  
Built for clarity, simplicity, and easy integration into any Discord.py-based project.

---

## 🚀 Features  
- 📝 Manage custom phrases easily  
- 🔀 Random phrase selection  
- 📦 Simple file-based or JSON storage  
- ⚡ Ready for CI/CD with GitHub Actions  
- 🧩 Perfect for modular Discord bot architectures

---

## 📂 Project Structure  
```
discord-phrases/
│── phrases/
│   └── phrases.json
│── src/
│   └── phrases.py
│── tests/
│── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

---

## 🛠 Installation  
Install with pip:

```
pip install discord-phrases
```

Or install from source:

```
git clone https://github.com/USER/discord-phrases.git
cd discord-phrases
pip install -r requirements.txt
```

---

## 📦 Usage Example  
```python
from phrases import PhraseManager

phrases = PhraseManager("phrases/phrases.json")

print(phrases.get_random())
print(phrases.get("greeting"))
```

---

## 🔄 GitHub Actions (CI)  
Example workflow for `.github/workflows/ci.yml`:

```yaml
name: CI

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
    - uses: actions/checkout@v4
    - uses: actions/setup-python@v5
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: pip install -r requirements.txt

    - name: Run tests
      run: pytest -q

    - name: Lint
      run: flake8 src
```

---

## 📜 License  
Licensed under the **MIT License**.




