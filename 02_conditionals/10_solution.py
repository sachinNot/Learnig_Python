species = "dog"
age = 3   # age in years

if species == "dog":
    if age < 2:
        food = "Puppy food"
    else:
        food = "Adult dog food"

elif species == "cat":
    if age > 5:
        food = "Senior cat food"
    else:
        food = "Adult cat food"

else:
    food = "Unknown species, no recommendation available."


print("Recommended food:", food)
