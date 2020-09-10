amount = int(input())
list_victories = []
no_victories = 0
for i in range(amount):
    new_element = input().split()
    if new_element[1] == "win":
        no_victories += 1
        list_victories.append(new_element[0])

print(list_victories)
print(no_victories)

