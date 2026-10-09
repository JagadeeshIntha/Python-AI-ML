"""
Q1. Class Marks Report
--------------------------------------------------------------
A teacher has the marks of 8 students stored in a list:
  marks = [78, 45, 92, 33, 67, 88, 51, 29]

Write a program to print:
  - The highest and lowest marks
  - The class average
  - How many students passed (pass mark is 35)
  """
m=[78,45,92,33,67,88,51,29]
print("Highest marks:",max(m))
print("Lowest marks:",min(m))
average=sum(m)/len(m)
print("Class average:",average)
p=0
for i in m:
    if i>=35:
        p+=1
print("Students passed:",p)
"""
Q2. Grocery Shopping List
--------------------------------------------------------------
Start with an empty shopping list. Keep asking the user to
enter an item name. When the user types "done", stop and
print:
  - The full shopping list, one item per line with a number
  - The total number of items

If the user enters an item that is already in the list, print
"Already added" and do not add it again.

Sample run:
  Enter item: milk
  Enter item: bread
  Enter item: milk
  Already added
  Enter item: done
  1. milk
  2. bread
  Total items: 2
"""
shoplist=[]
while True:
    item=input("Enter item:")
    if item=="done":
        break
    if item in shoplist:
        print("Already added")
    else:
        shoplist.append(item)
for i in range(len(shoplist)):
    print(i+1,".",shoplist[i])
print("Total items:",len(shoplist))

"""
Q3. Username Validator
--------------------------------------------------------------
A website has these rules for usernames:
  - Length must be between 5 and 12 characters
  - It must not contain any spaces
  - It must not start with a digit

Take a username as input and print "Valid username" or the
reason it is invalid.

Sample run:
  Enter username: 7rahul
  Invalid: Username cannot start with a digit
"""
name=input("Enter username: ")
if len(name)<5 or len(name)>12:
    print("Length must be between 5 and 12 characters")

elif " " in name:
    print("It must not contain any spaces")
elif name[0].isdigit():
    print("Username cannot start with a digit")
else:
    print(name)
"""
Q4. Vowel Counter for a Tweet
--------------------------------------------------------------
A social media app wants to analyse a tweet. Take a sentence
as input and count:
  - Number of vowels
  - Number of consonants
  - Number of spaces

(Ignore digits and special characters for vowel/consonant count.)

"""
s=input("Enter the sentence")
v=0
c=0
space=0
for i in s:
    if i.lower() in "aeiou":
        v+=1
    elif i.isalpha():
        c+=1
    elif i== " ":
        space+=1
print("Vowels:",v)
print("Consonants:",c)
print("Spaces:",space)

"""
Q5. Palindrome Name Checker
--------------------------------------------------------------
A game gives bonus points if the player's name reads the same
forwards and backwards (like "Anna" or "Madam").
Take a name as input and check if it is a palindrome.
The check should NOT depend on uppercase/lowercase.

Sample run:
  Enter your name: Anna
  Bonus! Your name is a palindrome.
  """
name=input("Enter name:")
name=name.lower()
if name==name[::-1]:      #name[start:stop:step]
    print("Palindrome")
else:
    print("Not palindrome")
"""
Temperatures recorded in Hyderabad for a week are:
  temps = [32, 35, 38, 41, 36, 29, 40]
  days  = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

Write a program to:
  - Print the days on which temperature was above 37 (heat alert)
  - Print the hottest day and its temperature
  - Create a new list with temperatures converted to Fahrenheit
    (F = C * 9/5 + 32) and print it
"""
T=[32,35,38,41,36,29,40]
days=["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
for i in range(len(T)):
    if T[i]>37:
        print("Heat alert:",days[i])
hot=max(T)
p=T.index(hot)
print("Hottest day:",days[p])
print("Hottest temperature:",hot)
fahrenheit=[]
for i in T:
    f=i*9/5+32
    fahrenheit.append(f)
print("Fahrenheit:",fahrenheit)
"""
Q7. Word Frequency in a Sentence
--------------------------------------------------------------
Take a sentence from the user. Split it into words and print
the longest word and the shortest word. Also print how many
words start with a capital letter.

Sample run:
  Enter a sentence: I love learning Python in Hyderabad
  Longest word: Hyderabad
  Shortest word: I
  Words starting with capital letter: 3
  """
sentence = input("Enter a sentence: ")
sw= sentence.split()
longest_word = sw[0]
shortest_word = sw[0]
capital=0
for i in sw:
    if len(i)>len(longest_word):
        longest_word=i
    if len(i)<len(shortest_word):
        shortest_word=i
    if i[0].isupper():
        capital+=1
print("Longest word:",longest_word)
print("Shortest word:",shortest_word)
print("Words starting with capital letter:",capital)
"""
Q8. Remove Negative Balances
--------------------------------------------------------------
A bank has a list of account balances:
  balances = [1500, -200, 3000, -50, 0, 750, -1000]

Create two new lists using a loop:
  - positive_accounts : balances greater than 0
  - negative_accounts : balances less than 0
Print both lists and the total amount owed by negative accounts.

"""
balances = [1500, -200, 3000, -50, 0, 750, -1000]
PC=[]
pcount=0
NC=[]
ncount=0
for i in balances:
    if i>0:
       PC.append(i)
       pcount+=i
    else:
        NC.append(i)
        ncount+=i
print("Positive list:",PC)
print("Negative list:",NC)
print("the total amount owed by negative accounts:",ncount)        
"""
Q9. Password Strength Checker
--------------------------------------------------------------
Take a password as input. Loop through each character and
check whether it has:
  - At least one uppercase letter
  - At least one lowercase letter
  - At least one digit
  - At least 8 characters

Print "Strong" if all conditions are met, "Medium" if 2 or 3
are met, and "Weak" otherwise.

Hint: use isupper(), islower(), isdigit()
"""
password=input("Enter the Password: ")
u=any(i.isupper() for i in password)
l=any(i.islower() for i in password)
d=any(i.isdigit() for i in password)
length=len(password)>=8
count=u+l+d+length
if count==4:
    print("Strong")
elif count>=2:
    print("Medium")
else:
    print("Weak")
"""
Q10. Simple Name Initials Generator
--------------------------------------------------------------
An office ID card system needs initials. Take a full name
(e.g., "ruchik kumar sharma") and print:
  - The initials in uppercase with dots  -> R.K.S.
  - The name in title case               -> Ruchik Kumar Sharma
  - The name with only the surname in full -> R. K. Sharma
"""