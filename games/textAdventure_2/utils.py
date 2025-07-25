## === utils.py ===
import sys
import os
import string

def clear_screen():
    import os
    os.system("cls" if os.name == "nt" else "clear")


def get_input(prompt=""):
    print(prompt, end="", flush=True)
    valid_chars = string.ascii_letters + string.digits + string.punctuation + " "

    try:
        # Windows
        import msvcrt
        while True:
            ch = msvcrt.getch()
            if ch == b'\x1b':  # ESC key
                return 'p'
            if ch in [b'\x00', b'\xe0']:  # Arrow or function key prefix
                msvcrt.getch()  # discard next byte
                continue
            char = ch.decode().lower()
            if char in valid_chars:
                return char
    except ImportError:
        # Unix (macOS/Linux)
        import tty
        import termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            while True:
                ch = sys.stdin.read(1)
                if ch == '\x1b':  # ESC key
                    return 'p'
                if ch in valid_chars:
                    return ch.lower()
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)

