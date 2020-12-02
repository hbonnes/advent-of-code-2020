def star_one(input_path='1.txt'):
    with open(input_path) as f:
        numbers = [int(x) for x in f.read().strip().split('\n')]

    # One liners (x = numbers)
    # x = numbers
    # print([x[i] * x[j] for i in range(len(x)) for j in range(i+1, len(x)) if x[i] + x[j] == 2020][0])

    num_one = None
    num_two = None
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                num_one = numbers[i]
                num_two = numbers[j]
                break

    print(f'{num_one} + {num_two} = 2020')
    print(f'{num_one} x {num_two} = {num_one * num_two}')


def star_two(input_path='1.txt'):
    with open(input_path) as f:
        numbers = [int(x) for x in f.read().strip().split('\n')]

    # One liner
    # x = numbers
    # print([x[i] * x[j] * x[k] for i in range(len(x)) for j in range(i+1, len(x)) for k in range(j+1, len(x)) if x[i] + x[j] + x[k] == 2020][0])

    num_one = None
    num_two = None
    num_three = None
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            for k in range(j+1, len(numbers)):
                if numbers[i] + numbers[j] + numbers[k] == 2020:
                    num_one = numbers[i]
                    num_two = numbers[j]
                    num_three = numbers[k]
                    break

    print(f'{num_one} + {num_two} + {num_three} = 2020')
    print(f'{num_one} x {num_two} x {num_three} = {num_one * num_two * num_three}')


star_one()
star_two()