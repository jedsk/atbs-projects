### Project: Filling in the Gaps

# this program finds all files with a given prefix 
# ex. spam001.txt, spam002.txt, locates any gaps in the numbering
# and renames all the later files to close this gap

import re, os, shutil
from pathlib import Path

prefixRegex = re.compile(r'(^spam)(0*)(\d+)(.[a-zA-Z]+)*')

def renameFiles(folder, prefixRegex): 
    
    folder = Path(folder)
    matchedlist = []
    extension = ''
    appendfile = []
    
    print('Renaming files into correct format...\n')
    for match in os.listdir(folder):
                            
        mo = prefixRegex.search(match)
        if mo == None:
            continue
            
        if not extension:
            extension = mo.group(4)
            
        numstr = (''.join(mo.group(2,3)))
        
        #if number format has less or more than 3 digits
        while len(numstr) > 3:
            numstr = numstr[1:]
        while len(numstr) < 3:
            numstr = '0' + numstr
        
        #renaming file names then into absolute path
        if mo.group(4) == None:
            newName = mo.group(1) + numstr + extension
        else:
            newName = mo.group(1) + numstr + mo.group(4)
        oldnamePath = Path(folder, match)
        newnamePath = Path(folder, newName)
        
        if oldnamePath != newnamePath:
            if newName in os.listdir(folder):
                print(f'{match} not renamed')
                appendfile.append(match)
                continue
                
            shutil.move(oldnamePath, newnamePath)
            
        matchedlist.append(newnamePath.name)

        
    print('\nOrdering files in numerical order...\n')
    firstcount = int()
    count = int()
    
    for match in sorted(matchedlist):
        mo = prefixRegex.search(match)
        
        if count == 0:
            count += int(mo.group(3))
            firstcount += int(mo.group(3))
            print(f'Renaming files starting at {match}')
            continue
            
        count += 1
        if int(mo.group(3)) != count:
                  
            numstr = (''.join(mo.group(2) + str(count)))

            while len(numstr) < 3:
                numstr = '0' + numstr
            
            newfilename = mo.group(1) + numstr + mo.group(4)
            print(f'Renaming {match} to {newfilename}')
            
            oldnamePath = Path(folder, match)
            newnamePath = Path(folder, newfilename)
            shutil.move(oldnamePath, newnamePath)
            
    print('\nRenaming files complete.')
 
renameFiles('C:\\Users\\csakp\\JupyterFiles', prefixRegex)
