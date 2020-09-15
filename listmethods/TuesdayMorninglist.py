#!/usr/bin/env python3
#list of pets:
pets = ['fido', 'spot', 'fluffy']
i1 = input("Please insert a pet name:")
pets.append(i1)
print(len(pets))
i2 = input("Please insert another pet name:")
pets.append(i2)
print(len(pets))
i3 = input("Please insert one more pet name:")
pets.append(i3)
print(len(pets))
print(pets)
for index, pet in enumerate(pets):
    print(index, pet)
