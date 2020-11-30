from typing import List


def generate_10_numbers_from_0_until_100() -> List[int]:

    import random
    List = [random.randint(0, 99) for k in range(10)]
    return List

def print_list(numbers: List[int]):

    for i in range(10):
        print(numbers[i])

def sort_in_ascending_order(numbers: List[int]) -> List[int]:

    n = numbers
    n.sort()
    return n

def remove_content_which_number_is_under_50(numbers: List[int]) -> List[int]:

    l = [i for i in numbers if i>=50]
    return l

if __name__ == '__main__':
    x = generate_10_numbers_from_0_until_100()
    print_list(x)
    y = sort_in_ascending_order(x)
    print(y) #確認
    z = remove_content_which_number_is_under_50(x)
    print(z) #認確
