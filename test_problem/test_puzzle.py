import unittest
import puzzle


class MyTestCase(unittest.TestCase):
    def test_demo(self):
        with open("demo_data.txt") as file:
            data = puzzle.parse(file.readlines())
        answer = puzzle.solve(data)
        self.assertEqual(0, answer)


if __name__ == '__main__':
    unittest.main()
