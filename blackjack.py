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
        "Jack",
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
        "Jack": 10,
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
        card = self.cards.pop(0)
        value = Deck.ranks_value.get(card[1])

        return card, value


class Player:
    ...


if __name__ == "__main__":
    dck = Deck()
