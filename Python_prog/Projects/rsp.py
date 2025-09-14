import random
options=("rock","paper","sissor")
s1=0
s2=0
p=0
r=0
s=0
for i in range(100):
 p1=random.choice(options)
 p2=random.choice(options)
 if p1=="sissor" and p2=="rock":
    s1+=1
 if p2=="sissor" and p1=="rock":
    s2+=1
 if p1=="paper" and p2=="rock":
    s1+=1
 if p2=="paper" and p1=="rock":
    s2+=1
 if p1=="sissor" and p2=="rock":
    s2+=1
 if p2=="sissor" and p1=="rock":
    s1+=1
 if p1=="rock" and p2=="rock":
   r+=1
 if p1=="sissor" and p2=="sissor":
   s+=1
 if p1=="paper" and p2=="paper":
   p+=1
print()
print("Result : ",end='')
if s1>s2:
   print("Player 1 Won\n")
elif s1<s2:
   print("Player 2 Won\n")
else:
   print("Draw\n")

print(f"Player 1's Score: {s1}")
print(f"Player 2's Score: {s2}")
print()
print(f"Draws: Rock = {r}, Paper = {p}, Sissor= {s}")

