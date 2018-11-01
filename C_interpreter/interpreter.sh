echo "This is an Interpreter for C language, Purpose behinde coding this interpreter is that you can simply "
echo "code without that typing main and other coumplsury syntexes :) "
echo "This interpriter is included stdio.h library remaining you can add according to yor code"
echo "This script will create a file name temprary_file.c in your current directery so dont't worry "
echo "It will auto delete when you exit interpriter."
echo "press exit to close interpriter."
while :
do
echo "#include<stdio.h>" > temprary_file.c
x=abc
z=0
y=0
while [ "$x" ];
do

if [ "$x" = "exit" ]; then
    rm temprary_file.c
    exit 0
fi
echo ">>>>" | tr "\n" " "
read x
if [ "`echo $x | head -c 1`" = "#" ]; then
    if [ "$z" = "0" ]; then 
        echo "$x" >> temprary_file.c
        continue
    fi
fi
if [ "$y" = "0" ]; then
    echo "int main()" >> temprary_file.c
    echo "{" >> temprary_file.c
    y=1
fi
echo "$x" >> temprary_file.c
z=1
done
echo "}" >> temprary_file.c
cc temprary_file.c
[ "`echo $?`" = "0" ] && ./a.out
echo
rm temprary_file.c
done
