# a function to determine if the number is prime or not
def number(num):
    if num<1:
        print("prime : no")
    for i in range(2,num):
      if num%i==0:
        
        print ("prime : no")
        return
    else:
       print("prime : yes")
# a function to determine if the number is even or odd
def even_odd(num):
    if num%2==0:
        print("Taype : even")
    else:
        print("Type : odd")
# a function to calculate the square of the number
def squar_number(num):
 result=num*num
 print("Squar root : ",result)
while True:
 print("Enter Number for Star or enter 'stop' to exit")
 num=input("Enter your number :")
 if num=='stop':
  print("Good bye")
  break
 else:
        number(int(num))
        even_odd(int(num))
        squar_number(int(num))

