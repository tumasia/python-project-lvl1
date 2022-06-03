from random import randint
import prompt


def start_brain_even():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    if name:
        print(f'Hello, {name}!')
    
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i < 3:
        random_number = randint(1, 50)
        answer = prompt.string(f'Question: {random_number}\nYour answer: ')

        # all true answers
        if (random_number % 2 == 0 and answer.lower() == "yes") or (random_number % 2 != 0 and answer.lower() == "no"):
            print("Correct!")
            i += 1

        # false "yes"
        elif random_number % 2 != 0 and answer.lower() == "yes":
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
            break

        # false "no"
        else:
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
            break
        
        if i == 3:
            print(f"Congratulations, {name}!")
