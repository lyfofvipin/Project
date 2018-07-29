import sys
f = open("File_path/File_name.c","rt")
# you can enter file path with it's name
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
    f.close()
    
'''Example :

we have an example of C code here

https://github.com/vipin3699/Projects/blob/master/indentation/test.c

and we got It's output as shown here

https://github.com/vipin3699/Projects/blob/master/indentation/Output
'''
