import random 
from os import system
while True :
 system('cls')
 y=random.randint(1, 100)
 print('you have 7 try to guess the number')
 print("__________________________________")
 print("the number is an integer  between [1,100]")
 print("_____________good luck______________")
 i=1
 while i<=7:
    print('your ',i,'try')
    print("________________________________")
    x=input('input you imagine number is: ')
    x=int(x)
    if x==y:
        print('Congraiglitions YOU WIN!!!!')
        z=input("press any key to play again // or //press 0 to end")
        if z=='0':
         exit(0)
        break
    elif x>y:
        print("the aim number is (smaller) than your input number")
        print("__________________________________________________")
    elif x<y:
        print("the aim number is (bigger) than your input number")
        print("__________________________________________________")
    i=i+1
 if i>7:
  print("SORRY YOU LOST ")
  print("GAME OVER\n") 
  print("the number was : \n",y)
  z=input("press any key to play again // or //press 0 to end")
  if z=='0':
    exit(0)
 else:
     continue