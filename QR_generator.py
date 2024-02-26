import qrcode

print("your QR Code generator")
qr=qrcode.QRCode(version=3,box_size=20,border=10)

data=input("enter the url ")
qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
#fname=input("enter the qrcodename to be saved followed by .png extention ")

fname=(input("enter the qrcodename to be saved "))+".png"
img.save(fname)