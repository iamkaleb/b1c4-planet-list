# # Lists (ordered, mutable & allows duplicates)

# animals = ["Jack", "Noonan", "Blue", "Gypsy"]

# junk = ["Fred", True, [1, 2, 3], 234]

# # Adding items to the list
# junk.append(234)
# junk.insert(0, "oh, I get it")
# print(junk)
# junk.extend(["Mary", "Joseph", "Bob"])
# print(junk)

# # Negative indexing
# junk[-1] = "The last item"
# print(junk[-4])

# # Loop through the items in a list
# for taco in junk:
#     print(taco)

# # Javascript equivalent: junk.forEach(taco => console.log(taco));

# # You can declare an empty list:
# stuff = []

# Create a NEW list from a subset of values in another list with slice
my_list = [1, 2, 4, "hello", "monkey"]
my_subset = my_list[0:3]
my_subset = my_list[1:3]
my_subset = my_list[:3]
my_subset = my_list[2:]
print(my_subset)
print(my_list)

planet_list = ["Mercury", "Mars"]

planet_list.append('Jupiter')
planet_list.append('Saturn')

planet_list.extend(['Uranus', 'Neptune'])

planet_list.insert(1, 'Venus')
planet_list.insert(2, 'Earth')

planet_list.append('Pluto')

rocky_planets = planet_list[0:4]

del planet_list[-1]

print(planet_list)
print(rocky_planets)