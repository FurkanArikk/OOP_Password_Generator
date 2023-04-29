import random
from string import ascii_letters

class Main:

    letters = []

    for letter in ascii_letters:
        letters.append(letter)

    nums = []

    for num in range(0, 10):
        nums.append(f"{num}")
        num += 1
    symbols = ['~', ':', "'", '+', '[', '\\', '@', '^', '{', '%', '(', '-', '"', '*', '|', ',', '&', '<', '`', '}', '.',
               '_', '=', ']', '!', '>', ';', '?', '#', '$', ')', '/']

    def __init__(self, length, level):
        self.length = length
        self.level = level

    def create_password(self):
        if self.level == "Basic":
            random.shuffle(Main.letters)

            chosen_letter = random.sample(Main.letters, self.length)
            result = "".join(chosen_letter)
            return result

        elif self.level == "Medium":
            while True:
                try:
                    # enter the number of characters
                    how_many_letters = int(input("How many letters do you want in password: "))
                    how_many_numbers = int(input("How many numbers do you want in password: "))
                    total = how_many_letters + how_many_numbers

                    if total > self.length:
                        print("Characters total count is greater than the password length")

                    # picking random letters
                    word = []
                    for i in range(how_many_letters):
                        word.append(random.choice(Main.letters))
                    # picking random numbers
                    for i in range(how_many_numbers):
                        word.append(random.choice(Main.nums))

                    if total < self.length:
                        random.shuffle(Main.letters)
                        for i in range(self.length - total):
                            word.append(random.choice(Main.letters))

                    random.shuffle(word)
                    return "".join(word)

                except ValueError:
                    print("Please enter an integer number.")

        elif self.level == "Expert":
            while True:
                try:
                    # enter the number of characters
                    how_many_letters = int(input("How many letters do you want in password: "))
                    how_many_numbers = int(input("How many numbers do you want in password: "))
                    how_many_symbols = int(input("How many symbols do you want in password: "))
                    total = how_many_letters + how_many_numbers + how_many_symbols

                    if total > self.length:
                        print("Characters total count is greater than the password length")
                        continue

                    word = []
                    # picking random letters
                    for i in range(how_many_letters):
                        word.append(random.choice(Main.letters))
                    # picking random numbers
                    for i in range(how_many_numbers):
                        word.append(random.choice(Main.nums))
                    # picking symbols
                    for i in range(how_many_symbols):
                        word.append(random.choice(Main.symbols))

                    if total < self.length:
                        random.shuffle(Main.symbols)
                        for i in range(self.length - total):
                            word.append(random.choice(Main.symbols))

                    random.shuffle(word)
                    return "".join(word)

                except ValueError:
                    print("Please enter an integer number.")


while True:
    try:
        welcome_message = "Welcome to the password generator"
        print(welcome_message.upper())
        print("-" * 33)
        print("Choose your password level")
        print("-" * 33)
        print(
            """1 - Basic(only letters)\n"""
            """2 - Medium(letters and numbers)\n"""
            """3 - Expert(letters,numbers and symbols)\n"""
            """4 - Exit"""
        )
        print("-" * 33)
        #add capitalize() to make uppercase the first letter of the selection
        choice = int(input("Enter your choice: ".capitalize()))

        if choice == 1:
            length = int(input("Enter the length of your password: "))
            password = Main(length=length,level="Basic")
            print(f"Result: {password.create_password()}")
            message = input("Press enter the continue\n")
        elif  choice == 2:
            length = int(input("Enter the length of your password: "))
            password2 = Main(length = length,level="Medium")
            print(f"Result: {password2.create_password()}")
            message = input("Press enter the continue\n")
        if choice == 3:
            length = int(input("Enter the length of your password: "))
            password3 = Main(length=length,level="Expert")
            print(f"Result: {password3.create_password()}")
            print("-" * 30)
            message = input("Press enter to continue\n")
        elif choice == 4:
            break

    except ValueError:
        print("Please enter integer value")