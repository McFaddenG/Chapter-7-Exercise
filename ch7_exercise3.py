fn = input('Enter the file name: ')
if fn == 'na na boo boo':
    print("NA NA BOO BOO TO YOU - You have been punk'd!")
    quit()

try:
    fh = open(fn)
except FileNotFoundError:
    print('File cannot be opened:', fn)
    quit()

count = 0
for line in fh:
    if line.startswith('Subject:'):
        count = count + 1

print('There were', count, 'subject lines in', fn)
