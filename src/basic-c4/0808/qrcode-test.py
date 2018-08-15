import qrcode
img = qrcode.make("https://tabelog.com/okinawa/A4701/A470101/47012670/")
img.save("qrcode-test.png")
