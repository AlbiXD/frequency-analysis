#!/usr/bin/env python3

import sys
from simple_term_menu import TerminalMenu
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
        freq_map[letter] += 1

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

def main():
    init_freq_map()
    
    entry_options = ["Perform Frequency Analysis", "Exit"]
    
    terminal_menu = TerminalMenu(entry_options, preview_size=0.75)
    menu_entry_index = terminal_menu.show()

    # Get user selection
    selection = entry_options[menu_entry_index]
    if selection == entry_options[0]:
        cipher = input("Enter Cipher: ")
        get_freq(cipher)
        set_freq_max_heap()
        map_letters()

        # TESTING
        print("\nfreq_map")
        for letter, freq in freq_map.items():
            if freq > 0:
                print(f"${letter}: ${freq}")
        print()

        print("letters_map")
        print(letters_map)
        print()

        print("mapped_letters")
        print(mapped_letters)
    else: sys.exit(0)

if __name__ == "__main__":
    main()
