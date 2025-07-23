import random

Words = ("apple", "bridge", "cloud", "dream", "echo", "flame", "glow", "hollow", "ice", "jewel",
         "knight", "lantern", "mirror", "night", "ocean", "petal", "quartz", "river", "stone", "tower",
         "umbrella", "valley", "whisper", "xenon", "yarn", "zephyr", "anchor", "breeze", "crystal", "dawn",
         "ember", "forest", "gale", "harbor", "island", "jungle", "key", "leaf", "meadow", "nebula",
         "opal", "pulse", "quest", "ripple", "shade", "thunder", "unity", "vortex", "willow", "zenith",
         "arcade", "binary", "cipher", "drift", "ember", "flicker", "glyph", "hazel", "ignite", "jigsaw",
         "kaleidoscope", "lunar", "matrix", "nexus", "orbit", "pixel", "quiver", "relic", "signal", "tempo",
         "uplift", "verge", "warden", "xylem", "yearn", "zen", "alpine", "blizzard", "cascade", "dusk",
         "envoy", "fable", "grove", "hover", "illusion", "jade", "karma", "legend", "mystic", "noir",
         "onyx", "prism", "quartzite", "reign", "sable", "tundra", "unison", "voyage", "wisp", "zenobia")

is_running = True

while is_running:
    Attempts = 6
    Secret_Word = random.choice(Words)
    Display = ["_"] * len(Secret_Word)
    still_guessing = True
    print()
    print("---------------- WELCOME TO HANGMAN ------------------")
    print()
    while Attempts > 0 and still_guessing:
        print(f"Guess the word, You have {Attempts} Attempts.")
        print()
        print(Display,)
        print()
        print(f"Attempts left: {Attempts}")
        Correct = False
        Guess = input("Enter your Letter: ").lower()
        for i in range(len(Secret_Word)):
            if Secret_Word[i] == Guess:
                Display[i] = Guess
                Correct = True
        if Correct == True:
            print("Correct Attempt")
        else:
            print("Inorrect Attempt")
            Attempts -= 1
        for index in range(len(Display)):
            if Display[index] == "_":
                still_guessing = True
                break
            else:
                still_guessing = False

    if Attempts == 0:
        print("----------------- YOU LOSE --------------------")
        print()
        print("You failed to attempt the word.")
        print()
        print(f"The Correct word was {Secret_Word}.")
    else:
        print("----------------- YOU WIN --------------------")
        print()
        print("You guessed it correctly, Congratulations!!!")
        print()
        print(f"The Correct word was {Secret_Word}.")
    
    print()
    if not input("Want to play again?(y/n): ").lower() == "y":
        is_running = False

print()
print("-------------THANK YOU FOR PLAYING-----------------")