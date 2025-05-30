import os
import subprocess
import threading
import scripts.functions as functions


variables = functions.load_json("general")

def run_script(bot_name):
    python_path = os.path.join("bot-env", "bin", "python")
    subprocess.run([python_path, "bot.py", bot_name])


botThreads = []

if __name__ == "__main__":
    for bot in variables["Bots"]:
        botThread = threading.Thread(target=run_script, args=(bot,))
        botThreads.append(botThread)
        botThread.start()
    
    for thread in botThreads:
        thread.join()
