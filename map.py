from app.drawing import main
from app import app
import keyboard
import time
import webbrowser



if __name__ == '__main__':
   webbrowser.open_new('http://127.0.0.1:5000')
   keyboard.add_hotkey("alt + j", lambda: time.sleep(0.1))
   keyboard.add_hotkey("alt + j", main)
   app.run()


