from random import shuffle


class Deck:
    suits = ("spades", "hearts", "diamonds", "clubs")
    ranks = (
        "Two",
        "Three",
        "Four",
        "Five",
        "Six",
        "Seven",
        "Eight",
        "Nine",
        "Ten",
        "Joker",
        "Queen",
        "King",
        "Ace",
    )
    ranks_value = {
        "Two": 2,
        "Three": 3,
        "Four": 4,
        "Five": 5,
        "Six": 6,
        "Seven": 7,
        "Eight": 8,
        "Nine": 9,
        "Ten": 10,
        "Joker": 10,
        "Queen": 10,
        "King": 10,
        "Ace": 11,  # defaulting ace to 11 and not 11 or 1
    }

    def __init__(self) -> None:
        self.cards = []
        for suit in Deck.suits:
            for rank in Deck.ranks:
                self.cards.append((suit, rank))

        shuffle(self.cards)

    def get_card(self):
        card = self.cards.pop()
        value = Deck.ranks_value.get(card[1])

        return card, value


class Player:
    def __init__(self, name="Player", is_dealer=False) -> None:
        self.name = "Dealer" if is_dealer else name
        self.score = 0
        self.is_dealer = is_dealer
        self.card_list = []

    def __repr__(self) -> str:
        score = str(self.score)
        card_list = [f"{rank} of {suit}" for suit, rank in self.card_list]
        return ", ".join(card_list) + "\n Total Score: " + score

    def hit(self, deck):
        card, value = deck.get_card()
        self.score += value
        self.card_list.append(card)
        return card, value

    def input_choice(self):
        player_choice = ""
        while player_choice != "h" and player_choice != "s":
            player_choice = input(f"{self.name}, do you want to hit(h) or stay(s) ?\n")

        return player_choice

    def stay(self):
        pass

    def check_if_bust(self) -> bool:
        if self.is_dealer:
            if self.score > 17:
                return True
            return False
        else:
            if self.score > 21:
                return True
            return False

    def win(self):
        return self.score == 21


if __name__ == "__main__":
    deck = Deck()
    dealer = Player(is_dealer=True)
    player = Player("hari")

    GAME_ON = True
    PLAYER_ON = True
    DEALER_ON = True
    WHO_WON = ""

    while GAME_ON:
        # * deal two cards
        # dealer
        dealer.hit(deck)
        dealer.hit(deck)
        # player
        player.hit(deck)
        player.hit(deck)

        while PLAYER_ON:
            print(player)
            player_choice = player.input_choice()
            if player_choice == "h":
                card, value = player.hit(deck)
                print(f"{player.name} got {card[1]} of {card[0]}")

                if player.check_if_bust():
                    PLAYER_ON = False
                    DEALER_ON = False
                    GAME_ON = False
                    WHO_WON = "Dealer"

                if player.win():
                    PLAYER_ON = False
                    GAME_ON = False
                    DEALER_ON = False
                    WHO_WON = "Player"

            if player_choice == "s":
                PLAYER_ON = False

        while DEALER_ON and GAME_ON:
            if dealer.check_if_bust():
                print(dealer)
                WHO_WON = "Player"
                DEALER_ON = False
                GAME_ON = False
            else:
                while dealer.score < 17:
                    dealer.hit(deck)
                    print(dealer)
                    if dealer.win():
                        DEALER_ON = False
                        GAME_ON = False
                        WHO_WON = "Dealer"
                    break

    print(f"Winner is {WHO_WON}")
    print(player)
    print(dealer)