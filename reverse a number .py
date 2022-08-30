number=int(input("please enter any nunber:"))
reverse=0
while(num>0):
    reminder=number%10.
    reverse=(reverse*10)+reminder
    number=number//10.
    print("\n reverse of entered number is=%d"%reverse)
    
