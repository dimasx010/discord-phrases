# 📘 Discord Phrases
![Deploy](https://github.com/dimasx010/discord-phrases/actions/workflows/discord-phrase.yml/badge.svg)
![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python)
---
_Elegant, lightweight Phrase Manager for sending phrases to Discord(Python)_
- Run workflows every day (Workflow Job)
- Select phrase from ``phrases.json``
- Send a message to a specific channel of a Discord server

## 🖼 Preview
<img width="527" height="111" alt="image" src="https://github.com/user-attachments/assets/58041e39-492a-4749-8f09-e1e4873d1d44" />

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
│── phrases.json
│── main.py
│── .github/
│   └── workflows/
│       └── discord-phrase.yml
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

## 🔄 GitHub Actions (CI)  
Example workflow for `.github/workflows/discord-phrase.yml`:

```yaml
name: Run Command
on:
    schedule:
        - cron: '0 10 * * *' # At every hour
    workflow_dispatch: # manually
permissions:
  contents: write
jobs:
  Build-and-run-python:
    concurrency: ci-${{ github.ref }} # Recommended if you intend to make multiple deployments in quick succession.
    runs-on: ubuntu-latest
    steps:
      - name: 🛎️ Checkout 
        uses: actions/checkout@v4
        
      - name: ⚙ Setup python 
        uses: actions/setup-python@v4
        with:
          python-version: '3.9' # install the python version needed
      - name: Export env variable
        run: |
            echo "DISCORD_BOT_TOKEN=${{ secrets.DISCORD_BOT_TOKEN }}" >> $GITHUB_ENV
            echo "DISCORD_CHANNEL_ID=${{ secrets.DISCORD_CHANNEL_ID }}" >> $GITHUB_ENV
      - name: 🔧 Run command  # This example project is built using npm and outputs the result to the 'build' folder. Replace with the commands required to build your project, or remove this step entirely if your site is pre-built.
        run: |
          echo "Ejecución: $(date)"
          pip install -r requirements.txt -q
          python main.py
```

---

## 📜 License  
Licensed under the **MIT License**
