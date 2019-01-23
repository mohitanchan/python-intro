

capitals = {"India":"New Delhi", "Norway":"Oslo", "France":"Paris", "Italy":"Rome"}
print(capitals)

# print all keys
print(f"\n Keys : {capitals.keys()} \n")

# print all values
print(f"\n Values : {capitals.values()} \n")

for key,val in capitals.items():
    print(f"{key} : {val}")

# Add new entry to dictionary
capitals["South Africa"] = ["Pretoria", "Cape Town"]
print(capitals)

# Another way to initialize
company = dict(name="Miles", city="Mumbai", pin=400069)
print(company)


# delete an items
del capitals["Italy"]
print(capitals)
