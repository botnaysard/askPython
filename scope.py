# LESSON

balance = 0

def addAmount(x):
    global balance
    balance = balance + x

while balance < 30:
    addAmount(5)
    print(balance)

# EXERCISE

def reduceBalance(y):
    global balance
    balance = balance - y

if balance >= 30:
    reduceBalance(15)
    print(balance)