# ==============================================================================
# 🚀 PROJECT: HANGMAN GAME (TECH INTERNSHIP EDITION)
# 
# DESCRIPTION: 
# A robust, terminal-based implementation of the classic Hangman game built using 
# Python. This project highlights industry-standard practices, edge-case validation,
# and structured clean code.
#
# KEY FEATURES:
# 1. Advanced Input Validation: Handles empty strings, spaces, and numbers safely.
# 2. Smart Game State Tracking: Prevents repeating already-guessed letters.
# 3. Dynamic Visual UI: Displays visual gallows (ASCII Art) changing progressively.
#
# TECHNICAL DETAILS:
# - Language: Python 3.x
# - Data Structures Used: Set (for fast lookup) and List (for sequential graphics)
# ==============================================================================

import random
from typing import List, Set

# Visual tracking status layout stages array
HANGMAN_PICS: List[str] = [
    """
     +---+

         |
         |
         |
        ===""", 
    """
     +---+
     O   |

         |
         |
        ===""", 
    """
     +---+
     O   |

     |   |
         |
        ===""", 
    """
     +---+
     O   |
    /|   |

         |
        ===""", 
    """
     +---+
     O   |
    /|\\  |

         |
        ===""", 
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""", 
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

def select_random_word(words: List[str]) -> str:
    """Selects a random secret word from the word list."""
    return random.choice(words).lower()

def display_current_state(word: str, guessed: Set[str]) -> str:
    """Builds the masked word string output status."""
    return " ".join([char if char in guessed else "_" for char in word])

def get_valid_input(guessed: Set[str]) -> str:
    """Validates absolute strict criteria for standard input letters."""
    while True:
        # Strip handles accidental blank space strings gracefully
        guess = input("👉 Guess a letter: ").strip().lower()
        
        # Absolute empty string kani multi-character array block filter bounds validation
        if not guess or len(guess) != 1 or not guess.isalpha():
            print("⚠️  Invalid entry. Please type exactly one single letter (A-Z).")
            continue
            
        if guess in guessed:
            print("💡 Letter already tried. Try a different one.")
            continue
            
        return guess

def run_game() -> None:
    """Core runtime engine block flow control."""
    word_bank: List[str] = ["cloud", "algorithm", "backend", "frontend", "compiler"]
    secret_word: str = select_random_word(word_bank)
    guessed_letters: Set[str] = set()
    
    max_lives: int = 6
    wrong_attempts: int = 0

    print("🚀 Tech Internship Hangman Pro Edition")
    
    while wrong_attempts < max_lives:
        print(HANGMAN_PICS[wrong_attempts])
        
        current_display = display_current_state(secret_word, guessed_letters)
        print(f"Word: {current_display}")
        print(f"Attempts left: {max_lives - wrong_attempts}")

        if "_" not in current_display:
            print(f"\n🎯 Success! You decoded the word: {secret_word.upper()} 🎉")
            return

        next_guess = get_valid_input(guessed_letters)
        guessed_letters.add(next_guess)

        if next_guess in secret_word:
            print("✅ Good guess!")
        else:
            print("❌ Incorrect!")
            wrong_attempts += 1

    print(HANGMAN_PICS[wrong_attempts])
    print(f"\n👾 Out of lives! The system word was: {secret_word.upper()} 💀")

if __name__ == "__main__":
    run_game()
