import random
# get guess from user
def get_guess():
    return list(input("What is your guess?\n"))

# generate a random number
def generate_code():
    digits = [str(num) for num in range(10)]
    random.shuffle(digits)
    return(digits[:3])

# generate clues
def generate_clues(code, user_guess):
    if user_guess == code:
        return "CODE CRACKED"
    clues = []
    for ind,num in enumerate(user_guess):
        if num == code[ind]:
            clues.append("MATCH")
        elif num in code:
            clues.append("CLOSE")
    if clues == []:
        return ["NOPE!"]
    else:
        return clues

# Game logic
print("Welcome to Code-Breaker!, press zzz to quit.")
secret_code = generate_code()
clue_report = []
while clue_report != "CODE CRACKED":
    guess = get_guess()
    if guess == ['z','z','z']:
        break;
    clue_report = generate_clues(guess, secret_code)
    print("Here is the result of your guess: ")
    for clues in clue_report:
        print(clues)
