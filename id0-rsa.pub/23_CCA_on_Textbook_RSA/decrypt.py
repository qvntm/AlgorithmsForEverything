#!/usr/bin/env python3
from Crypto.PublicKey import RSA
import requests

target_ct = 0x912fcd40a901aa4b7b60ec37ce6231bb87783b0bf36f824e51fe77e9580ce1adb5cf894410ff87684969795525a63e069ee962182f3ff876904193e5eb2f34b20cfa37ec7ae0e9391bec3e5aa657246bd80276c373798885e5a986649d27b9e04f1adf8e6218f3c805c341cb38092ab771677221f40b72b19c75ad312b6b95eafe2b2a30efe49eb0a5b19a75d0b31849535b717c41748a6edd921142cfa7efe692c9a776bb4ece811afbd5a1bbd82251b76e76088d91ed78bf328c6b608bbfd8cf1bdf388d4dfa4d4e034a54677a16e16521f7d0213a3500e91d6ad4ac294c7a01995e1128a5ac68bfc26304e13c60a6622c1bb6b54b57c8dcfa7651b81576fc

with open("pub_key.pem") as f:
    key = RSA.import_key(f.read())
    N = key.n
    e = key.e

    test_ct = pow(2, e, N) * target_ct % N
    url = "https://id0-rsa.pub/problem/rsa_oracle/" + hex(test_ct)[2:]
    r = requests.get(url = url)

    # since textbook RSA is homomorphic, return value is 2*plaintext
    retval = int(r.text, 16)
    assert(retval % 2 == 0)
    print("Answer is", hex(retval // 2)[2:])

