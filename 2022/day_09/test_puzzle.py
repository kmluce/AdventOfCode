import unittest
from puzzle import Puzzle


class MyTestCase(unittest.TestCase):
    def test_demo_part_a(self):
        demoa = Puzzle("demo_data.txt", "a", 1)
        demoa.parse()
        answer = demoa.solve()
        self.assertEqual(13, answer)

    def test_part_a(self):
        parta = Puzzle("test_data.txt", "a", 1)
        parta.parse()
        answer = parta.solve()
        self.assertEqual(6271, answer)

    def test_demo_part_b(self):
        demob = Puzzle("demo_data.txt", "b", 9)
        demob.parse()
        answer = demob.solve()
        self.assertEqual(1, answer)


    def test_part_b(self):
        partb = Puzzle("test_data.txt", "b", 9)
        partb.parse()
        answer = partb.solve()
        self.assertEqual(2458, answer)


if __name__ == '__main__':
    unittest.main()