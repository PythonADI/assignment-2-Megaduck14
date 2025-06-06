gold = int (input( " How much money you've got ?"))
health_potion_price = 20 
mana_potion_price = 30
sword_price = 75
print ( f" buying \'health potion \' will cost you {health_potion_price} gold ")
print ( f" buying \'mana potion \' will cost you {mana_potion_price} gold " )
print ( f" buying \'sword \' will cost you {sword_price} gold ")
error_message = " you cannot purchase this item , you don't have gold for it "
print( " what you want to buy ?" )
buy_item = input()
if gold == 0:
    print ( " You are beggar , get out of my store thief ")
else: 
    if gold < health_potion_price : 
         print ( error_message )
    else:
        if buy_item == ("health potion") :
           gold -= health_potion_price
           print ( f"You have purchased 'health potion' for {health_potion_price} and you left {gold} gold" )
           
    if gold < mana_potion_price:
        print ( error_message)
    else:
        if buy_item == ("mana potion") :
            gold -= mana_potion_price
            print ( f" You have purchased \' mana potion \' for {mana_potion_price} gold and you left {gold} gold")
    if gold < sword_price:
            print ( error_message)
    else:
        if buy_item == ("sword") :
            gold -= sword_price
            print ( f" You have purchased \'sword\' for {sword_price} gold and you left {gold} gold")
            
    
