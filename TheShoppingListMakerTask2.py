#Task 2: Include a function to remove items from the list.

#Copying code from TheShoppingListMakerTask1


#Writing code allowing users to add items to a list without printing

#Creating list array for shopping items and printing after user enters 'done'
pocket_burners = []

while True:
    shopping_item = input("Enter a shopping item or type 'done' to finish: ")
    if shopping_item.lower() == 'done':
        break
    else:
        shopitem = (shopping_item)
        pocket_burners.append(shopping_item)

#Creating code to remove items from the list that catches incorrect entries and reruns loop until done break without printing
while True:
    try:
        remove_item = input("Is there an item you would like to remove? Please enter item, if not type 'done' to finish: ")
        if remove_item.lower() == 'done':
            break
        else:
            pocket_burners.remove(remove_item)
    except ValueError:
        print("Apologies, entry must be an item you have entered.")