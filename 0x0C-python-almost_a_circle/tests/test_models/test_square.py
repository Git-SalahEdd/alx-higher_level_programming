#!/usr/bin/python3
"""
Module for the unittest of the class Square
"""
import models.square as s
import models.rectangle as r
import models.base as b
import unittest
from io import StringIO
from unittest.mock import patch


class TestSquare(unittest.TestCase):
    """
    class TestSquare
    """

    def test_module_doc(self):
        """
        Tests for module doc
        """
        self.assertIsNotNone(s.__doc__)
        self.assertGreater(len(s.__doc__), 0)

    def test_class_doc(self):
        """
        Tests for class doc
        """
        self.assertIsNotNone(s.Square.__doc__)
        self.assertGreater(len(s.Square.__doc__), 0)

    def test_init_doc(self):
        """
        Tests for init doc
        """
        self.assertIsNotNone(s.Square.__init__.__doc__)
        self.assertGreater(len(s.Square.__init__.__doc__), 0)

    def test_update_doc(self):
        """
        Tests for update doc
        """
        self.assertIsNotNone(s.Square.update.__doc__)
        self.assertGreater(len(s.Square.update.__doc__), 0)

    def test_to_dictionary_doc(self):
        """
        Tests for to dictionary doc
        """
        self.assertIsNotNone(s.Square.to_dictionary.__doc__)
        self.assertGreater(len(s.Square.to_dictionary.__doc__), 0)

    def setUp(self):
        """
        Resets id
        """
        b.Base._Base__nb_objects = 0

    def test_no_new_attrs(self):
        """
        Tests for no new attributes
        """
        obj = s.Square(5)
        self.assertNotIn("size", obj.__dict__)
        self.assertNotIn("_Square__size", obj.__dict__)
        dictt = {
            "id": 0,
            "_Rectangle__width": 1,
            "_Rectangle__height": 1,
            "_Rectangle__x": 0,
            "_Rectangle__y": 0,
        }
        self.assertCountEqual(dictt, obj.__dict__)

    def test_no_args(self):
        """
        Tests for no arguments
        """
        with self.assertRaises(TypeError) as err:
            s.Square()
        self.assertEqual(
            str(err.exception),
            "__init__() missing 1 required positional argument: 'size'",
        )

    def test_too_many_args(self):
        """
        Tests for too many arguments
        """
        with self.assertRaises(TypeError) as err:
            s.Square(1, 2, 3, 4, 5, 6)
        self.assertEqual(
            str(err.exception),
            "__init__() takes from 2 to 5 positional arguments but 7 were given",
        )

    def test_size_validation(self):
        """
        Tests for size validation
        """
        with self.assertRaises(TypeError) as err:
            s.Square(True)
            s.Square("Hola")
            s.Square([1, 2])
            s.Square(1.2)
            s.Square(float("inf"))
            s.Square(float("nan"))
        self.assertEqual(str(err.exception), "width must be an integer")
        with self.assertRaises(ValueError) as err:
            s.Square(0)
            s.Square(-1)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_x_validation(self):
        """
        Tests for x validation
        """
        obj = s.Square(1)
        with self.assertRaises(TypeError) as err:
            obj.x = True
            obj.x = "Hola"
            obj.x = {}
            obj.x = 1.2
            obj.x = [1]
            obj.x = float("inf")
            obj.x = float("nan")
        self.assertEqual(str(err.exception), "x must be an integer")
        with self.assertRaises(ValueError) as err:
            obj.x = -1
        self.assertEqual(str(err.exception), "x must be >= 0")

    def test_y_validation(self):
        """
        Tests for y validation
        """
        obj = s.Square(1, 1)
        with self.assertRaises(TypeError) as err:
            obj.y = True
            obj.y = "Hola"
            obj.y = {}
            obj.y = 1.2
            obj.y = [1]
            obj.y = float("inf")
            obj.y = float("nan")
        self.assertEqual(str(err.exception), "y must be an integer")
        with self.assertRaises(ValueError) as err:
            obj.y = -1
        self.assertEqual(str(err.exception), "y must be >= 0")

    def test_area(self):
        """
        Tests for area
        """
        self.assertEqual(s.Square(1).area(), 1)
        self.assertEqual(s.Square(2, 5).area(), 4)
        self.assertEqual(s.Square(5, 4, 3).area(), 25)
        self.assertEqual(s.Square(3, 5, 4, 8).area(), 9)

    def test_display_without_location(self):
        """
        Tests for display without location
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            s.Square(1).display()
            self.assertEqual(fo.getvalue(), "#\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            s.Square(2).display()
            self.assertEqual(fo.getvalue(), "##\n##\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            s.Square(4).display()
            self.assertEqual(fo.getvalue(), "####\n####\n####\n####\n")

    def test_str(self):
        """
        Tests for str or print
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            print(s.Square(3))
            self.assertEqual(fo.getvalue(), "[Square] (1) 0/0 - 3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            print(s.Square(2, 3, 4, 5))
            self.assertEqual(fo.getvalue(), "[Square] (5) 3/4 - 2\n")

    def test_display_with_location(self):
        """
        Tests for display with location
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            s.Square(3, 1, 1).display()
            self.assertEqual(fo.getvalue(), "\n ###\n ###\n ###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            s.Square(3, 0, 1).display()
            self.assertEqual(fo.getvalue(), "\n###\n###\n###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            s.Square(3, 1, 0).display()
            self.assertEqual(fo.getvalue(), " ###\n ###\n ###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            s.Square(3, 3, 3).display()
            self.assertEqual(fo.getvalue(), "\n\n\n   ###\n   ###\n   ###\n")

    def test_size_setter_and_getter(self):
        """
        Tests for size setter and getter
        """
        obj = s.Square(3)
        self.assertEqual(obj.size, 3)
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 3)
        obj.size = 18
        self.assertEqual(obj.size, 18)
        self.assertEqual(obj.width, 18)
        self.assertEqual(obj.height, 18)

    def test_update_args(self):
        """
        Tests for update with *args
        """
        obj = s.Square(10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update()
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (10) 10/10 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(1)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (1) 10/10 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(1, 2)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (1) 10/10 - 2\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(1, 2, 3, 4)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (1) 3/4 - 2\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(1, 2, 4, 5)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (1) 4/5 - 2\n")

    def test_update_re_args(self):
        """
        Tests for reupdate with *args
        """
        obj = s.Square(10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(2, 5, 19, 45)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (2) 19/45 - 5\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(4, 12, 3, 98)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (4) 3/98 - 12\n")

    def test_update_kwargs_1(self):
        """
        Tests for update with **kwargs
        """
        obj = s.Square(10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(x=4)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (10) 4/10 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(id=1)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (1) 4/10 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(y=5)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (1) 4/5 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(width=2)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (1) 4/5 - 2\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(size=8)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (1) 4/5 - 8\n")

    def test_update_kwargs_multiple(self):
        """
        Tests for update with multiple **kwargs
        """
        dictionary = {"x": 30, "y": 40}
        obj = s.Square(20)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(**dictionary)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (1) 30/40 - 20\n")
        dictionary = {"id": 89, "size": 21, "x": 65, "y": 0}
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(**dictionary)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (89) 65/0 - 21\n")
        dictionary = {"id": 89, "width": 21, "x": 65, "y": 0}
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(**dictionary)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (89) 65/0 - 21\n")
        dictionary = {"size": 89, "y": 21, "id": 65, "x": 0}
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(**dictionary)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (65) 0/21 - 89\n")

    def test_update_mix(self):
        """
        Tests for mix
        """
        obj = s.Square(10)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(69, y=30)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (69) 0/0 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(69, id=30)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (69) 0/0 - 10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(69, 12, 34, 77, y=30)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (69) 34/77 - 12\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(69, 12, 19, 34, id=30, size=22, x=11, y=13)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (69) 19/34 - 12\n")
        obj = s.Square(20)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(69, id=30, size=22, x=11, y=13)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Square] (69) 0/0 - 20\n")

    def test_to_dictionary(self):
        """
        Tests for to dictionary pt. 1
        """
        test_dict = {"id": 1, "size": 1, "x": 0, "y": 0}
        obj_dict = s.Square(1).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())

    def test_to_dictionary_2(self):
        """
        Tests for to dictionary pt. 2
        """
        test_dict = {"id": 1, "size": 1, "x": 3, "y": 0}
        obj_dict = s.Square(1, 3).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())

    def test_to_dictionary_3(self):
        """
        Tests for to dictionary pt. 3
        """
        test_dict = {"id": 1, "size": 1, "x": 3, "y": 4}
        obj_dict = s.Square(1, 3, 4).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())

    def test_to_dictionary_4(self):
        """
        Tests for to dictionary pt. 4
        """
        test_dict = {"id": 5, "size": 1, "x": 3, "y": 4}
        obj_dict = s.Square(1, 3, 4, 5).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())


if __name__ == "__main__":
    unittest.main()
