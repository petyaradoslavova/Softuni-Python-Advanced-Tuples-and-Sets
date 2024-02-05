from collections import deque


def print_list(label, items):
    if items:
        print(f'{label}: {", ".join(map(str, items))}')


tools = deque(int(x) for x in input().split())
substances = [int(y) for y in input().split()]
challenges = [int(z) for z in input().split()]

while tools and substances:
    current_tool = tools.popleft()
    current_substance = substances.pop()

    result = current_tool * current_substance
    if result in challenges:
        challenges.remove(result)
    else:
        current_tool += 1
        tools.append(current_tool)
        current_substance -= 1
        if current_substance > 0:
            substances.append(current_substance)

if not challenges:
    print("Harry found an ostracon, which is dated to the 6th century BCE.")
else:
    print("Harry is lost in the temple. Oblivion awaits him.")

print_list('Tools', tools)
print_list('Substances', substances)
print_list('Challenges', challenges)
