offset = int(input())
time = 10

if time + offset >= 24:
    print("Wednesday")
elif time + offset < 0:
    print("Monday")
else:
    print("Tuesday")
