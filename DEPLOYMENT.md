# Deployment Guide

This document provides instructions for deploying the Telegram Echo Bot to various free hosting platforms.

## Prerequisites

1. Create a Telegram bot via [@BotFather](https://t.me/botfather)
   - Send `/newbot` to BotFather
   - Follow the prompts to create your bot
   - Save the API token provided

## Deployment Options Comparison

| Platform | Free Tier | Always-On | Auto-Deploy | Setup Difficulty | Recommendation |
|----------|-----------|-----------|-------------|------------------|----------------|
| **Render** | 750hrs/month | ⚠️ Spins down after 15min idle | ✅ Yes | ⭐ Easy | **Best for beginners** |
| **Fly.io** | 3 shared VMs | ✅ Yes | ✅ Yes | ⭐⭐ Medium | **Best for reliability** |
| **Railway** | $5 credit/month | ✅ Yes | ✅ Yes | ⭐ Easy | Limited free tier |

## Option 1: Deploy to Render (Recommended for Ease)

### Manual Deployment

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Configure:
   - **Name**: `arrogant-chatbot`
   - **Runtime**: Python 3
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python bot.py`
5. Add Environment Variable:
   - **Key**: `TELEGRAM_BOT_TOKEN`
   - **Value**: Your bot token from BotFather
6. Click "Create Web Service"

### Using render.yaml (Infrastructure as Code)

The repository includes a `render.yaml` file for automatic setup:

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click "New +" → "Blueprint"
3. Connect your repository
4. Render will detect `render.yaml` automatically
5. Set the `TELEGRAM_BOT_TOKEN` environment variable
6. Deploy!

**Note**: Render free tier services spin down after 15 minutes of inactivity. The bot will automatically wake up when it receives a message, but there may be a slight delay for the first message.

## Option 2: Deploy to Fly.io (Recommended for Always-On)

### Prerequisites

```bash
# Install Fly CLI
curl -L https://fly.io/install.sh | sh

# Login to Fly
fly auth login
```

### Deployment Steps

1. **Launch the app**:
   ```bash
   fly launch
   ```
   - Choose a name or press Enter for auto-generated
   - Select a region close to you
   - Don't deploy yet - we need to set secrets first

2. **Set your bot token**:
   ```bash
   fly secrets set TELEGRAM_BOT_TOKEN=your_token_here
   ```

3. **Deploy**:
   ```bash
   fly deploy
   ```

4. **Check status**:
   ```bash
   fly status
   fly logs
   ```

### Updating the Bot

```bash
fly deploy
```

## Option 3: Deploy to Railway

1. Go to [Railway](https://railway.app/)
2. Click "New Project" → "Deploy from GitHub repo"
3. Select your repository
4. Add environment variable:
   - **Key**: `TELEGRAM_BOT_TOKEN`
   - **Value**: Your bot token
5. Railway will auto-detect Python and deploy

## GitHub Actions Auto-Deployment

The repository includes GitHub Actions workflows for automatic deployment:

### For Render

Render automatically deploys on push to main branch if you set it up via Blueprint or enable auto-deploy in the dashboard.

### For Fly.io

1. Get your Fly API token:
   ```bash
   fly auth token
   ```

2. Add it as a GitHub secret:
   - Go to your repository → Settings → Secrets and variables → Actions
   - Add new secret: `FLY_API_TOKEN` = your token

3. The workflow in `.github/workflows/deploy.yml` will automatically deploy on push to main

## Local Testing

1. Clone the repository:
   ```bash
   git clone https://github.com/degru82/arrogant-chatbot.git
   cd arrogant-chatbot
   ```

2. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Set your bot token:
   ```bash
   export TELEGRAM_BOT_TOKEN=your_token_here  # On Windows: set TELEGRAM_BOT_TOKEN=your_token_here
   ```

5. Run the bot:
   ```bash
   python bot.py
   ```

6. Test by sending messages to your bot on Telegram!

## Troubleshooting

### Bot not responding

- Check that `TELEGRAM_BOT_TOKEN` is set correctly
- Check logs: `fly logs` (Fly.io) or via Render dashboard
- Ensure the bot is running: `fly status`

### Deployment failed

- Verify `requirements.txt` is present
- Check Python version compatibility (3.11+ recommended)
- Review deployment logs for specific errors

### Bot stops after some time

- This is expected on Render free tier (spins down after inactivity)
- Use Fly.io for always-on functionality
- Or upgrade to Render paid tier

## Cost Comparison

- **Render Free**: $0/month (with 15min spin-down)
- **Fly.io Free**: $0/month (3 VMs included)
- **Railway Free**: ~$5 credit/month
- **Render Starter**: $7/month (always-on)

## Recommendation

- **For learning/testing**: Use Render (easiest setup)
- **For production/always-on**: Use Fly.io (free and reliable)
- **For quick prototypes**: Use Railway (simple but limited free tier)
