#7.2
# Write a program that prompts for a file name, 
# then opens that file 
# and reads through the file, 
# looking for lines of the form: X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the lines 
# and compute the average of those values 
# and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.

fname = input('Enter file name: ')
fh = open(fname)
c = 0
s = 0

for l in fh:
    if not l.startswith('X-DSPAM-Confidence'):
        continue
    else:
        a = l.find('0')
        x = l[a:]
        x = float(x)
        c = c + 1
        s = s + x

print('Average spam confidence:', s/c)