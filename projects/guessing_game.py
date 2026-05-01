import random

easy_words = ["cat", "dog", "apple", "book", "car"]
medium_words = ["python", "guitar", "mountain", "ocean", "computer"]
hard_words = ["watering", "college", "umbrella", "elephant", "diamond"]

print("WELLOME TO PASSWORD GUESSING GAME!")
print("SELECT A DIFFICULTY LEVEL")

level = input("enter difficulty: ").lower()
if level == "easy":
    word = random.choice(easy_words)
elif level == "medium":
    word = random.choice(medium_words)
elif level == "hard":
    word = random.choice(hard_words)
else:
    print("invalid difficulty level. defaulting to easy")
    word = random.choice(easy_words)
    
attempts = 0
print("\n guess the secret password!")

while True:
    guess = input("enter your guess: ").lower()
    attempts +=1
    
    if guess == word:
        print(f"congraulations! you guessed the password in {attempts} attempts")
        break
    
    hint = ""
    for i in range(len(word)):
        if i < len(guess) and guess[i] == word[i]:
            hint += guess[i]
        else:
            hint += "_"
            
    print(f"hint:{hint}")
print(f"the secret password was: {word}")
print("THANK YOU FOR PLAYING THE PASSWORD GUESSING GAME, SEE YOU NEXT TIME!")

            
            
        