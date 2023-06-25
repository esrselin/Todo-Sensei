from telegram.ext import Updater, CommandHandler

# Initialize the bot
updater = Updater('6156564013:AAGlx6TVwZAqGX2_JIo8rEHJ8HYcJjR7JCU', use_context=True)
dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to your to-do list!")

def add_task(update, context):
    task = ' '.join(context.args)
    # ToDo: Add the task to your to-do list storage (e.g., database or file)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Added task: {task}")

def list_tasks(update, context):
    # ToDo: Retrieve the tasks from your to-do list storage
    tasks = ['Task 1', 'Task 2', 'Task 3']  # Replace with your implementation
    task_list = '\n'.join(tasks)
    context.bot.send_message(chat_id=update.effective_chat.id, text=f"Tasks:\n{task_list}")

def main():
    # Initialize the bot with your token
    updater = Updater('6156564013:AAGlx6TVwZAqGX2_JIo8rEHJ8HYcJjR7JCU', use_context=True)
    dispatcher = updater.dispatcher

    # Define the command handlers
    start_handler = CommandHandler('start', start)
    add_handler = CommandHandler('add', add_task)
    list_handler = CommandHandler('list', list_tasks)

    # Register the command handlers
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(add_handler)
    dispatcher.add_handler(list_handler)

    # Start the bot
    updater.start_polling()

if __name__ == '__main__':
    main()


