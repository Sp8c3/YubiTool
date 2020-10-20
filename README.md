# Prerequisites

 - Python3
 - [ykman](https://www.yubico.com/products/services-software/download/yubikey-manager)

# Usage
Just use the same Arguments as in ykman 

    $ python3 ./yubitool.py <args>
For Example:

    $ ykman oath list ->
    
    $ python3 ./yubitool.py oath list   

# extra Features

It can count how many Oath-Entrys you have on all keys, just use

    $ python3 yubitool.py oath list
the script will than display than every single List as normal, and in the End it will print a Summary like:

	$ YubiKey 5 NFC [OTP+FIDO+CCID] Serial: 11111111 : 8
	$ YubiKey 5 NFC [OTP+FIDO+CCID] Serial: 10101010 : 30 
	$ YubiKey 5C NFC [OTP+FIDO+CCID] Serial: 12345678 : 15
