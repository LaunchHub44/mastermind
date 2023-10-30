import random

def randNum():
    digits = list(range(1, 10))
    random.shuffle(digits)
    return tuple(digits[:3])

def ansToTuple(num:str):
    if not num.isnumeric():
        return None
    if len(num) != 3:
        return None
    
    rtn = []
    for n in num:
        rtn.append(int(n))
    return tuple(rtn)

def checkAnswer(guess, answer):
    hits = 0
    blows = 0
    
    for i in range(0,3):
        if guess[i] == answer[i]:
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
    player_num = None
    cpu_num = randNum()
    tries = 1
    won = False
    
    while tries < 10 and won == False:
        player_num = ansToTuple(input("Enter a three-digit number. "))
        while player_num == None:
            print("Invalid response.")
            player_num = ansToTuple(input("Enter a three-digit number. "))
        if checkAnswer(player_num, cpu_num) == (3, 0):
            won = True
        else:
            tries += 1
            print(f"You have {10-tries} tries left.")
    
    if won == True:
        print(f"You won in {tries} tries!")
    else:
        print(f"Game over! The number was {cpu_num}.")

if __name__ == "__main__":
    main()