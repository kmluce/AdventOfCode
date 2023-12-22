import unittest
from puzzle import Puzzle
from puzzle import card_hand_type
from puzzle import card_hand_value


class MyTestCase(unittest.TestCase):
    def test_card_type(self):
        self.assertEqual(7, card_hand_type('AAAAA'))
        self.assertEqual(6, card_hand_type('KAAAA'))
        self.assertEqual(5, card_hand_type('KAAKA'))
        self.assertEqual(4, card_hand_type('1AAKA'))
        self.assertEqual(3, card_hand_type('1AKKA'))

    def test_card_value(self):
        self.assertEqual(1414141414, card_hand_value('AAAAA'))

    # @unittest.skip("Skipping testing part A with demo data, not yet implemented")
    def test_demo_part_a(self):
        demo_a = Puzzle("demo_data1.txt", "a", 1)
        answer = demo_a.solve()
        self.assertEqual(6440, answer)

    # @unittest.skip("Skipping testing part A with real data, not yet implemented")
    def test_part_a(self):
        part_a = Puzzle("test_data.txt", "a", 1)
        answer = part_a.solve()
        self.assertEqual(-1, answer)

    @unittest.skip("Skipping testing part B with demo data, not yet implemented")
    def test_demo_part_b(self):
        demo_b = Puzzle("demo_data1.txt", "b", 1)
        answer = demo_b.solve()
        self.assertEqual(-1, answer)

    @unittest.skip("Skipping testing part B with real data, not yet implemented")
    def test_part_b(self):
        part_b = Puzzle("test_data.txt", "b", 1)
        answer = part_b.solve()
        self.assertEqual(-1, answer)


if __name__ == '__main__':
    unittest.main()
