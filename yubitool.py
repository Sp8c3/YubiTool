import os
import sys
path = ""

yubikeys = []

# Interactive: python3 -i yubitool.py

ylistStream = os.popen("ykman list")
ylist = ylistStream.read()
while ylist.__contains__("\n"):
    key = ylist[:ylist.find("\n")]
    ylist = ylist[len(key)+1:]
    keySerial = key[len(key)-8:]
    yubikeys.append(keySerial)
print(yubikeys)
print("")


def exec(string):
    for key in yubikeys:
        print("ykman --device " + key + " " + string)
        stream = os.popen("ykman --device " + key + " " + string)
        result = stream.read()
        print(result)

if len(sys.argv) <= 1:
    pass

else:
    args = ""
    for x in range(1, len(sys.argv)):
        args += sys.argv[x] + " "
    exec(args)
