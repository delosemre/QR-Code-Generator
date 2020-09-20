import pyqrcode
import png

add=input("The address (link) or message you want to open with the QR Code:")
url=pyqrcode.create(add)

print("""
1-) SVG
2-) PNG
""")
output=input("Output Type:")
outputname=input("Name of output file:")
if output=="1":
    url.svg(outputname+'.svg',scale=8)

elif output=="2":
    url.png(outputname+'.png',scale=8)

else: 
    print("Incorrect entry")

