# -*- coding=utf-8-*-
from Crypto.Cipher import AES
import base64

"""
aes加密算法
padding : PKCS7
"""

class AESUtil:

    def __init__(self, key, iv=''):
        self.key = key[0:16] #只截取16位
        self.iv = iv # 16位字符，用来填充缺失内容，可固定值也可随机字符串，具体选择看需求。

    def __pad(self, text):
        """填充方式，加密内容必须为16字节的倍数，若不足则使用self.iv进行填充"""
        text_length = len(text)
        amount_to_pad = AES.block_size - (text_length % AES.block_size)
        if amount_to_pad == 0:
            amount_to_pad = AES.block_size
        pad = chr(amount_to_pad)
        return text + pad * amount_to_pad

    def __unpad(self, text):
        pad = ord(text[-1])
        return text[:-pad]

    def cbc_encrypt(self, raw):
        """加密"""
        raw = self.__pad(raw)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv)
        enc_bytes = cipher.encrypt(raw)
        base64_str = base64.b64encode(enc_bytes).decode()
        return base64_str

    def cbc_decrypt(self, enc):
        """解密"""
        enc = base64.b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_CBC, self.iv )
        dec_str = cipher.decrypt(enc).decode("utf-8")
        return self.__unpad(dec_str)

if __name__ == "__main__":
    key = "abcdnnnnnn123456"
    iv = "e4b9ba1c7bf76ceb"
    text = '18728677715'
    aesUtil = AESUtil(key,iv)
    res = aesUtil.cbc_encrypt(text)
    print (res) # b'UNAfBt2366cTkCC9/jgJ9A=='
    res = aesUtil.cbc_decrypt(res)
    print (res) # b'18728677715'