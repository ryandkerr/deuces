from deuces import Card
from deuces import Evaluator
from deuces import Deck

c = Card.new("Qh")

Card.print_pretty_cards([c])

p1 = [Card.new("As"), Card.new("Ks")]
p2 = [Card.new("Ah"), Card.new("Ts")]

board = [Card.new("Ad"), Card.new("5h"), Card.new("5d"), Card.new("7s"), Card.new("Js")]

wins = 0
for i in range(1,1000):
    deck = Deck()
    board = deck.draw(5)
    player1_hand = deck.draw(2)
    player2_hand = deck.draw(2)
    evaluator = Evaluator()

    if(evaluator.evaluate(board, player1_hand) > evaluator.evaluate(board, player2_hand)):
        wins += 1

print wins / 1000.0


# print Evaluator().evaluate(board, p1)
# print Evaluator().evaluate(board, p2)
