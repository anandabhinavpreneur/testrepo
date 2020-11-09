#input a number and find the sum of it's digits

n=int(input("Enter a natural number = "))
count=0
for i in range(1,n+1):
    if(n%i==0):
        count=count+1
if (count==2):
    print("The Given Number is a prime number")
else:
    print("The Given Number is not prime number")

        
        
