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
        self.name = "Dealer" if is_dealer is None else name
        self.score = 0
        self.is_dealer = is_dealer
        self.card_list = []

    def hit(self, deck):
        card, value = deck.get_card()
        self.score += value
        self.card_list.append(card)

        return card, value

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


if __name__ == "__main__":
    deck = Deck()
    dealer = Player(is_dealer=True)
    player = Player("hari")

    while True:
        # * deal two cards
        # dealer
        dealer.hit(deck)
        dealer.hit(deck)
        # player
        player.hit(deck)
        player.hit(deck)

        print(dealer.card_list)
        print(dealer.score)
        print(player.card_list)
        print(player.score)

        break