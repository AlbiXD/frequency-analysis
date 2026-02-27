#!/usr/bin/env python3

from simple_term_menu import TerminalMenu
banner = r"""
 _____ ____  _____ ____  _     _____ _      ____ ___  _   ____  _      ____  _    ___  _ ____  _  ____    ____ _____ _____ ____  ____  _  __
/    //  __\/  __//  _ \/ \ /\/  __// \  /|/   _\\  \//  /  _ \/ \  /|/  _ \/ \   \  \/// ___\/ \/ ___\  /  _ Y__ __Y__ __Y  _ \/   _\/ |/ /
|  __\|  \/||  \  | / \|| | |||  \  | |\ |||  /   \  /   | / \|| |\ ||| / \|| |    \  / |    \| ||    \  | / \| / \   / \ | / \||  /  |   / 
| |   |    /|  /_ | \_\|| \_/||  /_ | | \|||  \__ / /    | |-||| | \||| |-||| |_/\ / /  \___ || |\___ |  | |-|| | |   | | | |-|||  \__|   \ 
\_/   \_/\_\\____\\____\\____/\____\\_/  \|\____//_/     \_/ \|\_/  \|\_/ \|\____//_/   \____/\_/\____/  \_/ \| \_/   \_/ \_/ \|\____/\_|\_\
"""



# Layout CIPHER TEXT, DECRYPT TEXT


freq_map = {}
    
# Sets up the frequency table 
def init_freq_map():
    for i in range((ord('Z') - ord(' ') +1)):
        freq_map[chr(ord(' ')+i)] = 0



def main():
    init_freq_map()
    
    for key in freq_map:
        print(key)
    print(banner)
    cipher = input("Enter Cipher: ")
    entry_options = ["Perform Frequency Analysis", "Exit"]
    
    terminal_menu = TerminalMenu(entry_options, preview_size=0.75,)
    menu_entry_index = terminal_menu.show()


if __name__ == "__main__":
    main()