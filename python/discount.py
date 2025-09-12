pkgCost = 99.00

pkgs = int(input("ENTER AMOUNT OF PACKAGES TO PURCHASE >>>"))

dis = 0.0
if(pkgs < 10):
    dis = 0.0
elif(pkgs < 20):
    dis = 0.1
elif(pkgs < 50):
    dis = 0.2
elif(pkgs < 100):
    dis = 0.3
else:
    dis = 0.4

