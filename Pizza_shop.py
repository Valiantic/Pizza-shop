

def pizzadiv(peoplenum, pizzanum):
    return peoplenum / pizzanum / pizzanum

def leftovers(peoplenum, pizzanum):
    return peoplenum % pizzanum


print("Pizza shop ni venven")
print("")
print("How many people? ")
peoplenum = int(input())
print("How many pizza do you have? ")
pizzanum = int(input())

print(f"{peoplenum} people with {pizzanum} pizzas")
divpizza = pizzadiv(peoplenum, pizzanum)
print(f"Each person gets {divpizza} of pizzas")
leftpizza = leftovers(peoplenum, pizzanum)
print(f"Each person gets {leftpizza} of pizzas")








