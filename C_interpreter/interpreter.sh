echo "This Code is written in shell and act as a C language Interpreter, Purpose behind building this code is to 
help in forming some tasks without writing all the syntax and compulsory statement of code."
echo "code without that typing main and other coumplsury syntexes :) "
echo "This interpreter is included stdio.h library, If you want to add other then you can add them just by typing them
Ex : #include<conio.h>  
And then you can start your program direct from initializing state main function and curly brackets are auto write by the script."
echo "This script will create a temporary file name temprary_file.c in your directory which will auto delete when you type exit."

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
