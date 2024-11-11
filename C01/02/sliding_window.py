def max_num_list(num_list, k):
    max_num_list = []

    for _ in range(len(num_list) - k + 1):
        max_num_list.append(max([x for x in num_list[_:(_ + k)]]))

    return max_num_list


def is_integer(n):
    try:
        int(n)
    except ValueError:
        return False
    return True


def slid_win_input():
    num_list = []
    num_list_value = ""
    num_list_index = 0

    while num_list_value != ".":
        while True:
            num_list_value = input(
                f"Enter value {num_list_index + 1} in number list (enter . to end list): ")
            if is_integer(num_list_value) == True:
                num_list_value = int(num_list_value)
                num_list.append(num_list_value)
                num_list_index += 1
                break
            elif num_list_value == ".":
                break
            else:
                print("Value must be integer")

    while True:
        k = input("Enter k (sliding window): ")
        if k.isnumeric():
            k = int(k)
            break
        else:
            print("k must be integer")

    return num_list, k


def sliding_window_function():
    num_list, k = slid_win_input()

    print(f"Number list: {num_list}")
    print(f"Maximum number list: {max_num_list(num_list, k)}")

    return True


if __name__ == "__main__":
    # Input: Enter integer number list and k (sliding window)
    sliding_window_function()
    # Output: Print integer number list and max numbers list
