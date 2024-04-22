#Splitting lines in a text into separate text files with single lines

#Definition to split lines from a file
def readLineByLine(filename):
    with open(filename, 'r',encoding="utf8") as f: #Use with statement to correctly close the file when you read all the lines.
        for line in f:    # Use implicit iterator over filehandler to minimize memory used
            yield line.strip('\n') #Use generator, to minimize memory used, removing trailing carriage return as it is not part of the command.
            
Sv = 1         #Counter Flag For English
En = 1         #Counter Flag For Swedish
countE = 1     #Numbering Counter English
countS = 1     #Numbering Counter Swedish
Lines = 5      #Total Number of Lines/text files required

EngSrc = "Eng.txt"      #Source Path For English Corpus
SweSrc = "Sv.txt"       #Source Path for Swedish Corpus
EngTar = "En"           #Target Path for English text file
SweTar = "Sv"           #Target Path for Swedish text file

flag = []
prev = ' '


#Loop to iterate the readLineByLine function for English Corpus
for line in readLineByLine(EngSrc):
    if(Sv<Lines):
        if(prev == line):
            flag.append(d)
            Sv = Sv+1
            continue
        else:
            prev = line
            with open(EngTar+str(countE)+".txt", "w",encoding="utf8") as txt_file:
                txt_file.write("{} ".format(line.strip()))
            countE = countE + 1
    Sv = Sv+1

    
#Loop to iterate the readLineByLine function for Swedish Corpus
for line in readLineByLine(SweSrc):
    if(En<Lines):
        e=0
        if e in flag:
            En = En+1
            continue
        else:
            with open(SweTar+str(countS)+".txt", "w",encoding="utf8") as txt_file:
                txt_file.write("{} ".format(line.strip()))
            countS = countS + 1
    En = En+1