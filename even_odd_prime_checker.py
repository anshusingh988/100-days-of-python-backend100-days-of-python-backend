def is_even(num: int) -> bool:
    return num % 2 == 0


def is_prime(num: int) -> bool:
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def main():
    try:
        num = int(input("Enter a number: "))

        # Even / Odd
        if is_even(num):
            print(f"{num} is Even")
        else:
            print(f"{num} is Odd")

        # Prime
        if is_prime(num):
            print(f"{num} is a Prime number")
        else:
            print(f"{num} is not a Prime number")

    except ValueError:
        print("❌ Please enter a valid integer number")


if __name__ == "__main__":
    main()
