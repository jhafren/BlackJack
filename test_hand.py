import unittest
from hand import Hand
from card import Card

class TestHand(unittest.TestCase):
    
    def test_sum_one_card(self):
        hand = Hand()
        hand.take(Card(2, "spades"))

        result = hand.sum()

        self.assertEqual(result, 2)

    def test_sum_one_face_one_ace(self):
        hand = Hand()
        hand.take(Card(1, "spades"))
        hand.take(Card(11, "spades"))

        result = hand.sum()

        self.assertEqual(result, 21)

    def test_sum_two_faces(self):
        hand = Hand()
        hand.take(Card(11, "spades"))
        hand.take(Card(13, "spades"))

        result = hand.sum()

        self.assertEqual(result, 20)

    def test_sum_two_faces_one_ace(self):
        hand = Hand()
        hand.take(Card(11, "spades"))
        hand.take(Card(13, "spades"))
        hand.take(Card(1, "spades"))

        result = hand.sum()

        self.assertEqual(result, 21)

    def test_sum_three_faces_one_ace(self):
        hand = Hand()
        hand.take(Card(11, "spades"))
        hand.take(Card(12, "spades"))
        hand.take(Card(13, "spades"))
        hand.take(Card(1, "spades"))

        result = hand.sum()

        self.assertEqual(result, 31)

    def test_sum_one_face_two_aces(self):
        hand = Hand()
        hand.take(Card(11, "spades"))
        hand.take(Card(1, "spades"))
        hand.take(Card(1, "hearts"))

        result = hand.sum()

        self.assertEqual(result, 12)

    def test_sum_5_cards(self):
        hand = Hand()
        hand.take(Card(11, "spades"))
        hand.take(Card(6, "spades"))
        hand.take(Card(1, "spades"))
        hand.take(Card(1, "hearts"))
        hand.take(Card(1, "diamonds"))

        result = hand.sum()

        self.assertEqual(result, 19)

if __name__ == "__main__":
    unittest.main()

