file_name = "Test.txt"# input("Enter file name: (Full path) \n")
file = open(file_name,"r")
data = file.readlines()
file.close()
start = 0
stop = 0
startline = int(input("When to start reverting? (Note, the program will copy the lines above but will not try to revert them \n"))
stopline = int(input("When to stop reverting? (Note, the program will copy the lines below but will not try to revert them \n"))
counter = 0
dataWrite = []
def is_ascii(s):
    return all(ord(c) < 128 for c in s)


for stringIn in data:
    counter += 1
    stSpaces = ""
    for i in stringIn:
        if i == " ":
            stSpaces += " "
        else:
            break
    st1 = ""
    stringIn = stringIn.lstrip()
    if counter < startline  or counter > stopline or is_ascii(stringIn):
        dataWrite.append(stringIn)
        continue
    if stringIn == '\n' or stringIn == "":
        dataWrite.append(stringIn)
        continue

    if (stringIn[0] == "<") and (stringIn[1] == "!"):
        dataWrite.append(stringIn)
        continue

    st = ""
    end = len(stringIn)
    start = 0
    stop = 0
    for i in range(0,len(stringIn)):
        if stringIn[i] == ">":
            start = i
        elif stringIn[i] == "<" and i != 0:
            stop = i
            break
    for i in range(start + 1 ,stop):
        st += stringIn[i]
    stMiddle = ""
    stStart = ""
    stEnd = ""
    for i in range(0,start + 1):
        stStart += stringIn[i]
    for i in range(stop,end):
        stEnd += stringIn[i]
    stMiddle =st[::-1]
    st1 = stSpaces + stStart + stMiddle + stEnd
    dataWrite.append(st1)
file = open(file_name,"w")
file.write("")
file.close()
file = open(file_name,"a")
for i in dataWrite:
    file.write(i)