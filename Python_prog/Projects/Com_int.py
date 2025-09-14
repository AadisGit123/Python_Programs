principle = 0
time = 0
rate = 0

while principle <=0 :
  principle=int(input("Enter the Principle amount: "))
  if principle<=0:
    print("Invalid principle amount !")

while rate <=0 :
  rate=int(input("Enter the  Interest Rate: "))
  if rate<=0:
    print("Invalid interest rate !")

while time <=0 :
  time=int(input("Enter the  time: "))
  if time<=0:
    print("Invalid time !")

total = principle*pow((1 + rate / 100 ),time)

print(f'Balance after {time} year/s = £{total:.2f}')