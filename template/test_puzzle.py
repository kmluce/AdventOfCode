import unittest
from puzzle import Puzzle


class MyTestCase(unittest.TestCase):
    # @unittest.skip("Skipping testing part A with demo data, not yet implemented")
    def test_demo_part_a(self):
        demo_a = Puzzle("demo_data1.txt", "a", 10)
        answer = demo_a.solve()
        self.assertEqual(-1, answer)

    @unittest.skip("Skipping testing part A with real data, not yet implemented")
    def test_part_a(self):
        part_a = Puzzle("test_data.txt", "a", 10)
        answer = part_a.solve()
        self.assertEqual(-1, answer)

    @unittest.skip("Skipping testing part B with demo data, not yet implemented")
    def test_demo_part_b(self):
        demo_b = Puzzle("demo_data1.txt", "b", 10)
        answer = demo_b.solve()
        self.assertEqual(-1, answer)

    @unittest.skip("Skipping testing part B with real data, not yet implemented")
    def test_part_b(self):
        part_b = Puzzle("test_data.txt", "b", 10)
        answer = part_b.solve()
        self.assertEqual(-1, answer)


if __name__ == '__main__':
    unittest.main()
