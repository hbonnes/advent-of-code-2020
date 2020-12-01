def star_one(input_path='1.txt'):
    with open(input_path) as f:
        numbers = [int(x) for x in f.read().strip().split('\n')]

    num_one = None
    num_two = None
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            # Removes already done numbers
            j_index = j + i + 1
            if numbers[i] + numbers[j_index] == 2020:
                num_one = numbers[i]
                num_two = numbers[j_index]
                break

    print(f'{num_one} + {num_two} = 2020')
    print(f'{num_one} x {num_two} = {num_one * num_two}')


def star_two(input_path='1.txt'):
    with open(input_path) as f:
        numbers = [int(x) for x in f.read().strip().split('\n')]

    num_one = None
    num_two = None
    num_three = None
    for i in range(len(numbers)):
        for j in range(len(numbers) - i - 1):
            j_index = j + i + 1
            for k in range(len(numbers) - j_index - 1):
                k_index = k + j_index + 1

                if numbers[i] + numbers[j_index] + numbers[k_index] == 2020:
                    num_one = numbers[i]
                    num_two = numbers[j_index]
                    num_three = numbers[k_index]
                    break

    print(f'{num_one} + {num_two} + {num_three} = 2020')
    print(f'{num_one} x {num_two} x {num_three} = {num_one * num_two * num_three}')


star_one()
star_two()