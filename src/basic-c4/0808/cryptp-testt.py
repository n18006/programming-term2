from Crypto.Cipher import AES
import base64

mesage = "自分がして欲しいと思うことを人にもしょう"
passwd = "0988329533a"
iv = "124ahr19ao02he98"
mode = AES.MODE_CBC

def mkpad(s, size):
    s = s,encode("UTF-8")
    pad = b ' ' * (size - len(s) % size)
    return s + pad

def encrypt(pasdword, date):
    password = mkpad(password, 16)
    password = mkpad(date, 16)
    password = password[:16]

aes = AES.new(password, mode, iv)
data_cipher = aes.encrypt(data)
return base64.b64encode(data_cipher).decode(")
