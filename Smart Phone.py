''' Question ref.
https://www.iarcs.org.in/inoi/2014/zco2014/zco2014-2a.php '''
n=int(input()) #the total number of potential customers
customer=[]
result=[]
for _ in range (n): 
    i=int(input())
    customer.append(i)
customer.sort() #sorting all the budgets from min to max 
for i in range(n):
    result.append(customer[i]*(n-i))
print(max(result))
    
