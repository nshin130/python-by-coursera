# File !!
# opening: open(filename, mode)
# r: read w: write c:close

# \n : new line
stuff = 'x\ny'
len(stuff) # -> 3

# reading
xfile = open('mbox.txt')
for cheese in xfile:
    print(cheese)
# looping each line

#counting lines in a file
fhand = open('mbox.txt')
count = 0
for line in fhnad:
    count = count + 1
print('Line count: ', count)

#reading whole file
fhand = open('mbox.txt')
inp = fhand.read()
print(len(inp)) #total character in the file

#searching
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.strartswhit('From:'):
        print(line)

#skipping (same result with skipping extra lines)
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if not line.strartswhit('From:'):
        continue
    print(line)

# Files are stored in secondary memory
# If the opne is successful, the os returns us a file handle.
# File handle is not the actual data containe din the file, but instead it is a "handle" that we can use to read the data.
# You are given a handle if the requested file exists and you have th eproper permission to read the file.


