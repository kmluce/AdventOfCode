import unittest
from puzzle import Puzzle

class MyTestCase(unittest.TestCase):
    def test_demoa(self):
        demoa = Puzzle("demo_data.txt")
        demoa.parsea()
        answer = demoa.solvea()
        self.assertEqual(150, answer)

    def test_fulla(self):
        fulla = Puzzle("test_data.txt")
        fulla.parsea()
        answer = fulla.solvea()
        self.assertEqual(1694130, answer)

    def test_demob(self):
        demob = Puzzle("demo_data.txt")
        demob.parseb()
        answer = demob.solvea()
        self.assertEqual(900, answer)

    def test_fullb(self):
        fullb = Puzzle("test_data.txt")
        fullb.parseb()
        answer = fullb.solvea()
        self.assertEqual(1698850445, answer)

if __name__ == '__main__':
    unittest.main()
