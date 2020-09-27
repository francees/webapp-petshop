from PIL import Image
im = Image.open("Face.jpg")
#im.rotate(180).show()

import requests
url = "https://api.covid19api.com/summary"
r = requests.get(url)
print(r.json())