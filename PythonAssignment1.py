
"""A cinema charges ticket prices based on age:
  - Below 5 years   : Free
  - 5 to 17 years   : Rs. 100
  - 18 to 59 years  : Rs. 200
  - 60 and above    : Rs. 120

Ask the customer for their age and print the ticket price.

Sample run:
  Enter your age: 65
  Your ticket price is Rs. 120

"""

J=int(input('Enter your age: '))
if J < 5:
  print('The ticket is Free')
elif J < 17:
  print('Ticket price is 100')
elif J < 59:
  print('Ticket price is 200')
else:
  print('Ticket price is 120')

"""Q2. Electricity Bill Calculator
--------------------------------------------------------------
The electricity board charges as follows:
 - First 100 units       : Rs. 3 per unit
 - Next 100 units (101-200): Rs. 5 per unit
 - Above 200 units       : Rs. 8 per unit

Take the number of units consumed and print the total bill.

Sample run:
 Enter units consumed: 250
 Total bill: Rs. 1200
 (100*3 + 100*5 + 50*8 = 300 + 500 + 400)
"""
u=int(input('Please enter the units consumed:'))
if u<=100:
  bill=u*3
elif u<=200:
  bill=100*3+(u-100)*5
else:
  bill=100*3+100*5+(u-200)*8
print('Total bill :' ,bill)
"""
Q3. Multiplication Table for a Kid
--------------------------------------------------------------
A little kid wants to learn tables. Ask for a number and print
its multiplication table from 1 to 10 using a for loop.

Sample run:
  Enter a number: 7
  7 x 1 = 7
  7 x 2 = 14
  ...
  7 x 10 = 70
"""

MultiplicationTable= int(input('Enter the MultiplicationTable Number: '))
for i in range(1, 11):
  print(MultiplicationTable, 'x', i, '=', i*MultiplicationTable)
"""
Q4. Savings Piggy Bank
--------------------------------------------------------------
Riya puts money into her piggy bank every day. Her goal is
Rs. 1000. Using a while loop, keep asking how much she saved
today and add it to the total. Stop when the total reaches or
crosses Rs. 1000, then print how many days it took.

Sample run:
  Enter today's savings: 300
  Enter today's savings: 450
  Enter today's savings: 400
  Goal reached in 3 days! Total saved: Rs. 1150
  """
total=0
days=0
goal=1000
while total<goal:
    savings=int(input("Enter today savings:"))
    total+=savings
    days+=1
print("You reached your goal!")
print("Days taken to reach goal!:", days)
print("Total amount saved:", total)

"""
An ATM's correct PIN is 4321. The user gets only 3 attempts.
  - If the PIN is correct, print "Access granted".
  - If wrong, print "Wrong PIN" and ask again.
  - After 3 wrong attempts, print "Card blocked".

Sample run:
  Enter PIN: 1111
  Wrong PIN
  Enter PIN: 4321
  Access granted

"""
correct_PIN=4321
a=0

while a<3:
    pin=int(input("Enter PIN:"))
    if pin==correct_PIN:
        print("Access granted")
        break
    else:
        print("Wrong PIN")
        a+=1
if a==3:
    print("Card blocked")
"""
Q6. Even and Odd Counter
--------------------------------------------------------------
A teacher wants to know how many roll numbers from 1 to N are
even and how many are odd. Ask for N and use a for loop to
count them.

Sample run:
  Enter N: 15
  Even numbers: 7
  Odd numbers: 8
"""
N=int(input('enter N:'))
even=0
odd=0
i=1
while(i<N+1):
  if i%2 == 0:
    even+=1
  else:
    odd+=1
  i=i+1
print('Even numbers:',even)
print('Odd Numbers:',odd)

"""
Q7. Number Guessing Game
--------------------------------------------------------------
The secret number is 27 (store it in a variable). Keep asking
the player to guess until they get it right. After each wrong
guess, tell them "Too high" or "Too low". At the end, print
how many guesses they took.

Sample run:
  Guess the number: 50
  Too high
  Guess the number: 20
  Too low
  Guess the number: 27
  Correct! You took 3 guesses.
  """
Secret_number=27
i=0;
while(True):
   number=int(input("Enter the random number:"))
   i+=1
   print("Guess number:", i)
   if number>Secret_number:
     print('Too High')
   elif number<Secret_number:
     print('Too Low')
   else:
     print('Correct! You took', i,'guesses')
     break
"""
Q8. Exam Result with Grade
--------------------------------------------------------------
Take marks (out of 100) of a student and print the grade:
  - 90 and above : A
  - 75 to 89     : B
  - 50 to 74     : C
  - 35 to 49     : D
  - Below 35     : Fail
If the marks entered are less than 0 or more than 100, print
"Invalid marks".
"""
M=int(input("Enter Marks: "))
if M>100 or M<0:
  print('Invalid marks')
elif M>=90 and M<=100:
   print('Grade:A')
elif M>=75 and M<=89:
   print('Grade:B')
elif M>=50 and M<=74:
   print('Grade:c')
elif M>=35 and M<=49:
   print('Grade:D')
else:
   print('Fail')

"""
Q9. Sum of Digits on a Bill Number
--------------------------------------------------------------
A shop gives a free gift if the sum of the digits of the bill
number is more than 20. Take the bill number (as an integer)
and use a while loop with % and // to find the sum of its
digits. Print whether the customer gets a gift.

Sample run:
  Enter bill number: 98765
  Sum of digits: 35
  Congratulations! You win a free gift.

"""
N=int(input("Enter Number"))
T=0
while N>0:
     T=T+N%10
     N=N//10
print("Sum of digits: ",T)
if T>20:
     print("Congratulations! You win a free gift.")
"""
Q10. Staircase Pattern
--------------------------------------------------------------
A game developer needs a simple staircase made of '*'.
Ask for the number of steps and print the pattern using
nested for loops.

Sample run:
  Enter number of steps: 4
  *
  * *
  * * *
  * * * *
"""
s=int(input("Enter No of steps:"))
for i in range(1,s+1):
    for j in range(1,i+1):
        print("*",end=" ") 
    print()
