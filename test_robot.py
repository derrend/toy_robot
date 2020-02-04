import unittest
from robot import LocationError, Robot

class TestRobot(unittest.TestCase):
    def test_location(self):
        r = Robot()
        self.assertRaises(LocationError, r.move)
        self.assertRaises(LocationError, r.left)
        self.assertRaises(LocationError, r.right)
        self.assertRaises(LocationError, r.report)

    def test_place(self):
        r = Robot()
        self.assertRaises(ValueError, r.place, 6, 0, 'NORTH')
        self.assertRaises(ValueError, r.place, 0, 6, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, 0, 6)

        self.assertRaises(ValueError, r.place, -1, 0, 'NORTH')
        self.assertRaises(ValueError, r.place, 0, -1, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, 0, -1)

        self.assertRaises(TypeError, r.place, 5j, 0, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, 5j, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, 0, 5j)

        self.assertRaises(TypeError, r.place, 2.5, 0, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, 2.5, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, 0, 2.5)

        self.assertRaises(TypeError, r.place, 'hello', 0, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, 'hello', 'NORTH')
        self.assertRaises(ValueError, r.place, 0, 0, 'hello')

        self.assertRaises(TypeError, r.place, None, 0, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, None, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, 0, None)

        self.assertRaises(TypeError, r.place, True, 0, 'NORTH')
        self.assertRaises(TypeError, r.place, False, 0, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, True, 'NORTH')
        self.assertRaises(TypeError, r.place, 0, False, 'NORTH')

        self.assertRaises(TypeError, r.place, 0, 0, True)
        self.assertRaises(TypeError, r.place, 0, 0, False)

    def test_move(self):
        r = Robot()
        r.place(0, 5, 'NORTH')
        self.assertRaises(ValueError, r.move)
        r.place(5, 0, 'EAST')
        self.assertRaises(ValueError, r.move)
        r.place(0, 0, 'SOUTH')
        self.assertRaises(ValueError, r.move)
        r.place(0, 0, 'WEST')
        self.assertRaises(ValueError, r.move)

    def test_left(self):
        r = Robot()
        r.place()
        self.assertEqual(r.report()['F'], 'NORTH')
        r.left()
        self.assertEqual(r.report()['F'], 'WEST')
        r.left()
        self.assertEqual(r.report()['F'], 'SOUTH')
        r.left()
        self.assertEqual(r.report()['F'], 'EAST')
        r.left()
        self.assertEqual(r.report()['F'], 'NORTH')

    def test_right(self):
        r = Robot()
        r.place()
        self.assertEqual(r.report()['F'], 'NORTH')
        r.right()
        self.assertEqual(r.report()['F'], 'EAST')
        r.right()
        self.assertEqual(r.report()['F'], 'SOUTH')
        r.right()
        self.assertEqual(r.report()['F'], 'WEST')
        r.right()
        self.assertEqual(r.report()['F'], 'NORTH')

    def test_report(self):
        r = Robot()
        r.place()
        self.assertDictEqual(r.report(), dict(X=0, Y=0, F='NORTH'))
