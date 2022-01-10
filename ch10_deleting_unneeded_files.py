### Chapter 10 Project: Deleting Unneeded Files

# Searches directory, for files over the limit size in argument
# Sort from largest to smallest while displaying their name, destination, and size

import os, sys
from pathlib import Path

def searchLgFiles(folder, sizelimitMB):
    p = Path(folder)
    fileList = {}
    sizelimit = (sizelimitMB * 1000000)
    
    print(f'Searching for files above {sizelimitMB} MB in {folder}...\n')
    
    for foldername, subfolders, filenames in os.walk(folder):
        
        for filename in filenames:
            sizeFilename = os.path.join(foldername, filename)
            absFilename = os.path.abspath(sizeFilename)
            
            if os.path.getsize(sizeFilename) > sizelimit:
                MBformat = (os.path.getsize(sizeFilename)/1000000)
                fileList[filename]= [absFilename, MBformat]
          
            else:
                continue
                
    sortedlist = dict(sorted(fileList.items(), key=lambda item: item[1][1], reverse=True))

    for k, v in sortedlist.items():
        w = ('{:,.2f}'.format(v[1]) + ' MB')
        vparent = Path(v[0])
        print(k[:40].ljust(40) + ' size: '.rjust(15) + w.rjust(10))
        print(vparent.parent,'\n')
        
    print('\nDone searching')

searchLgFiles('absolute path directory to search', 100)
