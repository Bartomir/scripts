import random

name_list = []
while True:
    decision = raw_input('Enter a name or type "end" to finish:')
    if decision == 'end':
        break
    name_list.append(decision)

print(name_list)
random.shuffle(name_list)

groups_number = int(input('Pick number of groups:'))

all_groups = {'Group {}'.format(i + 1): [] for i in range(groups_number)}

while name_list:
    for group in all_groups.values():
        try:
            group.append(name_list.pop())
        except IndexError:
            break

for key in sorted(all_groups.iterkeys()):
    print "%s: %s" % (key, all_groups[key])
