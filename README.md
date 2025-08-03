# Telegram Referral Bot

This is a simple Telegram bot built using [Aiogram](https://docs.aiogram.dev) (Python asynchronous framework for Telegram Bot API).  
The bot allows users to generate personal invitation links and track how many friends they have referred to the bot.

## Features

- `/start` command with referral support
- Deep linking for unique invite links
- Inline buttons for:
  - Getting an invite link
  - Checking the number of invited friends
- Simple in-memory storage for referrals (can be replaced with a database)

## How it works

1. A user starts the bot.
2. The bot generates a unique start link containing the user ID.
3. When someone joins using this link, the bot counts them as a referral.
4. The user can check how many friends they have invited anytime.

## Requirements

- Python 3.10+
- Aiogram 3.x

## How to run

1. Clone this repository.
2. Install dependencies:
