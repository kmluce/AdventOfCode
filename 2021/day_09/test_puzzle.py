import unittest
from puzzle import Puzzle


class MyTestCase(unittest.TestCase):
    @unittest.skip("Skipping testing part A with demo data, not yet implemented")
    def test_demoa(self):
        demoa = Puzzle("demo_data.txt")
        demoa.parse()
        answer = demoa.solve_a()
        self.assertEqual(15, answer)

    @unittest.skip("Skipping testing part A with demo data, not yet implemented")
    def test_fulla(self):
        fulla = Puzzle("test_data.txt")
        fulla.parse()
        answer = fulla.solve_a()
        self.assertEqual(577, answer)


    def test_demob(self):
        demob = Puzzle("demo_data.txt")
        demob.parse()
        answer = demob.solve_b()
        self.assertEqual(0, answer)


#    def test_fullb(self):
#        fullb = Puzzle("test_data.txt")
#        fullb.parse()
#        answer = fullb.solveb()
#        self.assertEqual(0, answer)


if __name__ == '__main__':
    unittest.main()
