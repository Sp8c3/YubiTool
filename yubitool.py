import os
import sys
path = ''

yubikeys = []

ylistStream = os.popen('ykman list')
ylist = ylistStream.read()
while ylist.__contains__('\n'):
    key = ylist[:ylist.find('\n')]
    ylist = ylist[len(key)+1:]
    keySerial = key[len(key)-8:]
    yubikeys.append(keySerial)
os.system('ykman list')
print('')


def exec(args):
    for key in yubikeys:
        print('ykman --device ' + key + ' ' + args)
    print('')
    for key in yubikeys:
        print('ykman --device ' + key + ' ' + args)
        stream = os.popen('ykman --device ' + key + ' ' + args)
        result = stream.read()
        print(result)

if len(sys.argv) <= 1:
    pass

# ykman oath uri
elif((sys.argv[1] == 'oath') and (sys.argv[2] == 'uri')):
    args = 'oath uri "' + sys.argv[3] + '" '
    for x in range(4, len(sys.argv)):
        args += sys.argv[x] + ' '
    exec(args)

# ykam oath list
elif((sys.argv[1] == 'oath') and (sys.argv[2] == 'list')):
    ylistStream = os.popen('ykman list')
    ylist = ylistStream.read()
    summary = ''

    args = 'oath list '
    for x in range(3, len(sys.argv)):
        args += sys.argv[x] + ' '
    
    for key in yubikeys:
        print('ykman --device ' + key + ' ' + args)
    print('')
    for key in yubikeys:
        print('ykman --device ' + key + ' ' + args)
        stream = os.popen('ykman --device ' + key + ' ' + args)
        result = stream.read()
        print(result)

        ylist = ylist[:ylist.find(key)+8] + ' : ' + str(result.count('\n')) + ylist[ylist.find(key)+8:]
        
        
    print(ylist)


else:
    args = ''
    for x in range(1, len(sys.argv)):
        args += sys.argv[x] + ' '
    exec(args)



