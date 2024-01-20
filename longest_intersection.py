longest_intersection = set()

for _ in range(int(input())):
    first_data , second_data = [el.split(',') for el in input().split("-")]

    first_set = set(range(int(first_data[0]),int(first_data[1]) + 1))
    second_set = set(range(int(second_data[0]), int(second_data[1]) + 1))

    intersection = first_set.intersection(second_set)

    if len(intersection) > len(longest_intersection):
        longest_intersection = intersection

print(f'Longest intersection is [{", ".join(str(x) for x in longest_intersection)}]'
      f' with length {len(longest_intersection)}')









# import sys
# number_of_intersection_couples = int(input())
#
# max_number = -sys.maxsize
# counter = 0
# intersection = 0
#
# while number_of_intersection_couples:
#     current_couple = input().split("-")
#     set1 = set()
#     set2 = set()
#     for numbers in current_couple:
#         start_number,end_number = numbers.split(',')
#         counter += 1
#         for num in range(int(start_number),int(end_number)+1):
#             if counter %2 !=0:
#                 set1.add(num)
#             else:
#                 set2.add(num)
#
#     intersection_length = len(set1&set2)
#     if intersection_length > max_number:
#         max_number = intersection_length
#         intersection = (set1 & set2)
#     number_of_intersection_couples-=1
#
# print(f"Longest intersection is {list(intersection)} with length {max_number}")