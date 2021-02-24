temp = int(input("Temperature: "))
type = input("F or C: ")

if type == "F":
    temp = (temp-32)/1.8
    print(temp)
elif type == "C":
    temp = temp*1.8+32
    print(temp)
else:
    print("Please select a correct type (C or F)")