import json
import requests
body = json.dumps({
 "notification": "Hello World!",
 "accessCode": "ACCESS_CODE"
})
requests.post(url = "https://api.notifymyecho.com/v1/NotifyMe", data = body)
