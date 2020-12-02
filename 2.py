import re


def star_one(input_path='2.txt'):
    with open(input_path) as f:
        file_data = f.read().strip().split('\n')

    # One Liner
    # print(len([i for i in [re.findall(r'(\d+)-(\d+)\s(.):\s(.*)', x)[0] for x in file_data] if int(i[0]) <= i[3].count(i[2]) <= int(i[1])]))

    data = [re.findall(r'(\d+)-(\d+)\s(.):\s(.*)', x)[0] for x in file_data]

    password_count = 0
    for policy in data:
        min_count, max_count, character, password = (int(policy[0]), int(policy[1]), policy[2], policy[3])
        policy_count = password.count(character)
        if min_count <= policy_count <= max_count:
            password_count += 1

    print(f'FOUND {password_count} VALID PASSWORDS')


def star_two(input_path='2.txt'):
    with open(input_path) as f:
        file_data = f.read().strip().split('\n')
        data = [re.findall(r'(\d+)-(\d+)\s(.):\s(.*)', x)[0] for x in file_data]

    # One liner
    # print(len([i for i in [re.findall(r'(\d+)-(\d+)\s(.):\s(.*)', x)[0] for x in file_data] if (i[3][int(i[0])-1] == i[2]) ^ (i[3][int(i[1])-1] == i[2])]))

    data = [re.findall(r'(\d+)-(\d+)\s(.):\s(.*)', x)[0] for x in file_data]
    password_count = 0
    for policy in data:
        min_count, max_count, character, password = (int(policy[0]), int(policy[1]), policy[2], policy[3])
        contains_min = password[min_count - 1] == character
        contains_max = password[max_count - 1] == character
        if contains_min ^ contains_max:
            password_count += 1

    print(f'FOUND {password_count} VALID PASSWORDS')


star_one()
star_two()
