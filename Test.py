'''*** This is code to demonstrate the Revenue of a business ***'''

Reach = int(input("Enter the Reach of the particular Business: "))
Conversion = float(input("Enter the Conversion percentage of actually people purchasing From the business: "))
AverageSale = int(input("Enter the value of the products sold on daily bases: "))


print("Reach of the particular Business: ", Reach)

print("Conversion rate of actually people purchasing from the Business: ", Conversion)
print("Average sale of products: ", AverageSale)


Revenue = Reach*(Conversion/100) *AverageSale

print("Your Revenue will be: ", Revenue)