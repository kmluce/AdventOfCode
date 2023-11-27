import unittest
import puzzle


class MyTestCase(unittest.TestCase):
    def test_demo(self):
        with open("demo_data.txt") as file:
            data = puzzle.parse(file.readlines())
        answer = puzzle.solvea(data)
        self.assertEqual(7, answer)
        answer = puzzle.solveb(data)
        self.assertEqual(5, answer)
    def test_a(self):
        with open("test_data1.txt") as file:
            data = puzzle.parse(file.readlines())
        answer = puzzle.solvea(data)
        self.assertEqual(1228, answer)
        answer = puzzle.solveb(data)
        self.assertEqual(1257, answer)


if __name__ == '__main__':
    unittest.main()
