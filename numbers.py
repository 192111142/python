# sum of natural numbers upto num
num=16
if num<0:
    ("enter the positive number")

else:
    sum=0
    # use while loop to iterate until zero
    while(num>0):
        sum+=num
        num-=1
        print("the sum is", sum)
