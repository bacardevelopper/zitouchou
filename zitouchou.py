import keyboard

class Zitouchou:
    def __init__(self):
        pass

    def keylogger_space(self):
        while True:
            keyboard.wait('space')
            print(' "space" a été appuyé')
            keyboard.wait('esc')
            print(' esc a été appuyé')

def main():
    zitouchou = Zitouchou()
    zitouchou.keylogger_space()

if __name__ == "__main__":
    main()
