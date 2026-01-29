# Arrogant Chatbot

A Telegram echo bot built with Python that repeats back whatever you say.

## Introduction

This repository is a sort of my learning-by-doing projects for vibe-coding with github action and claude code.

My objectives are here.
- Building a telegram chatbot only using vibe-coding.
  - All I need to do should be limited to reading the code lines and guiding how to improve or asking what have been done.
  - Vibe-coding should be available anywhere, literally, so I should be able to edit the repo in the bed.
- Testing vibe-coding methods.
  - McDonalds? Requirement-driven? Search web for those vibe-coding methods and test it here.

## Features

- Echo back any text message sent by users
- `/start` command - Welcome message
- `/help` command - Show available commands

## Setup

### Prerequisites

- Python 3.11+
- A Telegram Bot Token (get one from [@BotFather](https://t.me/botfather))

### Local Development

1. Clone the repository:
   ```bash
   git clone https://github.com/degru82/arrogant-chatbot.git
   cd arrogant-chatbot
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set the environment variable:
   ```bash
   export TELEGRAM_BOT_TOKEN="your-bot-token-here"
   ```

4. Run the bot:
   ```bash
   python bot.py
   ```

### Docker

Build and run with Docker:

```bash
docker build -t telegram-echo-bot .
docker run -e TELEGRAM_BOT_TOKEN="your-bot-token-here" telegram-echo-bot
```

## Deployment

### Railway

1. Create a new project on [Railway](https://railway.app)
2. Connect your GitHub repository
3. Add the `TELEGRAM_BOT_TOKEN` environment variable in Railway settings
4. Deploy!

For automatic deployments via GitHub Actions:
- Add `RAILWAY_TOKEN` to your repository secrets

### Render

1. Create a new Worker on [Render](https://render.com)
2. Connect your GitHub repository
3. Add the `TELEGRAM_BOT_TOKEN` environment variable
4. Deploy!

## Project Structure

```
arrogant-chatbot/
├── bot.py              # Main bot application
├── requirements.txt    # Python dependencies
├── Dockerfile          # Docker configuration
├── railway.json        # Railway deployment config
├── render.yaml         # Render deployment config
└── .github/
    └── workflows/
        └── deploy.yml  # GitHub Actions deployment workflow
``` 
