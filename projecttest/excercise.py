thislist = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
x = 0
print("when finished type: done")
while True:
    z = input("please enter a number: ")
    if z == "done":
        exit()
    for i in thislist:

        try:
            x = float(z)
        except Exception:
            print("invalid data. must be a number")
            break
        if i < x:
            print([i for i in thislist if i < x])
            break
