import unittest
from puzzle import Puzzle


class MyTestCase(unittest.TestCase):
    def test_character_node(self):
        demoa = Puzzle("demo_data.txt")
        demoa.parse()
        result = demoa.check_rules(4, "a")
        self.assertEqual(True, result)

    def test_and_node(self):
        demoa = Puzzle("demo_data.txt")
        demoa.parse()
        result = demoa.check_rules(6, "ab")
        self.assertEqual(True, result)

#    def test_demoa(self):
#        demoa = Puzzle("demo_data.txt")
#        demoa.parse()
#        answer = demoa.solvea()
#        self.assertEqual(2, answer)

#    def test_fulla(self):
#        fulla = Puzzle("test_data.txt")
#        fulla.parse()
#        answer = fulla.solvea()
#        self.assertEqual(0, answer)

#    def test_demob(self):
#        demob = Puzzle("demo_data.txt")
#        demob.parse()
#        answer = demob.solveb()
#        self.assertEqual(0, answer)

#    def test_fullb(self):
#        fullb = Puzzle("test_data.txt")
#        fullb.parse()
#        answer = fullb.solveb()
#        self.assertEqual(0, answer)

if __name__ == '__main__':
    unittest.main()
