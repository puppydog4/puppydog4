num = 0
tot = 0.0
while True:
    sval = input("enter number :")
    if sval == "done":

        break
    try:
        fval = float(sval)
    except:
        print('invalid data')
        continue
   # print(fval)
    num = num +1
    tot = tot + fval

#print("all done")
print(num, tot, tot/num)