print(10 * 5)
print(10 ** 2)
print(15 / 10)
print(15 // 10)
print(-15 // 10)
print(15 % 10)
print(10 % 15)
print(10 % 10)
print(0 % 10)
print(10 / 15) #the answer is neverending, but in the program it eventually ends


rate = float(input("Input ER from Euro to USD: "))
#rate variable that asks for an exchange rate
print("The Exchange Rate is ",[rate])
#prints rate variable to user
amount = float(input("How much currency to exchange: "))
#input an amount to convert from user
print("The input is $",[amount])
#print the amount variable for user
total = float(rate * amount)
#creates total variable which is the converstion of the amount inputted and the rate
print("USD Received before fees: ",[total])
#prints the total variable for user
result = float(total - 3)
#creates result variable which subtracts the fee from total variable
print("USD Received after $3 fee: ",[result])
#prints the result variable for the user as a final result of the code
