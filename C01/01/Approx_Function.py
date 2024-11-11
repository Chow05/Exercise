def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


def is_number(n):
    try:
        float(n)
    except ValueError:
        return False
    return True


def cal_approx(x, n):
    sin_res = 0.0
    cos_res = 0.0
    sinh_res = 0.0
    cosh_res = 0.0
    for _ in range(n):
        sin_res += ((-1) ** _) * ((x ** (2 * _ + 1)) / factorial((2 * _ + 1)))
        cos_res += ((-1) ** _) * ((x ** (2 * _)) / factorial((2 * _)))
        sinh_res += (x ** (2 * _ + 1)) / factorial((2 * _ + 1))
        cosh_res += (x ** (2 * _)) / factorial((2 * _))
    return sin_res, cos_res, sinh_res, cosh_res


if __name__ == "__main__":
    print("Please enter value x and n")
    while True:
        x = input("Enter value x (x is radian): ")
        if is_number(x) == True:
            x = float(x)
            break
        else:
            print("Please enter value x (x is radian) agian")
    while True:
        n = input("Enter value n (n E Z+): ")
        if n.isnumeric() and float(n) > 0:
            n = int(n)
            break
        else:
            print("Please enter value n (n E Z+) again")

    cal_approx_res = cal_approx(x, n)
    print(f"approx_sin (x={x}, n={n}): {cal_approx_res[0]}")
    print(f"approx_cos (x={x}, n={n}): {cal_approx_res[1]}")
    print(f"approx_sinh (x={x}, n={n}): {cal_approx_res[2]}")
    print(f"approx_cosh (x={x}, n={n}): {cal_approx_res[3]}")
