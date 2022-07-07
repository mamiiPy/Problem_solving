# Max And Min Number

# My List Number
myNumList = []

# Start Counter
num1 = 0
num2 = 0

# Empty List Condition
if len(myNumList) > 0:
    while num2 < len(myNumList) - 1:  # 0 < 5 true
        if myNumList[num1] > myNumList[num1+1]:  # 10 > 12
            myNumList.remove(myNumList[num1+1])
        else:
            myNumList.remove(myNumList[num1])
    num2 += 1
    print(myNumList)
else:
    print('Sorry! your List is Empty')
