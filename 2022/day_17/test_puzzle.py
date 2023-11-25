import unittest
import numpy as np
from puzzle import Puzzle
from puzzle import DropMap


class MyTestCase(unittest.TestCase):

    def test_small_unit_tests(self):
        result_a = np.array([[0, 1, 0, 0, 0, 0, 0],
                             [1, 1, 1, 0, 0, 0, 0],
                             [0, 1, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0],
                             [0, 0, 0, 0, 0, 0, 0]])
        test_a = Puzzle("demo_data1.txt", "a", 7, 2022)
        self.assertTrue(np.array_equal(result_a, test_a.test_setup()))

    def test_stringify_array(self):
        result_a = """[[0100000]
[1110000]
[0100000]
[0000000]
[0000000]
[0000000]
[0000000]
[0000000]]"""
        my_map = DropMap(7, 8)
        my_map.add_rock_to_map(1, 0, 0)
        self.assertEqual(result_a, my_map.stringify())

    def test_is_collision_complete_overlap(self):
        my_map = DropMap(7, 8)
        my_map.add_rock_to_map(1, 0, 0)
        self.assertTrue(my_map.is_collision(1, 0, 0))

    def test_is_collision_vertical_overlap(self):
        my_map = DropMap(7, 8)
        my_map.add_rock_to_map(1, 0, 0)
        self.assertTrue(my_map.is_collision(1, 0, 2))

    def test_is_collision_horizontal_overlap(self):
        my_map = DropMap(7, 8)
        my_map.add_rock_to_map(1, 0, 0)
        self.assertTrue(my_map.is_collision(1, 2, 0))

    def test_is_collision_no_overlap(self):
        my_map = DropMap(7, 8)
        my_map.add_rock_to_map(1, 0, 0)
        self.assertFalse(my_map.is_collision(1, 0, 4))

    # @unittest.skip("Skipping testing part A with demo data, not yet implemented")
    def test_demo_part_a(self):
        demo_a = Puzzle("demo_data1.txt", "a", 1, 2022)
        answer = demo_a.solve()
        self.assertEqual(3068, answer)

    # @unittest.skip("Skipping testing part A with real data, not yet implemented")
    def test_part_a(self):
        part_a = Puzzle("test_data.txt", "a", 1, 2022)
        answer = part_a.solve()
        self.assertEqual(3127, answer)

    # @unittest.skip("Skipping testing part B with demo data, not yet implemented")
    def test_demo_part_b(self):
        demo_b = Puzzle("demo_data1.txt", "b", 1, 1000000000000)
        answer = demo_b.solve()
        self.assertEqual(1514285714288, answer)

    # @unittest.skip("Skipping testing part B with real data, not yet implemented")
    def test_part_b(self):
        part_b = Puzzle("test_data.txt", "b", 1, 1000000000000)
        answer = part_b.solve()
        self.assertEqual(1542941176480, answer)


if __name__ == '__main__':
    unittest.main()
