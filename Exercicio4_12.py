my_foods = ["pizza", "falafel", "carrot cake"]
friend_foods = my_foods[:]
print("\nMy favorite foods are:")
for food in my_foods:
    print(food.title())
print("\nMy friend´s favorite foods are:") 
for food in friend_foods:
    print(food.title())
my_foods.append("cannoli")
friend_foods.append("ice cream")
print("\nMy new favorite foods are:")
for food in my_foods:
    print(food.title())
print("\nMy friend´s new favorite foods are:") 
for food in friend_foods:
    print(food.title())
