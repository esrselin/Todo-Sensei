# Todo-Sensei 🧠⏳  
**Telegram Pomodoro & NLP Productivity Bot**

Todo-Sensei is a Telegram bot that helps users stay focused and productive by combining the **Pomodoro time management technique** with **basic Natural Language Processing (NLP)**.  
Users can start Pomodoro sessions with custom names, check remaining time or break status, clear sessions, and interact with the bot through simple conversational messages.

The project is mainly built with **Node.js**, using the Telegram Bot API, and includes a small **Python prototype** for basic to-do list commands.

---

## ✨ Features

- Start Pomodoro sessions via Telegram
- Custom session names (e.g. coding, studying, reading)
- Session status tracking (work / break & remaining time)
- Clear and reset Pomodoro sessions
- NLP-based intent detection (greetings, casual messages)
- Modular and readable code structure

---

## 🧱 Project Structure

```

Todo-Sensei/
├─ .gitattributes
├─ .gitignore
├─ README.md
├─ package.json
├─ package-lock.json
│
├─ index.js               # Main entry: Telegram bot setup & command routing
├─ pomo.js                # Pomodoro session logic (timers, status, clear)
├─ nlpcontrol.js          # NLP intent classification & responses
├─ classifier.json        # Trained NLP classifier model
│
└─ todosensei.py          # Python prototype (basic to-do list commands)

````

---

## 🛠️ Tech Stack

- Node.js
- Telegram Bot API (`node-telegram-bot-api`)
- Natural Language Processing (`natural`, `node-nlp`)
- Python (prototype script)

---

## ✅ Requirements

- Node.js (LTS recommended)
- npm
- Telegram Bot Token (from **@BotFather**)

---

## ⚙️ Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/esrselin/Todo-Sensei.git
cd Todo-Sensei
````

### 2️⃣ Install dependencies

```bash
npm install
```

### 3️⃣ Add your Telegram Bot Token

Open `index.js` and replace the token with your own Telegram Bot token.

> You can optionally move the token to a `.env` file for better security.

Example:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

---

## ▶️ Run the Bot

### Option 1 — Run directly

```bash
node index.js
```

### Option 2 — Using npm script

```bash
npm run bot
```

---

## 🤖 How to Use (Telegram Commands)

### Start a Pomodoro session

```text
/pomodoro <session_name>
```

Example:

```text
/pomodoro coding
```

### Check current session status

```text
/pomodoro status
```

### Clear all sessions

```text
/pomodoro clear
```

---

## 🧩 How It Works

* `index.js` listens for incoming Telegram messages and commands.
* Pomodoro-related commands are handled by `pomo.js`, which:

  * Starts work sessions
  * Switches to break mode
  * Tracks elapsed and remaining time
  * Clears sessions when requested
* `nlpcontrol.js` uses a trained classifier (`classifier.json`) to detect simple user intents and respond accordingly.
* `todosensei.py` is an early Python prototype demonstrating basic to-do list logic.

---

## 🚀 Possible Improvements

* Persistent session storage (Redis / database)
* Multi-user session isolation
* Extended NLP intents (tasks, reminders, motivation)
* Full to-do list integration into the Node.js bot
* Deployment with Docker

---

## 🧱 Project Demo

![pomodoro-gif](https://github.com/esrselin/Todo-Sensei/blob/main/to-dosensei.gif)

