from datetime import datetime
import nltk
from nltk.corpus import words

#this function leverages the nltk library to create and generate a list containing all the words in the NLTK project dictionary
def get_english_dictionary() -> list:
    #words.words() is an NLTK method 
    dictionary = words.words()
    return dictionary

#this function accepts a string an integer, the string is the word to be translated, and the integer is how many letters to shift the word
def caesar_cipher(word, shift) -> str:
    result = ''
    for i in range(len(word)):
        character = word[i]
        #this takes the character in question, translates it to a unicode character, shifts the unicode character, 
        #then translates the unicdde character into the new letter, and adds it to the result
        result+= chr((ord(character) + shift - 97) % 26 + 97)
    return result

def main():
    nltk.download('words')
    words = get_english_dictionary()
    candidates = []
    #these numbers were chosen to ensure vowels are translated into other vowels
    #A->E: 5, A->I: 8, A->O:14,A->U:20, E->I:4,E->O:10,E->U:16,E->A:22, I->O:6, I->U:12, I->A:18, I->E:22, O->U:6 O->A:12 O->E:17 O->I:20 U->A:6 U->E:10 U->I:14 U->O:20
    shifts_to_test = [4,5,6,8,10,12,14,16,17,18,20,22]
    #this loop loops over every word, calls the caesar_cipher function to translate it, then adds it to the candidates array
    #if the translated word is a valid word (appears in words)
    for word in words:
        test = word.lower()
        for shift in shifts_to_test:
            cipher = caesar_cipher(test,shift)
            if cipher in words:
                candidates.append([word,cipher])
    #sorts by length, so longer, more evocative words will be listed first
    candidates.sort(key = lambda s:len(s[0]), reverse = True)
    with open('sorted_candidates.txt','a') as f:
        for candidate in candidates:
            f.write(str(candidate)+'\n')
    return candidates
    

if __name__ == "__main__":
    initial_time = datetime.now()
    main()
    finish_time = datetime.now()
    print(f'script finished, runtime is {finish_time - initial_time}')
