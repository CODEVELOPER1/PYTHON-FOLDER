#Secert Word Game with loops

secert_word = "giraffe" #secert word
guess = "" #stores user response
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secert_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter Secert Word Guess. You Only have 3 tries, Choose Wisely: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print('Nice Try, but you didn\'t succeed, you ran out of guesses. Thanks for Playing! Good-Bye')
else:
    print("You got the Secert Word")



