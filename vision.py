import base64
from advanced import send_message
from mss import mss
from pynput import keyboard

def take_screenshot():
    with mss() as sct:
        sct.shot()

def encode_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
    
def on_press(key):
    try:
        if key.char == 'p':
            take_screenshot()
            image = encode_image("monitor-1.png")
            text = input("Text: ")

            response = send_message([
                {
                    "type": "text", 
                    "text": text
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image}"}
                }
                ])
            
            print(response)
    except:
        pass

def main():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()