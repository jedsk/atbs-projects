### Chapter 8 Project: Sandwich Creator

import pyinputplus as pyip
import time

print('Ready to order your sandwich?')

orderList = {}

while True:
    
    nameEntry = pyip.inputStr('\nWho is this sandwich for?')
    nameEntry = nameEntry.title()
    nameFor = {nameEntry:{}}
    print(f'\nHi {nameEntry},')
    
    def selectbread():
        breadType = pyip.inputMenu(['wheat', 'white', 'sourdough'], '\nPlease select your bread of choice: \n')
        nameFor[nameEntry]['Bread']= breadType
    
    def selectprotein():
        proteinType = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='\nOkay, now select your protein of choice: \n')
        nameFor[nameEntry]['Protein'] = proteinType
    
    def selectcheese():
        cheeseType = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella', 'none'], prompt='\nOkay, now select your choice of cheese: \n')
        if cheeseType.lower() != 'none':
            nameFor[nameEntry]['Cheese']  = cheeseType
    
    def selectTops():
        tops = []
        topslist = ['mayo', 'mustard', 'lettuce', 'tomato', 'none']
        
        print()
        while True:
            if tops:
                print('\nYour toppings are: *', ' *'.join(tops)) 
                
            topType = pyip.inputMenu(list(topslist), prompt='Choose your toppings: \n')
            
            if topType.lower() == 'none' or topType.lower() == 'done':
                break
             
            topslist.remove(topType)
            tops.append(topType)
            if 'none' in topslist:
                topslist.remove('none')
            if 'done' not in topslist:
                topslist.append('done')
                
                
        nameFor[nameEntry]['Toppings']  = tops
        
    def selectQuantity():
        quantity = pyip.inputNum(prompt='\nHow many of this sandwich would you like?', min=1)
        nameFor[nameEntry]['Quantity']  = quantity 
    
    def checkOrder():
        print(f'\nPlease review your order for, {nameEntry}')
        #categories = []
        
        for selections in nameFor.values():
            for k, v in selections.items():
                if k == 'Toppings':
                    print(k.ljust(leftWidth, '.') + 'yes'.rjust(rightWidth))     
                if k != 'Toppings':
                    v = str(v)
                    print(k.ljust(leftWidth, '.') + v.rjust(rightWidth))
                    #categories.append(k)

        verifyOrder = pyip.inputYesNo(f'\nIs this correct?')
        if verifyOrder == 'yes':
            orderList.update(nameFor)
            print(f'\nOrder added to cart!')

        elif verifyOrder == 'no':
            editCancel = pyip.inputChoice(['Edit', 'Cancel'], prompt='\nEdit or Cancel this order?\n')

            if editCancel == 'Edit':
                editOrder = pyip.inputMenu(list(categories), prompt='\nWhat would you like to change?\n')
                if editOrder == 'Bread':
                    selectbread()
                if editOrder == 'Protein':
                    selectprotein()
                if editOrder == 'Cheese':
                    selectcheese()
                if editOrder == 'Quantity':
                    selectQuantity()
                checkOrder()

            elif editCancel == 'Cancel':
                nameFor.clear()
                print('Order Cancelled')
                
    leftWidth, rightWidth = 12, 12            
    selectbread()
    selectprotein()
    selectcheese()
    selectTops()
    selectQuantity()
    checkOrder()
              
    addOrder = pyip.inputYesNo(prompt='\nAdd another order?')
    
    if addOrder == 'yes':
              continue 
    else:
        print('\nYour Order: ')
        total = 0
        b = 0
        
        for order in orderList:
            quantity = orderList[order]['Quantity']
            price = '${:,.2f}'.format(float(orderList[order]['Quantity'] * 5))
            total += float(orderList[order]['Quantity'] * 5)
    
            a = (order.ljust(leftWidth, '.'), 'x',str(quantity), price.rjust(rightWidth))
            print(''.join(a))
            b = len(''.join(a))
            
        totalmemo = 'Total: '+'${:,.2f}'.format(total)
        print(totalmemo.rjust(b))
        print('\nThank you!')
        break
