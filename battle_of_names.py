number_of_names = int(input())

odd_set = set()
even_set = set()

for n in range(1,number_of_names+1):
    sum_of_char = sum(ord(char) for char in input()) // n
    if sum_of_char % 2 != 0:
        odd_set.add(sum_of_char)
    else:
        even_set.add(sum_of_char)

sum_odd_set , sum_even_set = sum(odd_set),sum(even_set)

if sum_odd_set == sum_even_set:
    print(*odd_set.union(even_set), sep=", ")
elif sum_odd_set > sum_even_set:
    print(*odd_set.difference(even_set), sep=", ")
else:
    print(*odd_set.symmetric_difference(even_set), sep=", ")
