### Chapter 7 Project: Date Detection

#detect and validate dates in DD/MM/YYYY format

import re
dateRegex = re.compile(r'''(
(([0][1-9])|([1-2]\d)|([3][0-1])) #DD 01-31
(/)
([0][1-9]|[1][1-2]) #MM 01-12
(/)
([1-2]\d{3}) #YYYY 1000-2999
)''', re.VERBOSE)

text = '29/02/1924, 31/02/1900, 30/02/2000, 30/04/1800, 31/02/2000, 31/04/2400, 23/02/2000'

matches = []
validDates = []
invalidDates = []

#take found dates, validates, and creates list of validated dates and invalid dates
for groups in dateRegex.findall(text):
    
    #if year divisible by 4 and 400
    leapYear = False
    if int(groups[8]) % 4 == 0:
        if int(groups[8]) % 100 == 0:
            if int(groups[8]) % 400 == 0:
                leapYear = True
        else:
            leapYear = True
            
    if groups[6] == '04' or groups[6] == '06' or groups[6] == '09' or groups[6] == '11':
        if int(groups[1]) > 30:
            invalidDates.append(groups[0])
            continue
            
    if groups[6] == '02':
        if leapYear == False and int(groups[1]) > 28:
            invalidDates.append(groups[0])
            continue
        elif leapYear == True and int(groups[1]) > 29:
            invalidDates.append(groups[0])
            continue      

    validDates.append(groups[0])

if len(validDates) > 0:
    print(validDates)

if len(invalidDates) > 0:
    print(invalidDates)
else:
    print('No matches of dates')
