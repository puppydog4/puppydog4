fname = input("enter file name: ")
try:
    fhand = open(fname)
except:
    print("file cannot be opened", fname)
    quit()
for line in fhand:
    line = line.rstrip()
    wds = line.split()
    if len(wds) < 1:
        #print("skip blank")
        continue
    if wds[0] != "From":
        continue
    print(wds[2])
