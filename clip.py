import keyboard
import pyperclip
from time import sleep

print("Clipboard listener script running.")
print("press esc at any time to terminate the program.")
while True:
    try:
        if keyboard.is_pressed('ctrl+c'):
            sleep(0.3)
            text = pyperclip.paste().strip() + "\n"
            f = open("board.txt", "a")
            f.write(text)       
            f.close()
        elif keyboard.is_pressed('esc'):
            print("terminating...")
            break

    except Exception as error:
        print(error)
