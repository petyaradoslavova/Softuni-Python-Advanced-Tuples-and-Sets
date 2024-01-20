text = [char for char in input()]
same_values_dict = {}

for n in text:
    if n not in same_values_dict:
        same_values_dict[n] = 0
    same_values_dict[n] += 1

[print(f"{key}: {value} time/s")for key,value in sorted(same_values_dict.items())]

# text = input()
#
# for symbol in sorted(set(text)):
#     print(f"{symbol}: {text.count(symbol)} time/s")