import random

def randomNumber():
    digits = list(range(1,10))
    random.shuffle(digits)
    return tuple(digits[:3])

def convertGuess(num:str) -> (int, int, int):
    if num.isnumeric() == False:
        return None
    if len(num) != 3:
        return None

    lst = []
    for d in num:
        lst.append(int(d))
    return tuple(lst)

def checkAnswer(guess, answer) -> (int, int):
    hits = 0
    blows = 0

    for n in range(0,3):
        if guess[n] == answer[n]:
            hits += 1
    
    if guess[0] == answer[1] or guess[0] == answer[2]:
        blows += 1
    if guess[1] == answer[0] or guess[1] == answer[2]:
        blows += 1
    if guess[2] == answer[0] or guess[2] == answer[1]:
        blows += 1
    
    print(f"{hits} hit(s), {blows} blow(s)!")
    print()
    return (hits, blows)

def main():
    p_num = None
    c_num = randomNumber()
    tries = 1
    done = False

    while tries < 10 and done == False:
        p_num = convertGuess(input(f"Round {tries}: Enter a 3-digit number. "))
        while p_num == None:
            print("Answer is too short or long.")
            p_num = convertGuess(input(f"Enter a 3-digit number. "))
        if checkAnswer(p_num, c_num) == (3, 0):
            done = True
        else:
            tries += 1
    
    if tries < 10:
        print(f"You won in {tries} tries!")
    else:
        print(f"Game Over! The number was {c_num}.")

if __name__ == '__main__':
    main()