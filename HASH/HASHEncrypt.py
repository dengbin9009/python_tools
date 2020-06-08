# -*- coding: UTF-8 -*-

import hashlib
import base64

class HashUtil(object):

    # 初始化key
    def __init__(self):
        pass

    def md5_encrypt(self, message):
        message = message.encode(encoding='UTF-8')
        my_md5 = hashlib.md5()#获取一个MD5的加密算法对象
        my_md5.update(message) #得到MD5消息摘要
        my_md5_Digest = my_md5.hexdigest()#以16进制返回消息摘要，32位
        return my_md5_Digest

    def sha1_encrypt(self, message):
        message = message.encode(encoding='UTF-8')
        my_sha1 = hashlib.sha1()#获取一个MD5的加密算法对象
        my_sha1.update(message) #得到MD5消息摘要
        my_sha1_Digest = my_sha1.hexdigest()#以16进制返回消息摘要，32位
        return my_sha1_Digest

    def base64_encrypt(self, message):
        message = message.encode(encoding='UTF-8')
        my_base64 = str(base64.b64encode(message), 'UTF-8')
        return my_base64

    def base64_decrypt(self, message):
        message = message.encode(encoding='UTF-8')
        my_base64 = str(base64.b64decode(message), 'UTF-8')
        return my_base64

def testAll():
    data = "hellworldhellworldhellworldhell"
    data = data.encode(encoding='UTF-8')

    md5 = hashlib.new('md5', data).hexdigest()
    print(md5)

    md5 = hashlib.md5(data).hexdigest()
    print(md5)

    sha1 = hashlib.sha1(data).hexdigest()
    print(sha1)

    bs = str(base64.b64encode(data), 'UTF-8')
    print(bs)

if __name__ == "__main__":
    print("__main__")
    message = 'hellworldhellworldhellworldhell'
    print("明文内容：>>> ")
    print(message)
    hashUtil = HashUtil()
    encrypy_result = hashUtil.md5_encrypt(message)
    print("md5加密结果：>>> ")
    print(encrypy_result)
    encrypy_result = hashUtil.sha1_encrypt(message)
    print("sha1加密结果：>>> ")
    print(encrypy_result)
    encrypy_result = hashUtil.base64_encrypt(message)
    print("base64加密结果：>>> ")
    print(encrypy_result)
    encrypy_result = hashUtil.base64_decrypt(encrypy_result)
    print("base64解密结果：>>> ")
    print(encrypy_result)

    # testAll()

