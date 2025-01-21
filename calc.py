import time

def kaprekars_constant():
    def sort_digits(num, reverse=False):
        """Sort the digits of a number in ascending or descending order."""
        return int("".join(sorted(f"{num:04d}", reverse=reverse)))

    def kaprekar_step(num):
        """Perform one step of Kaprekar's routine."""
        ascending = sort_digits(num)
        descending = sort_digits(num, reverse=True)
        return descending - ascending

    print("Kaprekar's Constant Calculator!")
    while True:
        try:
            user_input = int(
                input("Enter a 4-digit number (at least two different digits): ")
            )
            if 1000 <= user_input <= 9999 and len(set(str(user_input))) > 1:
                break
            else:
                print(
                    "Invalid input. Please enter a 4-digit number with at least two different digits."
                )
        except ValueError:
            print("Invalid input. Please enter a valid 4-digit number.")

    print(f"\nStarting with: {user_input}")
    print(f"Step ;: decending - ascending of {user_input}")

    steps = 0
    while user_input != 6174:
        ascending = sort_digits(user_input)
        descending = sort_digits(user_input, reverse=True)
        result = kaprekar_step(user_input)

        print(f"\nStep {steps + 1}: {descending} - {ascending} = {result}")

        user_input = result
        steps += 1
        time.sleep(0.4)
                        
    print(f"\nKaprekar's constant (6174) reached in {steps} steps.")


if __name__ == "__main__":
    kaprekars_constant()
