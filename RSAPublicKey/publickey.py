from Crypto.PublicKey import RSA
import binascii

n = '9585A4773ABEECB949701D49762F2DFAB9599BA19DFE1E1A2FA200E32E0444F426DA528912D9EA8669515F6F1014C454E1343B97ABF7C10FE49D520A6999C66B230E0730C3F802D136A892501FF2B13D699B5C7ECBBFEF428AC36D3D83A5BD627F18746A7FDC774C12A38DE2760A3B95C653C10D7EB7F84722976251F649556B'
# publicExponent="10001"
# -----BEGIN PUBLIC KEY-----
# MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCVhaR3Or7suUlwHUl2Ly36uVmb
# oZ3+HhovogDjLgRE9CbaUokS2eqGaVFfbxAUxFThNDuXq/fBD+SdUgppmcZrIw4H
# MMP4AtE2qJJQH/KxPWmbXH7Lv+9CisNtPYOlvWJ/GHRqf9x3TBKjjeJ2CjuVxlPB
# DX63+Ecil2JR9klVawIDAQAB
# -----END PUBLIC KEY-----


key = RSA.construct((int(n,16),int('10001',16)))  
public_key = key.publickey().exportKey() 
print(public_key.decode())


# ----- python2效果更好  ----
# n2 = (binascii.b2a_hex(n)).upper()
# print(n2)

# key = RSA.construct((long(n,16),long('10001',16)))  
# public_key = key.publickey().exportKey() 
# print(public_key)  
# ----- python2效果更好  ----


