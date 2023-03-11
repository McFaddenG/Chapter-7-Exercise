fn = input("Enter file name: ")
fh = open(fn)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
        count = count + 1
        num = float(line[line.find(':')+1:])
        total = total + num
if count > 0:
    avg = total / count
    print("Average spam confidence:", avg)
else:
    print("No lines found")
