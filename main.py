print("Name: Ryan Hermoso")
print("Section: BS COMPUTER SCIENCE 1-E")
print("Instructor: Mr. Ralph Angelo Baguio")
print("Date: December 08, 2023")
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


def display_primes_in_range(start, end):
    if start < 0:
        print("Enter a non-negative number.")
        return
    if end <= start:
        print("Enter a number greater than the start number.")
        return

    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num)


if __name__ == "__main__":
    while True:
        start = int(input("Enter the starting number (enter 0 to terminate): "))

        if start == 0:
            print("Program terminated.")
            break

        end = int(input("Enter the ending number: "))

        display_primes_in_range(start, end)

