# by Kami Bigdely
# Remove control flag
def find_food(food, fridge):
    for item in fridge:
        if item == food in fridge:
            item_name = food
            print("Found: " + item_name)
            break
        else:
            print("item not here")
            

if __name__ == "__main__":
    food = 'wesabi'
    food_list = ['onion', 'cucumber','Guacamole', 'kabob barg', 'wesabi']
    find_food(food, food_list)