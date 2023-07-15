import random
word_list=["dog","procrastination","resolution"]
chosen_word=random.choice(word_list)

#placing blanks
display=[]
for letter in chosen_word:
    display+="_"

print(display)


end_of_the_game=False

#checking answer
while not end_of_the_game:

    guess=input("guess a letter:").lower()

    for position in range(len(chosen_word)):
        letter=chosen_word[position]

        if letter==guess:
            display[position]=guess
            print(display)
    if "_" not in display:
        end_of_the_game=True
        print("You win!")
        

       

