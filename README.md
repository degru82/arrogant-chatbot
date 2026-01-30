# Arrogant Chatbot

A Telegram echo bot built using vibe-coding with Claude Code and GitHub Actions.

## Introduction

This repository is a learning-by-doing project for vibe-coding with GitHub Action and Claude Code.

### Objectives

- Building a telegram chatbot only using vibe-coding.
  - All I need to do should be limited to reading the code lines and guiding how to improve or asking what have been done.
  - Vibe-coding should be available anywhere, literally, so I should be able to edit the repo in the bed.
- Testing vibe-coding methods.
  - McDonalds? Requirement-driven? Search web for those vibe-coding methods and test it here.

## What This Bot Does

This is a simple Telegram echo bot that repeats everything you send to it:
- Text messages → echoed back
- Photos → echoed back
- Stickers → echoed back
- Voice messages → echoed back
- Videos → echoed back
- Documents → echoed back

### Commands

- `/start` - Start the bot and get a welcome message
- `/help` - Show help information

## Quick Start

### 1. Create Your Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` and follow the prompts
3. Save the bot token provided

### 2. Deploy (Choose One)

#### Option A: Render (Easiest)

1. Fork this repository
2. Go to [Render Dashboard](https://dashboard.render.com/)
3. New + → Blueprint
4. Connect your forked repository
5. Set environment variable: `TELEGRAM_BOT_TOKEN` = your token
6. Deploy!

#### Option B: Fly.io (Always-On)

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login and deploy
fly auth login
fly launch
fly secrets set TELEGRAM_BOT_TOKEN=your_token_here
fly deploy
```

#### Option C: Local Testing

```bash
# Clone the repository
git clone https://github.com/degru82/arrogant-chatbot.git
cd arrogant-chatbot

# Setup virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set bot token and run
export TELEGRAM_BOT_TOKEN=your_token_here  # Windows: set TELEGRAM_BOT_TOKEN=your_token_here
python bot.py
```

## Deployment Details

See [DEPLOYMENT.md](DEPLOYMENT.md) for comprehensive deployment instructions including:
- Platform comparison (Render vs Fly.io vs Railway)
- Step-by-step guides for each platform
- GitHub Actions auto-deployment setup
- Troubleshooting tips

## Project Structure

```
.
├── bot.py                          # Main bot implementation
├── requirements.txt                # Python dependencies
├── Dockerfile                      # Container configuration
├── render.yaml                     # Render deployment config
├── fly.toml                        # Fly.io deployment config
├── DEPLOYMENT.md                   # Detailed deployment guide
├── .github/
│   └── workflows/
│       ├── claude.yml              # Claude Code integration
│       ├── claude-code-review.yml  # Code review automation
│       └── deploy-flyio.yml        # Auto-deployment to Fly.io
└── README.md                       # This file
```

## Technology Stack

- **Language**: Python 3.11+
- **Framework**: python-telegram-bot 21.0.1
- **Deployment**: Render / Fly.io / Railway
- **CI/CD**: GitHub Actions

## Development

This project uses "vibe-coding" - development driven by natural language instructions to Claude Code through GitHub Actions.

To contribute or modify:
1. Create an issue describing the change
2. Tag `@claude` in a comment with your instructions
3. Claude will implement, test, and create a PR
4. Review and merge!

## License

This is a learning project. Feel free to fork and experiment!

## Links

- [Create your own Telegram bot](https://t.me/botfather)
- [python-telegram-bot documentation](https://docs.python-telegram-bot.org/)
- [Render](https://render.com/)
- [Fly.io](https://fly.io/)
