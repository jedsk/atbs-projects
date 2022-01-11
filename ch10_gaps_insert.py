### Project: Insert gaps into numbered files

# this program insert gaps into numbered giles so that a new file can be added.
# (assuming files are already ordered by "Filling in the Gaps" program)
# ex. gapping #3, in spam002.txt, spam003.txt. spam004.txt
# becomes spam002.txt, spam004.txt. spam005.txt


import re, os, shutil
from pathlib import Path

prefixRegex = re.compile(r'(^spam)(0*)(\d+)(.[a-zA-Z]+)*')

def skipFiles(folder, filetoSkip): 
    
    print('Creating gap at postion: ' + str(filetoSkip) ,'\n')
    
    folder = Path(folder)
    matchedlist = []
    
    for match in os.listdir(folder):
        mo = prefixRegex.search(match)
        if mo == None:
            continue
            
        newnamePath = Path(folder, match)
        matchedlist.append(newnamePath.name)
    
    firstcount = int()
    count = int()
    filetoSkip = filetoSkip - 1
    
    for match in sorted(matchedlist, reverse = True):
        mo = prefixRegex.search(match)
        
        if int(mo.group(3)) == filetoSkip:
            break
        
        count = int(mo.group(3)) + 1
        numstr = (''.join(mo.group(2) + str(count)))
        
        while len(numstr) > 3:
            numstr = numstr[1:]
        
        newfilename = mo.group(1) + numstr + mo.group(4)
        print('Renaming ' + match + ' to '+ newfilename)
        
        oldnamePath = Path(folder, match)
        newnamePath = Path(folder, newfilename)
        shutil.move(oldnamePath, newnamePath)

    print('\nGap creation complete.')
    
    
skipFiles('insert directory here', int(gap desired))
