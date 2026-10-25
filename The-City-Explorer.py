pasta = ("Pasta Arrabiata", "Italian", 20, "Medium")
biryani = ("Chicken Biryani", "Indian", 45, "Hard")
print("Recipe 1: ", pasta)
print("Name: ", pasta[0])
print("Cuisine: ", pasta[1])
print("Difficulty: ", pasta[-1])
all_recipes = (pasta, biryani)
print("\nFirst recipe name: ", all_recipes[0][0])
print("Second recipe time: ", all_recipes[1][2], "mins")
print("Pasta details (sliced): ", pasta[1:3])
print("\nPasta Recipe details: ")
for detail in pasta:
    print("-", detail)
a = {"tomato", "garlic", "pasta", "chilli"}
b = {"rice", "chicken", "garlic", "tomato"}
a.add("Cheese")
a.discard("chilli")
print(a | b, a & b, a - b, a ^ b)