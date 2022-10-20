import pyqrcode

'''
big_code = pyqrcode.create('0973326355', error='L', version=6, mode='binary')
big_code.png('code.png', scale=1, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff])
#big_code.show()


number = pyqrcode.create(123456789012345)
number.png('code1.png', scale=1, module_color='red', background=[0xff, 0xff, 0xff])
number.show()
'''

number2 = pyqrcode.create('google.com')
number2.png('code3.png', scale=1, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xff], quiet_zone=10)
#number2.show()

'''
text = pyqrcode.create('Example')
print(text.terminal())
print(text.terminal(module_color='red', background='yellow').show())
print(text.terminal(module_color=5, background=123, quiet_zone=1))
text.show()
'''

'''


>>>>>>>>>>>>>adding logo to the qrcode<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

# import modules
import qrcode
from PIL import Image

# taking image which user wants
# in the QR code center
Logo_link = 'g4g.jpg'

logo = Image.open(Logo_link)

# taking base width
basewidth = 100

# adjust image size
wpercent = (basewidth/float(logo.size[0]))
hsize = int((float(logo.size[1])*float(wpercent)))
logo = logo.resize((basewidth, hsize), Image.ANTIALIAS)
QRcode = qrcode.QRCode(
	error_correction=qrcode.constants.ERROR_CORRECT_H
)

# taking url or text
url = 'https://www.geeksforgeeks.org/'

# adding URL or text to QRcode
QRcode.add_data(url)

# generating QR code
QRcode.make()

# taking color name from user
QRcolor = 'Green'

# adding color to QR code
QRimg = QRcode.make_image(
	fill_color=QRcolor, back_color="white").convert('RGB')

# set size of QR code
pos = ((QRimg.size[0] - logo.size[0]) // 2,
	(QRimg.size[1] - logo.size[1]) // 2)
QRimg.paste(logo, pos)

# save the QR code generated
QRimg.save('gfg_QR.png')

print('QR code generated!')
'''

#for web development
code = pyqrcode.create('Are you suggesting coconuts migrate?')
image_as_str = code.png_as_base64_str(scale=5)
html_img = '<img src="data:image/png;base64,{}">'.format(image_as_str)