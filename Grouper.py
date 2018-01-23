import random

name_list = []
while True:
    decision = raw_input('Enter a name or type "no" to stop:')
    if (decision != 'no'):
        name_list.append(decision)
    else:
        break

print(name_list)
groups_number = int(input('Pick number of groups:'))

all_groups = {}
for number in range(groups_number):
    all_groups['Group ' + str(number + 1)] = []

counter = 0
while len(name_list) > 0:
    if len(name_list) >= groups_number:
        for group, player in all_groups.items():
            player.append(name_list.pop(random.randrange(len(name_list))))
            counter += groups_number
    elif len(name_list) < groups_number:
        while len(name_list) < groups_number:
            name_list.append('')
            if len(name_list) == groups_number:
                break
        if len(name_list) == counter:
            break

print (all_groups)
