import itertools
import random

def generate_cards(suits, max_rank):
    all_combinations = list(itertools.product(suits, range(1, max_rank + 1)))
    
    cards = [(suit, rank) for suit, rank in all_combinations]
    
    random.shuffle(cards)
    
    return cards

suits = {'Hearts', 'Bells', 'Sword'}
max_rank = 5
cards = generate_cards(suits, max_rank)
print(cards)
