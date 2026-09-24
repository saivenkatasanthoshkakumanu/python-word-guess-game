import random

fields = {
    "1": {
        "name": "Food",
        "word": "PINEAPPLE",
        "clue": "It has a reputation for starting arguments on pizza."
    },
    "2": {
        "name": "Sports",
        "word": "MARATHON",
        "clue": "The event where finishing itself is basically the flex."
    },
    "3": {
        "name": "Places",
        "word": "VENICE",
        "clue": "A city where your taxi might need to be a boat."
    },
    "4": {
        "name": "Movies & TV",
        "word": "TITANIC",
        "clue": "A movie where everyone knows the ending before pressing play."
    },
    "5": {
        "name": "Games",
        "word": "TETRIS",
        "clue": "The game that convinced people falling blocks could be stressful."
    },
    "6": {
        "name": "Animals",
        "word": "CHAMELEON",
        "clue": "Famous for changing its appearance, although pop culture exaggerates how it does it."
    },
    "7": {
        "name": "Cars",
        "word": "MUSTANG",
        "clue": "A horse that somehow ended up with four wheels."
    },
    "8": {
        "name": "Music",
        "word": "KARAOKE",
        "clue": "The activity where confidence matters more than talent."
    },
    "9": {
        "name": "Superheroes",
        "word": "DEADPOOL",
        "clue": "A superhero whose primary superpower appears to be refusing to shut up."
    },
    "10": {
        "name": "Random / Chaos",
        "word": "DINOSAUR",
        "clue": "Extremely successful for millions of years. Terrible at avoiding extinction."
    }
}


print("=" * 50)
print("                 FIELD GUESS")
print("=" * 50)

print("\nChoose your field:\n")

for number, field in fields.items():
    print(number + ". " + field["name"])

choice = input("\nEnter field number: ")

if choice not in fields:
    print("\nInvalid choice.")

else:

    selected = fields[choice]

    word = selected["word"]
    clue = selected["clue"]

    guesses_left = 10
    guessed = set()

    print("\n" + "=" * 50)
    print("FIELD:", selected["name"])
    print("=" * 50)

    print("\nCLUE:")
    print(clue)

    print("\nYou have 10 total guesses.")
    print("Guess one letter at a time.\n")

    while guesses_left > 0:

        display = ""

        for letter in word:
            if letter in guessed:
                display += letter + " "
            else:
                display += "_ "

        print("Word:", display)
        print("Guesses left:", guesses_left)

        if all(letter in guessed for letter in word):
            print("\nYou won!")
            print("The word was:", word)
            break

        guess = input("Guess a letter: ").upper()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter only one letter.\n")
            continue

        if guess in guessed:
            print("You already guessed that letter.\n")
            continue

        guessed.add(guess)
        guesses_left -= 1

        if guess in word:
            print("Correct!\n")
        else:
            print("That letter is not in the word.\n")

    else:
        print("\nOut of guesses!")
        print("The word was:", word)
