#requesting an image and saving it
import requests
import shutil

r = requests.get("https://picsum.photos/1200/900", stream=True)
if r.status_code == 200:
    with open("response.jpeg", 'wb') as f:
        r.raw.decode_content = True
        print(str(r.raw))
        shutil.copyfileobj(r.raw, f)  