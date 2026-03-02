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
    
# Sets up the frequency table 
def init_freq_map():
    for i in range(ord('A'), ord('Z') + 1):
        freq_map[chr(i)] = 0

# Puts frequency of letters from cipher into freq_map
def get_freq(cipher: str):
    for letter in cipher:
        if ord(letter) < 65 or ord(letter) > 90:
            continue
        freq_map[letter] += 1

# printing decoded message
def decode_cipher(cipher: str) -> str:
    decoded = ""
    for letter in cipher:
        if letter in letters_map:
            decoded += letters_map[letter]
        else:
            decoded += letter
    return decoded

def display_commands():
    print("I - print info")
    print("C - change mapping")
    print("R - reset mapping")
    print("N - enter new cipher")
    print("E - exit from loop")
    print("? - display list of commands")

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

def display_mapping():
    i = 1
    print("-" * 40)
    print(f"  | {'Cipher':<10} | {'Frequency':<10} | {'Plain':<10} |")
    print("-" * 40)
    for key in letters_map:
        print(f"{i} | {key:<10} | {freq_map[key]:<10} | {letters_map[key]:<10} |")
        i+=1
    print("-" * 40)

def display_cipher_text(cipher: str):
    print(cipher)

def display_info(cipher: str):
    print("\n")
    print("Mapping")
    display_mapping()
    print("\n")
    print("Cipher Text")
    display_cipher_text(cipher)
    print("\n")
    print("Decoded Text")
    print(decode_cipher(cipher))
    print("\n")
    
def change_mapping(cipher: str):
    display_info(cipher)

    while(True):
        print("Which letter would you like to change? Enter 0 to Cancel")
        change = str(input("$ ").upper())
        if change == "0":
            print("Canceled\n")
            return
        if change not in letters_map:
            print("This letter is not in the cipher. Please try again\n")
            continue

        restart = False
        while(True):
            print(f"Which letter would you like to replace {change} with? Enter 0 to Cancel, 1 to Restart")
            replace = str(input("$ ").upper())
            if replace == "0":
                print("Canceled\n")
                return
            elif replace == "1":
                restart = True
                break

            if ord(replace) < 65 or ord(replace) > 90:
                print("Invalid letter. Please try again")
                continue
            else: break
        if restart == True: continue
        
        letters_map[change] = replace

        display_info(cipher)
        print("Finish? (Y/N)")
        prompt = input("$ ")
        if prompt.lower() == "y":
            print()
            break
    return

def reset_global_vars():
    global freq_map, freq_max_heap, letters_map
    freq_map = {}
    freq_max_heap = []
    letters_map = {}

def perform_analysis(cipher: str):
    reset_global_vars()
    init_freq_map()
    get_freq(cipher)
    set_freq_max_heap()
    map_letters()
    display_info(cipher)

def confirm(message: str) -> bool:
    print(message)
    prompt = input("$ ")
    if prompt.lower() == "y":
        return True
    else:
        print("Canceled\n")
        return False

def main():
    entry_options = ["Perform Frequency Analysis", "Exit"]
    print("1)", entry_options[0])
    print("2)", entry_options[1])

    x = input("$ ")
    if x == '1':
        cipher = input("\nEnter Cipher: ")
        perform_analysis(cipher)
    else: sys.exit(0)

    display_commands()
    while True:
        x = input("$ ")
        match x:
            case '?':
                display_commands()
            case 'C':
                change_mapping(cipher)
            case 'I':
                display_info(cipher)
            case 'R':
                c = confirm("Are you sure you want to reset the letter mapping? This cannot be undone (Y/N)")
                if c == False: continue

                perform_analysis(cipher)
            case 'N':
                c = confirm("Are you sure you want to enter a new cipher? This will overwrite the previous cipher (Y/N)")
                if c == False: continue

                cipher = input("\nEnter Cipher: ")
                perform_analysis(cipher)
            case 'E':
                return
            case _:
                print("Type ? for a list of commands")

if __name__ == "__main__":
    main()