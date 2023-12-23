# Todo-Sensei
<p align="center">
A Telegram bot named Todo-Sensei was developed using the Telegram API. It is intended to keep tabs on your daily exercises and assist you. In order to discern between sentences and classify them into distinct intentions, it makes advantage of Node's Natural Language Processing to do so. It offers built-in methods (like "/pomodoro") that enable users to make advantage of their features. 
  
  
The Pomodoro Technique is a time management method that aims to increase productivity and attention. It is based on dividing labor into manageable periods of 25 minutes each, known as "pomodoros." You concentrate completely on the subject at hand during a pomodoro, striving to remove distractions and maintain high-quality attention. After 25 minutes, you take a 5-minute break to relax and refuel. This cycle is repeated, with every four pomodoros followed by a 15-30 minute respite. The approach helps people retain attention, minimize burnout, and increase productivity by arranging work into regular periods and pauses. It's a simple but powerful strategy that encourages a healthy mix of intensive work and frequent rest, eventually increasing productivity and job completion.

After you have entered "/pomodoro \<session name\>", \<session name\> executes.

- Sending the text `/pomodoro status` will let you know how much time you have left in your current Pomodoro session or break.
- Sending any other phrase will start a 25 minute pomodoro session. You'll be notified 25 minutes later via text to take a break. And then will be notified 7 minutes after that to get back to work (at which point you can send another phrase to start the Pomodoro session).
- Sending the word `/pomodoro clear` will clear all sessions. 

Get Started
Get your own Telegram token from BotFather. More on that here. Then, plug in the token at the top of index.js.

Clone this reposity and run:
npm install
Run the bot:
npm run bot

