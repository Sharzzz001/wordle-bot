import random

# Load a dictionary of 5-letter words
with open('all_wordle_words.txt', 'r') as f:
    wordlist = [line.strip() for line in f]
english_words_alpha = wordlist.copy()
english_words_alpha_set = set(english_words_alpha)

# Define the length of the target word
WORD_LENGTH = 5

def get_candidate_words():
    candidate_words = []
    for word in english_words_alpha_set:
        if len(word) == WORD_LENGTH:
            candidate_words.append(word)
    return candidate_words

def get_feedback(guess):
    greens = input("Enter the number of green letters: ")
    yellows = input("Enter the number of yellow letters: ")
    return int(greens), int(yellows)

def filter_words(candidate_words, guess, greens, yellows):
    remaining_words = []
    for word in candidate_words:
        if (sum([1 for i in range(WORD_LENGTH) if word[i] == guess[i]]) == greens
            and sum([1 for i in range(WORD_LENGTH) if word[i] != guess[i] and word[i] in guess]) == yellows):
            remaining_words.append(word)
    return remaining_words

def select_word(candidate_words):
    if (len(candidate_words)==len(english_words_alpha)):
        candidate_words.remove('adept')
        a = 'adept'
        print(a)
        return 'adept'
    else:
        a=random.choice(candidate_words)
        print(a)
        return a

def play_game():
    candidate_words = get_candidate_words()
    guess = select_word(candidate_words)
    # print(guess)
    
    while len(candidate_words) > 1:
        greens, yellows = get_feedback(guess)
        candidate_words = filter_words(candidate_words, guess, greens, yellows)
        print(("Guesses left: "+str(len(candidate_words))))
        
        if len(candidate_words) == 0:
            print("No candidate words left! The game is over.")
            return
        
        guess = select_word(candidate_words)
        # print(guess)
        
    print(f"The word is '{candidate_words[0]}'.")
    
play_game()