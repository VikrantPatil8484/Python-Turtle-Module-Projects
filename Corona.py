from turtle import *
color('white')
bgcolor('black')
speed(150)
hideturtle()
b = 0
while b < 200:
 right(b)
 forward(b*1)
 b = b+1




"""print("Welcome! To My Calculator")
while True:
 print()
 print("1.Addition\n 2.Subtraction\n 3.Multiplication\n 4.Division\n 5.Modulus\n 6.FloorDiv\n 7.Exit\n")
 option=int(input("Enter Option To perform :"))
 if option==1:
  Num1 = int(input("Enter value of Num1: "))
  Num2 = int(input("Enter value of Num2: "))
  print(Num1,'+',Num2,'=',Num1+Num2)
  
 elif option==2:
  Num1 = int(input("Enter value of Num1: "))
  Num2 = int(input("Enter value of Num2: "))
  print(Num1,'-',Num2,'=',Num1-Num2)
 
 elif option==3:
  Num1 = int(input("Enter value of Num1: "))
  Num2 = int(input("Enter value of Num2: "))
  print(Num1,'*',Num2,'=',Num1*Num2)
 
 elif option==4:
  Num1 = int(input("Enter value of Num1: "))
  Num2 = int(input("Enter value of Num2: "))
  print(Num1,'/',Num2,'=',Num1/Num2)
 
 elif option==5:
  Num1 = int(input("Enter value of Num1: "))
  Num2 = int(input("Enter value of Num2: "))
  print(Num1,'%',Num2,'=',Num1%Num2)
  
 elif option==6:
  Num1 = int(input("Enter value of Num1: "))
  Num2 = int(input("Enter value of Num2: "))
  print(Num1,'//',Num2,'=',Num1//Num2)
  
 elif option==7:
  print("Thanks For Using Calculator!!")
  break
 
 else:
  print("Operation not available!") """