cafe = input()
cafe_list = []
while cafe != "MEOW":
    cafe_list.append(cafe.split())
    cafe = input()
maximum = max([int(y) for [x, y] in cafe_list])
max_cafe = [x for [x, y] in cafe_list if int(y) == maximum]
print(max_cafe[0])
