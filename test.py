numbers = []
total = 0
while True:
    value = input("enter a number or write stop to quit: ")
    if value.lower() == "stop":
        break
    try:
        num = int(value)
        numbers.append(num)
        total += num
    except:
        print("please enter a number: ")
print( numbers )
print(total)

    
