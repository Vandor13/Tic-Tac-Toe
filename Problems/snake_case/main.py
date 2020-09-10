input_string = input()
output_string = ""

for c in input_string:
    if c.isupper():
        output_string += "_" + c.lower()
    else:
        output_string += c

print(output_string)
