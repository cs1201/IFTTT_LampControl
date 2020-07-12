import requests
import json
import rumps

WEBHOOK_BASEURL = "https://maker.ifttt.com/trigger"

with open('ifttt_key.json') as f:
    WEBHOOK_KEY = json.load(f)['key'] 

LAMP_ON_EVENT = 'desk_lamp_ON'
LAMP_OFF_EVENT = 'desk_lamp_OFF'

class LampControl(rumps.App):
    def __init__(self):
        super(LampControl, self).__init__('LampControl', icon='app_icon.png')
        self.menu = ["ON", "OFF", None]

    def _request(self, event_name):
        request_url = f"{WEBHOOK_BASEURL}/{event_name}/with/key/{WEBHOOK_KEY}"
        post = requests.post(request_url)
        if debug:
            if post.status_code != 200:
                print("BAD RESPONSE!")
            else:
                print("POST successful!")

    @rumps.clicked("ON")
    def on(self, _):
        self._request(LAMP_ON_EVENT)

    @rumps.clicked("OFF")
    def off(self, _):
        self._request(LAMP_OFF_EVENT)

if __name__ == "__main__":
    debug = False
    LampControl().run()