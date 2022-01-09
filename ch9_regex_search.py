### Regex Search

from pathlib import Path
import os, re

p = Path('C:\\Users\\')

txtFiles = list(p.glob('*.txt'))
matchReg = re.compile(r'graphics')

found = []
nomatch = []

for file in txtFiles:
    
    with open(file) as hFile:
        txtfile = hFile.read()
    
    tally = []
    for match in re.findall(matchReg, txtfile):
        tally.append(match)
    
    filename = file.name
    if tally:
        a = f'Matches in \"{filename}\" are {tally}'
        found.append(a)
    else:
        #b = f'There were no matches found in \"{filename}\"'
        nomatch.append(filename)
        

print('\n'.join(found))
print('\nThere were no matches found for: ', *nomatch, sep='\n')
