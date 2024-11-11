import re


def count_chars_input():
    while True:
        string = input("Enter string ([a-z] or/and [A-Z]): ")
        if bool(re.match(r'^[a-zA-Z ]+$', string)):
            break
        else:
            print("String must be [a-z] or/and [A-Z]")

    string = string.replace(" ", "")

    return string


def count_chars_function():
    string = count_chars_input()
    keys_list = list(set(string))
    values_list = []

    for keys_list_item in keys_list:
        char_count = 0
        for string_char in string:
            if string_char == keys_list_item:
                char_count += 1
        values_list.append(char_count)

    count_chars_dict = dict(zip(keys_list, values_list))
    count_chars_dict = dict(
        sorted(count_chars_dict.items(), key=lambda item: item[1]))
    print(f"Count each character in string: {count_chars_dict}")

    return True


if __name__ == "__main__":
    count_chars_function()          # Input: a string ([a-z] or/and [A-Z])
    # Output: a dictionary (value ascending)
