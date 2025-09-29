import pygame
import sys
import os
import random

pygame.init()
pygame.font.init()
pygame.mixer.init()

WIN_width, WIN_height = 1000 , 1000
win = pygame.display.set_mode((WIN_width,WIN_height))
pygame.display.set_caption("BlackJack")
font = pygame.font.SysFont("comicsans",50)

background = pygame.image.load(os.path.join("imgs","background.jpg"))
background = pygame.transform.scale(background,(WIN_width,WIN_height))

card_sound = pygame.mixer.Sound(os.path.join("sounds","card_sound.wav"))

class Card:
    def __init__(self,card_image,card_value):
        self.image = card_image
        self.value = card_value
    
    def change_card_value(self):
        self.value = 1
    
cards = []
my_funds = 500

def load_cards(folder_path):
    

    for filename in os.listdir(folder_path):
        filepath = os.path.join(folder_path,filename)
        card_image = pygame.image.load(filepath)
        card_image = pygame.transform.scale(card_image,(100,145))

        card_name = filename.replace(".png","")

        face_value = card_name.split('_')[0]

        if face_value in ["jack","king","queen"]:
            card_value = 10
        elif face_value == "ace":
            card_value = 11
        else:
            card_value = int(face_value)
        
        myCard = Card(card_image,card_value)

        cards.append(myCard)

load_cards("cards")                         

def pull_card(cards_pulled):
    pygame.time.delay(500)
    card_sound.play()
    while True:
        rand_index = random.randint(0, 51)
        if rand_index not in cards_pulled:
            cards_pulled.append(rand_index)
            return rand_index

def check_aces(current_cards):
    my_total = 22
    for card in current_cards:
        if card.value == 11:
            card.value = 1
            my_total = sum(card.value for card in current_cards)
        if my_total <= 21:
            break

def current_game(my_bet):
    run = True
    dealt = False
    dealer_hidden = True
    dealer_won = False
    player_won = False
    game_over = False
    my_cards = []
    dealer_cards = []
    cards_pulled = []

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if not game_over and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    random_number = pull_card(cards_pulled)
                    my_cards.append(cards[random_number])

                if event.key == pygame.K_RETURN:
                    dealer_hidden = False  # Reveal dealer cards (stand)

            if game_over and event.type == pygame.KEYDOWN:    
                if event.key == pygame.K_r:

                    if player_won and dealer_won:
                        my_bet = my_bet
                    elif player_won:
                        my_bet = my_bet*2
                    elif dealer_won:
                        my_bet = 0

                    return my_bet

        # Deal initial 2 cards each
        if not dealt:
            while len(cards_pulled) < 4:
                random_number = pull_card(cards_pulled)
                if len(cards_pulled) % 2 == 0:
                    my_cards.append(cards[random_number])
                else:
                    dealer_cards.append(cards[random_number])

                # Redraw screen after each card is dealt
                win.blit(background, (0, 0))

                # Draw current cards
                for i, card in enumerate(my_cards):
                    win.blit(card.image, (200 + i * 100, 400))
                for i, card in enumerate(dealer_cards):
                    if i == 1 and dealer_hidden:
                        # hide second dealer card
                        back_side = pygame.image.load(os.path.join("imgs", "back-side.png"))
                        back_side = pygame.transform.scale(back_side, (100, 145))
                        win.blit(back_side, (300, 200))
                    else:
                        win.blit(card.image, (200 + i * 100, 200))

                pygame.display.update()
                   

            dealt = True

        # Calculate totals
        my_total = sum(card.value for card in my_cards)
        dealer_total = sum(card.value for card in dealer_cards)

        #check for aces
        if my_total > 21:
            check_aces(my_cards)
        
        if dealer_total > 21:
            check_aces(dealer_cards)
        
        # Check player state
        if my_total == 21:
            player_won = True
            game_over = True
        elif my_total > 21:
            dealer_won = True
            game_over = True

        # If player stands, dealer plays
        if not dealer_hidden:
            if dealer_total <= 16 and not game_over:
                random_number = pull_card(cards_pulled)
                dealer_cards.append(cards[random_number])
                dealer_total = sum(card.value for card in dealer_cards)

            if dealer_total > 21:
                player_won = True
                game_over = True
            elif dealer_total == 21:
                dealer_won = True
                game_over = True
            elif dealer_total > 16:
                # Compare to player
                if dealer_total > my_total:
                    dealer_won = True
                elif dealer_total < my_total:
                    player_won = True
                else:
                    dealer_won = True
                    player_won = True  # Push
                game_over = True

        # 🖼️ Draw background and cards
        win.blit(background, (0, 0))

        # Draw player's cards
        for i, card in enumerate(my_cards):
            win.blit(card.image, (200 + i * 100, 400))
        
        #Draw bet
        my_bet_font = font.render(f"Betting: ${my_bet}", True, (255, 255, 255))
        win.blit(my_bet_font,(500, 20))

        # Draw dealer's cards
        if dealer_hidden:
            win.blit(dealer_cards[0].image, (200, 200))
            back_side = pygame.image.load(os.path.join("imgs", "back-side.png"))
            back_side = pygame.transform.scale(back_side, (100, 145))
            win.blit(back_side, (300, 200))
        else:
            for i, card in enumerate(dealer_cards):
                win.blit(card.image, (200 + i * 100, 200))
            dealer_total_text = font.render(f"Dealer Total: {dealer_total}", True, (255, 255, 255))
            win.blit(dealer_total_text, (20, 50))

        # Draw player's total
        if my_total == 21:
            my_total_text = font.render("You have 21! Blackjack!", True, (255, 255, 255))
        elif my_total > 21:
            my_total_text = font.render(f"You busted! ({my_total})", True, (255, 255, 255))
        else:
            my_total_text = font.render(f"Your Total: {my_total}", True, (255, 255, 255))
        win.blit(my_total_text, (20, 550))

        # Show outcome
        outcome_text = ""
        if game_over:
            if player_won and dealer_won:
                outcome_text = "It's a push!"
            elif player_won:
                outcome_text = "You win!"
            elif dealer_won:
                outcome_text = "Dealer wins!"
            win.blit(font.render(outcome_text, True, (255, 255, 255)), (20, 750))
        else:
            # Draw instructions
            controls_text = font.render("Space = Hit | Enter = Stand", True, (255, 255, 255))
            win.blit(controls_text, (20, 700))

        pygame.display.update()

   


def run_main_menu(winnings):
    run = True
    global my_funds
    my_bet = 100

    my_funds += winnings
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    my_funds -= my_bet
                    return my_bet

        win.blit(background, (0, 0))
        start_game_text = font.render('Press Space to start', True, (255, 255, 255))
        win.blit(start_game_text, (200, 300))
        my_funds_s = "$"+str(my_funds)
        funds_font = font.render(my_funds_s, True, (255, 255, 255))
        win.blit(funds_font, (800, 20))

        pygame.display.update()
    
        

def main():
    winnings = 0
    while True:
        my_bet = run_main_menu(winnings)
        winnings = current_game(my_bet)

main()
