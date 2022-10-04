import secrets
import math
import time


def main():
    keys_to_brute = []

    for i in multiplied_step_loop(8, 4096):
        print(
            f'Кількість варіантів ключів для {i}-бітної послідовності:\n{2**i}\n')

        random_key = key_from_binary(random_binary(i))

        keys_to_brute += [{"key": random_key, "bits": i}]

        print(
            f'Випадкове значення ключа у {i}-бітній послідовності:\n{random_key}\n')

        print('---------------------------------------------------------------------------')

    for item in keys_to_brute:
        print(
            f'Брут ключа {item["bits"]}-бітної послідовності:\n{item["key"]}\n')
        bruteforce_test(item['key'])
        print('---------------------------------------------------------------------------')


def multiplied_step_loop(i, end):
    while i <= end:
        yield i
        i *= 2


def random_binary(binary_length):
    binary_string = ''

    for _ in range(binary_length):
        binary_string += str(secrets.randbelow(2))

    return binary_string


def key_from_binary(binary):
    decimal_representation = int(binary, 2)
    hexadecimal_string = hex(decimal_representation)
    return hexadecimal_string


def bruteforce_test(searchable):
    start_time = time.time()

    for i in range(int(searchable, 16) + 1):
        if (hex(i) == searchable):
            end_time = time.time()
            diff = end_time - start_time

            print(
                f'Було витрачено часу для знаходження ключа: {math.floor(diff * 1000)} мілісекунд')
            break


main()
