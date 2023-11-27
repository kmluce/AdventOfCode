import unittest
from puzzle import Puzzle


class MyTestCase(unittest.TestCase):
    def test_demoa(self):
        demoa = Puzzle("demo_data.txt")
        demoa.parse()
        answer = demoa.solvea(80)
        self.assertEqual(5934, answer)

    def test_fulla(self):
        fulla = Puzzle("test_data.txt")
        fulla.parse()
        answer = fulla.solvea(80)
        self.assertEqual(361169, answer)

    def test_demob(self):
        demob = Puzzle("demo_data.txt")
        demob.parse()
        answer = demob.solvea(256)
        self.assertEqual(26984457539, answer)

    def test_fullb(self):
        fullb = Puzzle("test_data.txt")
        fullb.parse()
        answer = fullb.solvea(256)
        self.assertEqual(0, answer)


if __name__ == '__main__':
    unittest.main()
