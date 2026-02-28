#!/usr/bin/env python3

import sys
import heapq
# Layout CIPHER TEXT, DECRYPT TEXT

# Letters sorted by frequency in the English language
LETTERS_SORTED_BY_FREQUENCY = ['E', 'T', 'A', 'O', 'I', 'N', 'S', 'R', 'H', 'L', 'D', 'C', 'U', 'M', 'F', 'P', 'G', 'W', 'Y', 'B', 'V', 'K', 'X', 'J', 'Q', 'Z']

freq_map = {}

# freq_max_heap will store a tuple of the negative frequency (to make min heap a max heap)
# and the letter
# e.g. (-20, 'a')
freq_max_heap = []

# The key is a letter from the cipher, the value is a letter from LETTERS_SORTED_BY_FREQUENCY
letters_map = {}

# Stores letters that already have been mapped
# NOTE: The letters will correspond to LETTERS_SORTED_BY_FREQUENCY (value in letters_map),
# NOT the letters from the cipher (key in letters_map)
mapped_letters = set()
    
# Sets up the frequency table 
def init_freq_map():
    for i in range(ord('A'), ord('Z') + 1):
        freq_map[chr(i)] = 0

# Puts frequency of letters from cipher into freq_map
def get_freq(cipher: str):
    for letter in cipher:
        if ord(letter) >= 32 and ord(letter) <= 64:
            continue
        freq_map[letter] += 1
def display_commands():
    print("D - print debug")
    print("C - change mapping")
    print("E - exit from loop")
    print("? - display list of commandsc")
# Setting freq_max_heap using values in freq_map
def set_freq_max_heap():
    for letter, freq in freq_map.items():
        if freq != 0:
            # Push tuple of -freq (because of max heap) and letter
            heapq.heappush(freq_max_heap, (-freq, letter))

# Map frequent letters in cipher to most frequent letters in the English language
def map_letters():
    for i in range(len(freq_max_heap)):
        tup = heapq.heappop(freq_max_heap)
        letter = tup[1]

        letters_map[letter] = LETTERS_SORTED_BY_FREQUENCY[i]
        mapped_letters.add(LETTERS_SORTED_BY_FREQUENCY[i])

def display_mapping():
    total = len(letters_map)
    new_line = 0
    i = 1
    print("-" * 40)
    print(f"  | {'Cipher':<10} | {'Plain':<10} |")
    print("-" * 40)
    for key in letters_map:
        print(f"{i} |{key:<10}  | {letters_map[key]:<10} |")
        i+=1
    print("-" * 40)
def display_cipher_text(cipher: str):
    print(cipher)
    
def change_mapping():
    while(True):
        display_mapping()
        print("Which letter would you like to change?")
        change = str(input("$ "))
        print(f"Which letter would you like to replace {change} with?")
        replace = str(input("$ "))
        
        letters_map[change] = replace

        display_mapping()
        print("Finish? (Y/N)")
        prompt = input("$ ")
        if prompt.lower == "Y":
            break
        return
def display_debug(cipher: str):
    print("\n")
    print("Mapping")
    display_mapping()
    print("\n")
    print("Cipher Text")
    display_cipher_text(cipher)
    print("\n")
    print("Decoded Text")
    
    
def main():
    init_freq_map()
    entry_options = ["Perform Frequency Analysis", "Exit"]
    print("1)", entry_options[0])
    print("2)", entry_options[1])

    x = input("$ ")
        # Get user selection
    if x == '1':
        cipher = input("Enter Cipher: ")
        get_freq(cipher)
        set_freq_max_heap()
        map_letters()
    else: sys.exit(0)
    print("Type ? for a list of commands")
    while True:
        x = input("$ ")
        match x:
            case '?':
                display_commands()
            case 'C':
                change_mapping()
            case 'D':
                display_debug(cipher)
            case _:
                print("Type ? for a list of commands")
if __name__ == "__main__":
    main()
