#Task 1: Write a function that lets the user add items to a list.

#Writing code allowing users to add items to a list without printing

#Creating list array for shopping items
pocket_burners = []

while True:
    shopping_item = input("Enter a shopping item or type 'done' to finish: ")
    if shopping_item.lower() == 'done':
        break
    else:
        shopitem = (shopping_item)
        pocket_burners.append(shopping_item)