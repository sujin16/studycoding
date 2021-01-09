def soultion(numbers):
    numbers= list(map(str,numbers))
    print(numbers)
    numbers.sort(key =lambda x: x*3,reverse =True)
    return str(int(''.join(numbers)))
numbers=[6,2,10]

print(soultion(numbers))