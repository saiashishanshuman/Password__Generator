import random
from datetime import date
today = str(date.today())
w = input("Enter the website")
n = int(input("Enter the number of numeric characters"))
a = int(input("Enter the number of alphabetic characters"))
s = int(input("Enter the number of special chracters"))
alph = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
spec = ["!","@","#","$","%","^","&","*","(",")"]
pw = []

for i in range(0,n):
    n = random.randint(0,9)
    pw.append(str(n))

for i in range(0,a):
    n = random.choice(alph)
    pw.append(n)

for i in range(0,s):
    n = random.choice(spec)
    pw.append(n)

random.shuffle(pw)
pws = "".join(pw)

final = w + " password is " + pws + " on " + today

with open('logs.txt','a') as f:
    f.write(final)
    f.write("\n")

#)$a*b%3(0gm#






