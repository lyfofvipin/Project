import sys
f = open("/home/kumarvipinyadav/Documents/test.c","rt")
flag ,z = 0,""
for x in f.readlines():
    z = '    '*flag
    if '{' in x or flag > 0:
        if '{' in x and not x.startswith('print'): flag += 1
        if '}' in x and not x.startswith('print'):
            flag -= 1
            z = '    '*flag
        if '{' in x and '}' in x and not x.startswith('print'):
            z = z + x[:x.index('{')+1] + '\n' + z + "  " + x[x.index('{')+1:-2] + '\n' + z + '}\n'
            x = ""
    print(z+x)
