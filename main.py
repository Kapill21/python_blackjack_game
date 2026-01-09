import art
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]



def initial_draw():


    user_score = int(user_hand[0]) + int(user_hand[1])

    computer_score = int(computer_hand[0]) + int(computer_hand[1])
    print(f'Your cards: {user_hand}, current score: {user_score} ')
    print(f'\nComputer\'s first card: {computer_card1}')


    if user_score == 21 or computer_score == 21:
        if computer_score == 21:
            print('\nBlackjack!')
            print(f'\nComputer\'s hand: {computer_hand}')
            print('You lose!')
            return True
        elif user_score == 21 and not computer_score ==21:
            print('\nBlackjack!')
            print(f'\nComputer\'s hand: {computer_hand}')
            print('You win!')
            return True
        elif user_score == 21 and computer_score == 21:
            print('\nBlackjack!')
            print(f'\nComputer\'s hand: {computer_hand}')
            print('Draw!')
            return True

def user_draw():
    user_card3 = random.choice(cards)
    user_hand.append(user_card3)

    if sum(user_hand) > 21:
        user_hand.remove(user_card3)
        user_hand.append(int(1))

    user_score = 0
    for card in user_hand:
        user_score += int(card)
    print(f'Your cards: {user_hand}, current score: {user_score} ')
    print(f'\nComputer\'s first card: {computer_card1}')

def computer_draw():
    computer_score = 0
    computer_score = sum(computer_hand)
    while computer_score <= 16:
        computer_hand.append(random.choice(cards))
    if sum(computer_hand) > 21:
        computer_hand.pop()
        computer_hand.append(int(1))
    computer_score = sum(computer_hand)

    if computer_score == 21:

        print(f'\nComputer\'s hand: {computer_hand}')
        print('You lose!')
        return True

def over_21():
    user_score = 0
    computer_score = 0
    for card in user_hand:
        user_score += int(card)
    for card in computer_hand:
        computer_score += int(card)
    if user_score >21:

        print(f'\nComputer\'s hand: {computer_hand}')
        print(f'Computer\'s score: {computer_score}')
        print('You lose!')
        return True

def check_over_21():
    user_score = 0
    computer_score = 0
    for card in user_hand:
        user_score += int(card)
    for card in computer_hand:
        computer_score += int(card)
    if user_score > 21 and not computer_score > 21:

        print(f'\nComputer\'s hand: {computer_hand}')
        print(f'Computer\'s score: {computer_score}')
        print('You went over. You lose!')
        return True
    elif computer_score > 21 and not user_score >21:

        print(f'\nComputer\'s hand: {computer_hand}')
        print(f'Computer\'s score: {computer_score}')
        print('Opponent went over. You win!')
        return True
    return False

def compare_scores():
    user_score = 0
    computer_score = 0
    for card in user_hand:
        user_score += int(card)
    for card in computer_hand:
        computer_score += int(card)
    if user_score > computer_score:

        print(f"\nYour final hand: {user_hand}, final score: {user_score}")
        print(f'Computer\'s hand: {computer_hand}')
        print(f'Computer\'s score: {computer_score}')
        print('You win!')
        return True
    elif computer_score > user_score:

        print(f"\nYour final hand: {user_hand}, final score: {user_score}")
        print(f'Computer\'s hand: {computer_hand}')
        print(f'Computer\'s score: {computer_score}')
        print('You lose!')
        return True
    else:

        print(f"\nYour final hand: {user_hand}, final score: {user_score}")
        print(f'Computer\'s hand: {computer_hand}')
        print(f'Computer\'s score: {computer_score}')
        print('Draw!')
        return True

def game():


    print(art.logo)
    if initial_draw():
        return True
    else:
        continue_cards = input('continue taking cards: ')

        while continue_cards == 'y':
            user_draw()
            if over_21():
                return True
            continue_cards = input('continue taking cards: ')
            if continue_cards == 'n':
                break

        if computer_draw():
            return True
        if check_over_21():
            return True
        compare_scores()



game_over = False
while not game_over and input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    user_hand = []
    computer_hand = []

    user_card1 = random.choice(cards)
    user_card2 = random.choice(cards)
    user_hand.append(user_card1)
    user_hand.append(user_card2)

    computer_card1 = random.choice(cards)
    computer_card2 = random.choice(cards)
    computer_hand.append(computer_card1)
    computer_hand.append(computer_card2)


    game_over = game()
print('Have a great day!')
