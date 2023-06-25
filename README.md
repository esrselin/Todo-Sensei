# Todo-Sensei
<p align="center">
A bot that enhances your performance on daily tasks. 
<p align="center">
A Telegram bot named Todo-Sensei was developed using the Telegram API. It is intended to keep tabs on your daily exercises and assist you. In order to discern between sentences and classify them into distinct intentions, it makes advantage of Node's Natural Language Processing to do so. It offers built-in methods (like "/pomodoro") that enable users to make advantage of their features. 
  
  
##Quick Look
> * note "7 minutes done!" didn't take 7 minutes because of demo purposes.
  
  ## Current Techniques: #1 The Pomodoro Technique
  
  >Francesco Cirillo created the Pomodoro Technique as a time management technique in the late 1980s. The method divides work into segments that are typically 25 minutes long and are separated by brief breaks using a timer. These periods are referred described as "pomodori" after the Italian term pomodoro, which means "tomato." The approach is predicated on the notion that taking regular pauses helps boost mental flexibility.

After you have entered "/pomodoro \<session name\>", \<session name\> executes.

- Sending the text `/pomodoro status` will let you know how much time you have left in your current Pomodoro session or break.
- Sending any other phrase will start a 25 minute pomodoro session. You'll be notified 25 minutes later via text to take a break. And then will be notified 7 minutes after that to get back to work (at which point you can send another phrase to start the Pomodoro session).
- Sending the word `/pomodoro clear` will clear all sessions. 


