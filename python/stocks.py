stocksAmount1 = float(input("ENTER AMOUNT OF STOCKS BOUGHT >>>"))
stocksPrice1 = float(input("ENTER PRICE OF STOCKS BOUGHT >>>"))

stocksAmount2 = float(input("ENTER AMOUNT OF STOCKS SOLD >>>"))
stocksPrice2 = float(input("ENTER PRICE OF STOCKS BOUGHT >>>"))

totalBought = stocksAmount1 * stocksPrice1
totalSold = stocksAmount2 * stocksPrice2

totalBought = totalBought + (totalBought * 0.03)
totalSold = totalSold - (totalSold * 0.03)

print(f"Total Amount Bought ${totalBought:.2f}")
print(f"Total Amount Sold  ${totalSold:.2f}")

print(f"Money Gain/Loss ${(totalSold - totalBought):.2f}")
if(totalBought <= totalSold):
    
    print("\nYou Made a Profit :)")
else:
    print("\nYou Made a Loss :(")