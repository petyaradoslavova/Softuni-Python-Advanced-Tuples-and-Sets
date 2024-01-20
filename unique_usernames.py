number_of_usernames = int(input())

unique_usernames = set()

for user in range(number_of_usernames):
    current_username = input()
    unique_usernames.add(current_username)

[print(name) for name in unique_usernames]