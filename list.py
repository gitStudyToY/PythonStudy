# coding=utf-8
names = ["Marry","Tom","Eric"]
print(names[0])
print(names[1])
print(names[2])

print("Hello " + names[0])
print("Hello " + names[1])
print("Hello " + names[2])

print(names[0] + "," + names[1] + "," + names[2])

name_marry = names[0]
print(name_marry + " can't come")

names[0] = "Toney"
print(names[0] + "," + names[1] + "," + names[2])

names.insert(0,"Marry")
names.insert(3,"Lina")
names.append("Kalen")
print(names[0] + "," + names[1] + "," + names[2] + "," + names[3] + "," + names[4] + "," + names[5])

print("Sorry,I could can make two person to come my home")

person_sorry = names.pop()
print("Sorry " + person_sorry)

person_sorry = names.pop()
print("Sorry " + person_sorry)

person_sorry = names.pop()
print("Sorry " + person_sorry)

person_sorry = names.pop()
print("Sorry " + person_sorry)

print(names[0] , "Welcome to my home")
print(names[1] , "Welcome to my home")

del names[0]
del names[0]

addresses = ["america","beijing","wuhan","changsha","hangzhou","hainan"]
print(addresses)

print(sorted(addresses))

print(addresses)

print(sorted(addresses,reverse = True))

print(addresses)
addresses.reverse()
print(addresses)

print(addresses)
addresses.reverse()
print(addresses)

print(addresses)
addresses.sort()
print(addresses)

print(addresses)
addresses.sort(reverse = True)
print(addresses)

print(addresses)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)
cars.reverse()
print(cars)

print(len(names))

###for—≠ª∑######
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
	print(magician)
	
	
pizzas = ['a','b','c']
for pizza in pizzas:
	print(pizza)
	
for pizza in pizzas:
	print("I like " + pizza + " pizza")
	
print( "I really love pizza!") 

for value in range(1,21):
	print(value)

nums = []
for value in range(1,1000001):
	nums.append(value)
print(min(nums))
print(max(nums))
print(sum(nums))

numbers = [value for value in range(1,1000001)]
print(min(numbers))
print(max(numbers))
print(sum(numbers))

odd_numbers = [value for value in range(1,20,2)]
print(odd_numbers)

numbers_3 = [value for value in range(3,31,3)]
print(numbers_3)

numbers = [value**3 for value in range(1,11)]
print(numbers)
	





