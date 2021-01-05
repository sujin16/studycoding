def soultion(numbers):
  
    for i in range(1,len(numbers)):
        j, key = i-1,numbers[i]
        while j>=0:
            key_str =str(key)[0] 
            j_str = str(numbers[j])[0]

            if  int(j_str) >int(key_str): break

            if len(str(key))>1 : key_str =str(key)[1:]
            if len(str(numbers[j]))>1 : j_str =str(numbers[j])[1:]
            
            if  int(j_str) >= int(key_str): break
            numbers[j+1] =numbers[j]
            j =j-1

        numbers[j+1] =key
            

numbers=[6,10,2] 
soultion(numbers)
numbers ="".join[str(i) for i in numbers]
print(numbers)

