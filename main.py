numb1 =input("Enter number1:")
numb2=input("Enter number2:")
operation=input("Enter the number of operation: ")
from  math import *
if numb1.isdigit() & numb2.isdigit():
    print("the operation:"+"\n"+"1_ +"+"\n"+"2_ -"+"\n"+"3_ *"+"\n"+"4_ /"+"\n"+"5_ ^"+"\n"+"6_ %")
    number1=int(numb1)
    number2 = int(numb2)
if  operation == '+' or operation == '1':
       output=print(number1+number2)
elif  operation == '-' or operation == '2':
       output=print(number1-number2)
elif  operation == '*' or operation == '3':
       output=print(number1*number2)
elif  operation == '/' or operation == '4':
       output=print(number1/number2)
elif  operation == '^' or operation == '5':
       output=print(number1^number2)
elif  operation == '%' or operation == '6':
       output=print(number1%number2)

print("exit")

