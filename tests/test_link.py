# tests/test_link.py

import unittest
from src.link import Link

class TestLink(unittest.TestCase):
    def test_calculate_distance(self):
        link = Link()
        link.add_node(0, 0, 'upper')
        link.add_node(3, 4, 'lower')
        distance = link.calculate_distance(0, 1)
        self.assertEqual(distance, 5)

    def test_rotate(self):
        link = Link()
        link.add_node(0, 0, 'upper')
        link.add_node(100, 0, 'lower')
        link.rotate(90)
        self.assertAlmostEqual(link.nodes[1].x, 0)
        self.assertAlmostEqual(link.nodes[1].y, 100)

    def test_apply_force(self):
        link = Link()
        link.add_node(0, 0, 'fixed')  # 固定された節点
        link.add_node(10, 0, 'free')  # 自由に動く節点
        force = (5, 0)  # X軸方向に5の力を適用
        link.apply_force(force, 1)  # 節点1に力を適用
        self.assertEqual(link.nodes[1].x, 15)  # 力が適用された後の位置をテスト
        self.assertEqual(link.nodes[1].y, 0)

if __name__ == '__main__':
    unittest.main()
