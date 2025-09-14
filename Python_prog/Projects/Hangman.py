import random
from Python_prog.Projects.words_list import words

hangman_art = {0: ("   ",
                  "   ",
                  "   "),
               1: (" o ",
                  "   ",
                  "   "),
               2: (" o ",
                  " | ",
                  "   "),
               3: (" o ",
                  "/| ",
                  "   "),
               4: (" o ",
                  "/|\\",
                  "   "),
               5: (" o ",
                  "/|\\",
                  "/  "),
               6: (" o ",
                  "/|\\",
                  "/ \\")}


def display_man(wrong_guesses):
  print("********************\n")
  for line in hangman_art[wrong_guesses]:
     print(line)
  print("\n********************")

def display_hint(hint):
  print(" ".join(hint))

def display_answer(answer):
  print(" ".join(answer))


def main():
  answer=random.choice(words)
  hint=["_"]*len(answer)
  wrong_guesses = 0
  guessed_letters = set()
  is_running = True

  while is_running:
    display_man(wrong_guesses)
    display_hint(hint)
    guess = input("Enter a Leter: ").lower()
    
    if len(guess)!=1 or not guess.isalpha():
      print("\nInvalid Input\n")
      continue

    if guess in guessed_letters: 
      print(f"\n{guess} is already guessed\n")
      continue
    
    guessed_letters.add(guess)

    if guess in answer:
      for i in range(len(answer)):
        if answer[i]==guess:
          hint[i]=guess
    else:
      wrong_guesses+=1

    if "_" not in hint:
      display_man(wrong_guesses)
      display_answer(answer)
      print("\nYOU WIN!\n")
      is_running = False

    elif wrong_guesses>=len(hangman_art)-1:
      display_man(wrong_guesses)
      display_answer(answer)
      print("\nYOU LOSE!\n")
      is_running = False

if __name__ == "__main__":
  main()

