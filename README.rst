PyNaCl SealedBox encrypt/decrypt demo
==================================================
* Create environment and install packages.

.. code::

    $ python3.7 -m venv /tmp/pynacl-demo && source /tmp/pynacl-demo/bin/activate
    $ git clone git@gitlab.com:mtoshi/pynacl-demo.git
    $ cd pynacl-demo
    $ pip install setuptools --upgrade && pip install pip --upgrade
    $ pip install -r requirements.txt

* Run sample code.

.. code::

    $ python sealedbox_sample.py 

    ----------------------------------------------------------------------------------------------------
    KEY and MESSAGE
    ----------------------------------------------------------------------------------------------------
    PRIKEY: b'\xd7\x93j\xdc\x1e:\xe5i\xad\xab\t\xeb\x95<\xb7\xce\x03\xab/\x08]\xd9\x9f\xcf\xea\xa2\xbaC\xeb\x7f\x8c.'
    PRIKEY(BASE64): 15Nq3B465WmtqwnrlTy3zgOrLwhd2Z/P6qK6Q+t/jC4=
    PUBKEY: b'\xa2%\x0c\x879\xba\x0fL\x958Qdk\x1e\xdbO*\x80\xe5T}\x8d\x10S\xa3\xc4\xa4\xea\xf7\xd7Pu'
    PUBKEY(BASE64): oiUMhzm6D0yVOFFkax7bTyqA5VR9jRBTo8Sk6vfXUHU=
    MESSAGE: abcdefg1234
    ----------------------------------------------------------------------------------------------------
    ENCRYPT with public key
    ----------------------------------------------------------------------------------------------------
    ENCRYPTED MESSAGE: b'\xf4\xca\x7f\xe5k\x82\xee\x8e\x8aw3\xe4\x9eA\xb4\xa13\xedW\xb7\xe9&\xb9\xbb\x7fp\xae\xb2\x9f&\n\x00%\xae\xaaMVj\x86\xc7"\xec\x8dN\x18\xe4/\xc2M\xd6R\xb0g/\x05C\x90\x8aB'
    ENCRYPTED MESSAGE(BASE64): 9Mp/5WuC7o6KdzPknkG0oTPtV7fpJrm7f3Cusp8mCgAlrqpNVmqGxyLsjU4Y5C/CTdZSsGcvBUOQikI=
    ----------------------------------------------------------------------------------------------------
    DECRYPT with private key
    ----------------------------------------------------------------------------------------------------
    DECRYPTED MESSAGE: abcdefg1234


* Sample code.

.. code:: python

    from nacl.public import PrivateKey
    from nacl.public import SealedBox
    from nacl.encoding import Base64Encoder


    prikey = PrivateKey.generate()
    pubkey = prikey.public_key

    message = 'abcdefg1234'
    encoding = 'utf-8'

    box = SealedBox(pubkey)
    encrypted = box.encrypt(message.encode(encoding=encoding))
    print(encrypted)

    box = SealedBox(prikey)
    decrypted = box.decrypt(encrypted).decode(encoding=encoding)
    print(decrypted)

