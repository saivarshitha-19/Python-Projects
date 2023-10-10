import pyqrcode
import png
from pyqrcode import QRCode


s='https://saivarshitha.netlify.app/'

url=pyqrcode.create(s)

# url.svg('myqr.svg',scale=8)
url.png('myqr1.png',scale=12)

#scale represents the size of an qrcode

