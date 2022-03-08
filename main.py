import linuxdic
import macdic
import windowsdic
# all binary dictionary information split up among respective operating systems -- main.py will strictly be the logic




operatingSystem = input("Enter the operating system:    1 for Linux    2 for Mac/BSD    3 for Windows")
fullCmdLine = input("Enter a command line to learn more about it!")
cmdLineTerms = fullCmdLine.split()              # split cmdline given along whitespace -- into list of terms
output = ""                                     # will append to output as we obtain useful info


if operatingSystem == "1":                      # initializing some much needed variables
    operatingSystem = "LINUX"
    thisDictionary = linuxdic
    thisIndex = linuxdic.linuxIndex
elif operatingSystem == "2":
    operatingSystem = "MAC/BSD"
    thisDictionary = macdic
    thisIndex = macdic.macIndex
elif operatingSystem == "3":
    operatingSystem = "WINDOWS"
    thisDictionary = windowsdic
    thisIndex = windowsdic.windowsIndex


currentCommand = ""
previousCommand = ""                    #?potentially useless variable
for term in cmdLineTerms:
    if term in thisIndex:
        currentCommand = term           #?does viewMan already accomplish the task of bookmarking the dictionary in use till args are looked up?
        viewMan = thisIndex[term]       # set viewMan to its corresponding entry in the <os>index dictionary
        output += term + "\t:\t" + viewMan["description"]    # output "description" dictionary entry for <term> (in <term>'s dictionary)
    elif currentCommand != "" :         # if we have already analysed a recognized command
        try:
            output += "\t" + term + "\t:\t" + viewMan[term]         # try to output dictionary entry for <term> in the dictionary for <currentCommand>
        except:
            output += "#####\t{undefined_term}\t<NOT FOUND IN DICTIONARY>".format(undefined_term=term)
        #if term in operatorList:
            # currentCommand = ""


print(output)                                   # finally, print all the output to the screen