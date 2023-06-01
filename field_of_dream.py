import re
import random

words = ["hello", "work", "bike", "python"]
selection_word = random.choice(words)
attempts = int(input("Enter numbers of try: "))
part_pattern = " "
count = 0
while True:
    if count == attempts:
        print("You lose")
        break
    elem = input("Enter letter or word: ")
    if len(elem) == 1:
        if elem in selection_word:
            part_pattern += elem
            pattern = f"[^{part_pattern.strip()}]"
            print(re.sub(pattern, "*", selection_word))
            continue
        else:
            print("Invalid letter")
            count += 1
            continue

    else:
        if elem == selection_word:
            print("You won")
            break
        else:
            print("Invalid word")
            count += 1
