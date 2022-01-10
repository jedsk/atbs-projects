### Chapter 10 Project: Selective Copy

import os
from pathlib import Path
import shutil

def selectCopy(folder, newfolder, extension):
    
    p = Path(folder)
    pN = Path(newfolder)
    
    if pN.exists():
        print(f'Copying into exist folder {pN}\n')
    
    if not pN.exists() and not pN.is_file():
        print(f'Creating new folder \'{pN.name}\'\n')
        pN.mkdir()
        
    folder = os.path.abspath(folder)
    totalcount = 0
    
    for foldername, subfolders, filenames in os.walk(folder):
        
        if Path(foldername) == Path(pN):
            continue
        
        print(f'Walking {foldername}...')
        filecount = 0
        
        for filename in filenames:
            existinnew = os.path.join(pN, filename)
            if Path(existinnew).exists():
                print(filename + ' already exists')
                continue

            elif filename.endswith(extension):
                filename = os.path.join(foldername, filename)
                filecount += 1
                shutil.copy(filename, pN)

        totalcount += filecount  
        print(str(filecount) + f' ({extension}) files copied from {foldername}\n')

    print(f'{totalcount} ({extension}) files have been copied to {pN}')


selectCopy('copy from folder','destination folder', 'extension')
