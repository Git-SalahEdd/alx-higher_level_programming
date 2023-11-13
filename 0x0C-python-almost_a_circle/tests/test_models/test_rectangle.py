#!/usr/bin/python3
"""
Module for the unittests of the class Rectangle
"""
import models.rectangle as r
import models.base as b
import unittest
from io import StringIO
from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    def test_module_doc(self):
        """
        Tests for the module doc
        """
        self.assertIsNotNone(r.__doc__)
        self.assertGreater(len(r.__doc__), 0)

    def test_class_doc(self):
        """
        Tests for the class doc
        """
        self.assertIsNotNone(r.Rectangle.__doc__)
        self.assertGreater(len(r.Rectangle.__doc__), 0)

    def test_init_doc(self):
        """
        Tests for the __init__ doc
        """
        self.assertIsNotNone(r.Rectangle.__init__.__doc__)
        self.assertGreater(len(r.Rectangle.__init__.__doc__), 0)

    def test_area_doc(self):
        """
        Tests for the area doc
        """
        self.assertIsNotNone(r.Rectangle.area.__doc__)
        self.assertGreater(len(r.Rectangle.area.__doc__), 0)

    def test_update_doc(self):
        """
        Tests for the update doc
        """
        self.assertIsNotNone(r.Rectangle.update.__doc__)
        self.assertGreater(len(r.Rectangle.update.__doc__), 0)

    def test_to_dictionary_doc(self):
        """
        Tests for the to_dictionary doc
        """
        self.assertIsNotNone(r.Rectangle.to_dictionary.__doc__)
        self.assertGreater(len(r.Rectangle.to_dictionary.__doc__), 0)

    def setUp(self):
        """
        Resets id
        """
        b.Base._Base__nb_objects = 0

    def test_display_doc(self):
        """
        Tests for the display doc
        """
        self.assertIsNotNone(r.Rectangle.display.__doc__)
        self.assertGreater(len(r.Rectangle.display.__doc__), 0)

    def test_private_attrs(self):
        """
        Tests for private attributes
        """
        obj = r.Rectangle(1, 1)
        self.assertIn("id", obj.__dict__)
        self.assertIn("_Rectangle__width", obj.__dict__)
        self.assertNotIn("width", obj.__dict__)
        self.assertIn("_Rectangle__height", obj.__dict__)
        self.assertNotIn("height", obj.__dict__)
        self.assertIn("_Rectangle__x", obj.__dict__)
        self.assertNotIn("x", obj.__dict__)
        self.assertIn("_Rectangle__y", obj.__dict__)
        self.assertNotIn("y", obj.__dict__)

    def test_default(self):
        """
        Tests for default values
        """
        obj = r.Rectangle(1, 2)
        self.assertEqual(obj.width, 1)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 0)
        self.assertEqual(obj.y, 0)
        self.assertIsNotNone(obj.id)

    def test_all(self):
        """
        Tests for all values
        """
        obj = r.Rectangle(3, 2, 3, 4, 5)
        self.assertEqual(obj.width, 3)
        self.assertEqual(obj.height, 2)
        self.assertEqual(obj.x, 3)
        self.assertEqual(obj.y, 4)
        self.assertIsNotNone(obj.id)
        self.assertEqual(obj.id, 5)

    def test_setter(self):
        """
        Tests for setter
        """
        obj = r.Rectangle(1, 2)
        obj.width = 11
        self.assertEqual(obj.width, 11)
        obj.height = 12
        self.assertEqual(obj.height, 12)
        obj.x = 13
        self.assertEqual(obj.x, 13)
        obj.y = 14
        self.assertEqual(obj.y, 14)
        obj.id = 15
        self.assertEqual(obj.id, 15)

    def test_no_args(self):
        """
        Tests for no arguments
        """
        with self.assertRaises(TypeError) as err:
            r.Rectangle()
        self.assertEqual(
            str(err.exception),
            "__init__() missing 2 required positional arguments: 'width' and 'height'",
        )
        with self.assertRaises(TypeError) as err:
            r.Rectangle(1)
        self.assertEqual(
            str(err.exception),
            "__init__() missing 1 required positional argument: 'height'",
        )

    def test_too_many_args(self):
        """
        Tests for too many arguments
        """
        with self.assertRaises(TypeError) as err:
            r.Rectangle(1, 2, 3, 4, 5, 6)
        self.assertEqual(
            str(err.exception),
            "__init__() takes from 3 to 6 positional arguments but 7 were given",
        )

    def test_width_validation(self):
        """
        Tests for width validation
        """
        with self.assertRaises(TypeError) as err:
            r.Rectangle(True, 1)
            r.Rectangle("Hola", 1)
            r.Rectangle([1, 2], 1)
            r.Rectangle(1.2, 1)
            r.Rectangle(float("inf"), 1)
            r.Rectangle(float("nan"), 1)
        self.assertEqual(str(err.exception), "width must be an integer")
        with self.assertRaises(ValueError) as err:
            r.Rectangle(0, 1)
            r.Rectangle(-1, 1)
        self.assertEqual(str(err.exception), "width must be > 0")

    def test_height_validation(self):
        """
        Tests for heigth validation
        """
        with self.assertRaises(TypeError) as err:
            r.Rectangle(1, True)
            r.Rectangle(1, "Hola")
            r.Rectangle(1, [1, 2])
            r.Rectangle(1, 1.2)
            r.Rectangle(1, float("inf"))
            r.Rectangle(1, float("nan"))
        self.assertEqual(str(err.exception), "height must be an integer")
        with self.assertRaises(ValueError) as err:
            r.Rectangle(1, 0)
            r.Rectangle(1, -1)
        self.assertEqual(str(err.exception), "height must be > 0")

    def test_x_validation(self):
        """
        Tests for x validation
        """
        obj = r.Rectangle(1, 1)
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
        obj = r.Rectangle(1, 1)
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
        self.assertEqual(r.Rectangle(1, 1).area(), 1)
        self.assertEqual(r.Rectangle(2, 5).area(), 10)
        self.assertEqual(r.Rectangle(5, 4, 3).area(), 20)
        self.assertEqual(r.Rectangle(5, 5, 4, 3).area(), 25)
        self.assertEqual(r.Rectangle(1, 2, 3, 4, 5).area(), 2)

    def test_display_without_location(self):
        """
        Tests for display without location
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            r.Rectangle(1, 1).display()
            self.assertEqual(fo.getvalue(), "#\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            r.Rectangle(1, 2).display()
            self.assertEqual(fo.getvalue(), "#\n#\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            r.Rectangle(2, 2).display()
            self.assertEqual(fo.getvalue(), "##\n##\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            r.Rectangle(4, 6).display()
            self.assertEqual(fo.getvalue(), "####\n####\n####\n####\n####\n####\n")

    def test_str(self):
        """
        Tests for str and print
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            print(r.Rectangle(3, 2))
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 0/0 - 3/2\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            print(r.Rectangle(1, 2, 3, 4, 5))
            self.assertEqual(fo.getvalue(), "[Rectangle] (5) 3/4 - 1/2\n")

    def test_display_with_location(self):
        """
        Tests for display with location
        """
        with patch("sys.stdout", new=StringIO()) as fo:
            r.Rectangle(3, 3, 1, 1).display()
            self.assertEqual(fo.getvalue(), "\n ###\n ###\n ###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            r.Rectangle(3, 3, 0, 1).display()
            self.assertEqual(fo.getvalue(), "\n###\n###\n###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            r.Rectangle(3, 3, 1, 0).display()
            self.assertEqual(fo.getvalue(), " ###\n ###\n ###\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            r.Rectangle(3, 3, 3, 3).display()
            self.assertEqual(fo.getvalue(), "\n\n\n   ###\n   ###\n   ###\n")

    def test_update_args(self):
        """
        Tests for update with *args
        """
        obj = r.Rectangle(10, 10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update()
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (10) 10/10 - 10/10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(1)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 10/10 - 10/10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(1, 2)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 10/10 - 2/10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(1, 2, 3)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 10/10 - 2/3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(1, 2, 3, 4)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 4/10 - 2/3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(1, 2, 3, 4, 5)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 4/5 - 2/3\n")

    def test_update_re_args(self):
        """
        Tests for reupdate with *args
        """
        obj = r.Rectangle(10, 10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(2, 5, 30, 19, 45)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (2) 19/45 - 5/30\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(4, 28, 12, 3, 98)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (4) 3/98 - 28/12\n")

    def test_update_kwargs_1(self):
        """
        Tests for update with **kwargs pt. 1
        """
        obj = r.Rectangle(10, 10, 10, 10, 10)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(x=4)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (10) 4/10 - 10/10\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(height=3)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (10) 4/10 - 10/3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(id=1)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 4/10 - 10/3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(y=5)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 4/5 - 10/3\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(width=2)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 4/5 - 2/3\n")

    def test_update_kwargs_multiple(self):
        """
        Tests for update with **kwargs pt. 2
        """
        dictionary = {"x": 30, "y": 40}
        obj = r.Rectangle(10, 20)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(**dictionary)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (1) 30/40 - 10/20\n")
        dictionary = {"id": 89, "width": 97, "height": 21, "x": 65, "y": 0}
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(**dictionary)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (89) 65/0 - 97/21\n")
        dictionary = {"width": 89, "height": 97, "y": 21, "id": 65, "x": 0}
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(**dictionary)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (65) 0/21 - 89/97\n")

    def test_update_mix(self):
        """
        Tests for update with mix
        """
        obj = r.Rectangle(10, 20)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(69, y=30)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (69) 0/0 - 10/20\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(69, id=30)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (69) 0/0 - 10/20\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(69, 12, 19, 34, 77, y=30)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (69) 34/77 - 12/19\n")
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(69, 12, 19, 34, 77, id=30, width=22, height=21, x=11, y=13)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (69) 34/77 - 12/19\n")
        obj = r.Rectangle(10, 20)
        with patch("sys.stdout", new=StringIO()) as fo:
            obj.update(69, id=30, width=22, height=21, x=11, y=13)
            print(obj)
            self.assertEqual(fo.getvalue(), "[Rectangle] (69) 0/0 - 10/20\n")

    def test_to_dictionary(self):
        """
        Tests for to dictionary pt.1
        """
        test_dict = {"id": 1, "width": 1, "height": 2, "x": 0, "y": 0}
        obj_dict = r.Rectangle(1, 2).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())

    def test_to_dictionary_2(self):
        """
        Tests for to dictionary pt. 2
        """
        test_dict = {"id": 1, "width": 1, "height": 2, "x": 3, "y": 0}
        obj_dict = r.Rectangle(1, 2, 3).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())

    def test_to_dictionary_3(self):
        """
        Tests for to dictionary pt. 3
        """
        test_dict = {"id": 1, "width": 1, "height": 2, "x": 3, "y": 4}
        obj_dict = r.Rectangle(1, 2, 3, 4).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())

    def test_to_dictionary_4(self):
        """
        Tests for to dictionary pt. 4
        """
        test_dict = {"id": 5, "width": 1, "height": 2, "x": 3, "y": 4}
        obj_dict = r.Rectangle(1, 2, 3, 4, 5).to_dictionary()
        self.assertIsInstance(obj_dict, dict)
        self.assertCountEqual(test_dict.keys(), obj_dict.keys())
        self.assertCountEqual(test_dict.values(), obj_dict.values())


if __name__ == "__main__":
    unittest.main()
