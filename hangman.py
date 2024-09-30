import random

with open('english_word.txt', 'r') as file:
    words = file.read().splitlines()

random_word = random.choice(words)

random_list=[]
for i in random_word:    
    random_list.append(i)
#print(random_list)

new_list = ['_' for _ in range(len(random_list))]
max_attempts = 6
attempts = 0

while attempts < max_attempts:
    entered_word = input("Enter a letter: ").lower()

    if entered_word in random_list:
        all_occurrences = [i for i, val in enumerate(random_list) if val == entered_word]
        #print(f"All occurrences of '{entered_word}' are at indices: {all_occurrences}.")

        for i in all_occurrences:
            new_list[i] = entered_word
        print(f"Current word: {' '.join(new_list)}")

        if new_list == random_list:
            print("Hurray! You won the game!")
            break
    else:
        attempts += 1
        print(f"The letter '{entered_word}' is not in the word. Remaining attempts: {max_attempts - attempts}")

    if attempts == max_attempts:
        print("You are hung! Game over!")
        break

print("The final word is:", ''.join(random_list))
print("Your guess was:", ' '.join(new_list))
