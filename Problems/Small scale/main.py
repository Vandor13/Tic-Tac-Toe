input_text = input()
float_list = []
while input_text != ".":
    input_float = float(input_text)
    float_list.append(input_float)
    input_text = input()
print(min(float_list))
