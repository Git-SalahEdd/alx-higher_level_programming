#!/usr/bin/python3
"""
Module for the uniitest of the class Base
"""
import models.base as b
import models.rectangle as r
import models.square as s
import unittest
import os


class TestBase(unittest.TestCase):
    """
    class TestBase
    """

    def test_module_doc(self):
        """
        Tests for the module doc
        """
        self.assertIsNotNone(b.__doc__)
        self.assertGreater(len(b.__doc__), 0)

    def test_class_doc(self):
        """
        Tests for the class doc
        """
        self.assertIsNotNone(b.Base.__doc__)
        self.assertGreater(len(b.Base.__doc__), 0)

    def test_method_doc(self):
        """
        Tests for the __init__ doc
        """
        self.assertIsNotNone(b.Base.__init__.__doc__)
        self.assertGreater(len(b.Base.__init__.__doc__), 0)

    def test_to_json_string_doc(self):
        """
        Tests for the to json string doc
        """
        self.assertIsNotNone(b.Base.to_json_string.__doc__)
        self.assertGreater(len(b.Base.to_json_string.__doc__), 0)

    def setUp(self):
        """
        Resets counter and create a temporary directory for test files
        """
        b.Base._Base__nb_objects = 0

    def test_base_id_incr(self):
        """
        Tests for for base id inctrementation
        """
        b1 = b.Base()
        b2 = b.Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_id_None(self):
        """
        Tests for None id
        """
        b1 = b.Base(None)
        b2 = b.Base()
        self.assertEqual(b1.id, b2.id - 1)

    def test_private_attribute(self):
        """
        Tests for private attributes
        """
        with self.assertRaises(AttributeError):
            b.Base(5).__nb_objects

    def test_id_True(self):
        """
        Tests id boolean
        """
        self.assertEqual(b.Base(True).id, True)

    def test_base_id_input(self):
        """
        Tests for id input
        """
        self.assertEqual(b.Base(89).id, 89)
        self.assertEqual(b.Base(-89).id, -89)
        self.assertEqual(b.Base(0).id, 0)

    def test_id_str(self):
        """
        Tests with str id
        """
        self.assertEqual(b.Base("Hola!").id, "Hola!")

    def test_more_args(self):
        """
        Tests for too many args
        """
        with self.assertRaises(TypeError):
            b.Base(5, 10)

    def test_base_id_mix(self):
        """
        Tests for both
        """
        self.assertEqual(b.Base(89).id, 89)
        self.assertEqual(b.Base().id, 1)
        self.assertEqual(b.Base(0).id, 0)
        self.assertEqual(b.Base().id, 2)
        self.assertEqual(b.Base().id, 3)
        self.assertEqual(b.Base(-1).id, -1)
        self.assertEqual(b.Base(4).id, 4)

    def test_to_json_string_empty(self):
        """
        Tests for empty input
        """
        result = b.Base.to_json_string([])
        self.assertIsInstance(result, str)
        self.assertEqual(result, "[]")

    def test_to_json_string_none(self):
        """
        Tests with none input
        """
        result = b.Base.to_json_string(None)
        self.assertIsInstance(result, str)
        self.assertEqual(result, "[]")

    def test_to_json_string(self):
        """
        Test with 1 dictionary
        """
        dictionaries = r.Rectangle(10, 7, 2, 8).to_dictionary()
        expected = str(dictionaries)
        result = b.Base.to_json_string(dictionaries)
        self.assertIsInstance(result, str)
        self.assertEqual(eval(result), eval(expected))

    def test_to_json_strings(self):
        """
        Test with multiple dictionaries
        """
        d_list = []
        d_list.append(r.Rectangle(10, 7, 2, 8).to_dictionary())
        d_list.append(r.Rectangle(8, 4).to_dictionary())
        d_list.append(r.Rectangle(8, 4).to_dictionary())
        expected = str(d_list)
        result = b.Base.to_json_string(d_list)
        self.assertIsInstance(result, str)
        self.assertEqual(eval(result), eval(expected))

    def test_save_to_file_none(self):
        """
        Tests save to file with none with rectangle
        """
        r.Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_none_2(self):
        """
        Tests save to file with none with sqaure
        """
        s.Square.save_to_file(None)
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_empty_list(self):
        """
        Tests save to file with empty list with rectangle
        """
        r.Rectangle.save_to_file([])
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_empty_list_2(self):
        """
        Tests save to file with none with sqaure
        """
        s.Square.save_to_file([])
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.assertEqual(file_contents, "[]")

    def test_save_to_file_1_inst_rec(self):
        """
        Tests save to file with 1 intsance of rectangle
        """
        obj = r.Rectangle(5, 3, 1, 6, 9)
        r.Rectangle.save_to_file([obj])
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        dictionary = obj.to_dictionary()
        self.assertEqual(file_contents, b.Base.to_json_string([dictionary]))

    def test_save_to_file_1_inst_squ(self):
        """
        Tests save to file with 1 intsance of square
        """
        obj = s.Square(3, 1, 6, 9)
        s.Square.save_to_file([obj])
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        dictionary = obj.to_dictionary()
        self.assertEqual(file_contents, b.Base.to_json_string([dictionary]))

    def test_save_to_file_multiple_rec(self):
        """
        Tests save to file with multiple instances of rectangle
        """
        d_list = []
        d_list.append(r.Rectangle(2, 1))
        d_list.append(r.Rectangle(55, 1, 0, 12, 98))
        d_list.append(r.Rectangle(2, 5, 13, 4))
        r.Rectangle.save_to_file(d_list)
        self.assertTrue(os.path.exists(os.path.join(".", "Rectangle.json")))
        with open("Rectangle.json", "r") as f:
            file_contents = f.read()
        self.setUp()
        r_list = []
        r_list.append(r.Rectangle(2, 1).to_dictionary())
        r_list.append(r.Rectangle(55, 1, 0, 12, 98).to_dictionary())
        r_list.append(r.Rectangle(2, 5, 13, 4).to_dictionary())
        self.assertEqual(file_contents, b.Base.to_json_string(r_list))

    def test_save_to_file_multiple_squ(self):
        """
        Tests save to file with multiple instances of square
        """
        d_list = []
        d_list.append(s.Square(2, 1))
        d_list.append(s.Square(1, 0, 12, 98))
        d_list.append(s.Square(2, 5, 13, 4))
        s.Square.save_to_file(d_list)
        self.assertTrue(os.path.exists(os.path.join(".", "Square.json")))
        with open("Square.json", "r") as f:
            file_contents = f.read()
        self.setUp()
        r_list = []
        r_list.append(s.Square(2, 1).to_dictionary())
        r_list.append(s.Square(1, 0, 12, 98).to_dictionary())
        r_list.append(s.Square(2, 5, 13, 4).to_dictionary())
        self.assertEqual(file_contents, b.Base.to_json_string(r_list))


class TestBase_from_json_string(unittest.TestCase):
    """Tests for from json method"""

    def test_type(self):
        list_input = [{"id": 5, "width": 12, "height": 6}]
        json_input = r.Rectangle.to_json_string(list_input)
        list_output = r.Rectangle.from_json_string(json_input)
        self.assertEqual(list, type(list_output))

    def test_in_out_r(self):
        list_input = [{"id": 5, "width": 12, "height": 6}]
        json_input = r.Rectangle.to_json_string(list_input)
        list_output = r.Rectangle.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_2_rect(self):
        list_input = [
            {"id": 5, "width": 12, "height": 6},
            {"x": 14, "id": 22, "width": 5, "height": 8, "y": 4},
        ]
        json_input = r.Rectangle.to_json_string(list_input)
        list_output = r.Rectangle.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_in_out_s(self):
        list_input = [{"id": 5, "size": 12, "y": 6}]
        json_input = s.Square.to_json_string(list_input)
        list_output = s.Square.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_2_square(self):
        list_input = [
            {"id": 5, "size": 12, "x": 6, "y": 22},
            {"x": 14, "id": 22, "size": 5, "y": 4},
        ]
        json_input = s.Square.to_json_string(list_input)
        list_output = s.Square.from_json_string(json_input)
        self.assertEqual(list_input, list_output)

    def test_None(self):
        self.assertEqual(b.Base.from_json_string(None), [])

    def test_no_args(self):
        with self.assertRaises(TypeError):
            b.Base.from_json_string()

    def test_wrong_input(self):
        with self.assertRaises(TypeError):
            b.Base.from_json_string([], 3)


class TestBase_create(unittest.TestCase):
    """Tests for the create method"""

    def test_create_original_r(self):
        r1 = r.Rectangle(2, 5, 14)
        r1_dict = r1.to_dictionary()
        r2 = r.Rectangle.create(**r1_dict)
        self.assertEqual(str(r1), "[Rectangle] ({}) 14/0 - 2/5".format(r1.id))

    def test_create_new_r(self):
        r1 = r.Rectangle(2, 5, 14)
        r1_dict = r1.to_dictionary()
        r2 = r.Rectangle.create(**r1_dict)
        self.assertEqual(str(r2), "[Rectangle] ({}) 14/0 - 2/5".format(r2.id))

    def test_2_not_equal_r(self):
        r1 = r.Rectangle(2, 5, 14)
        r1_dict = r1.to_dictionary()
        r2 = r.Rectangle.create(**r1_dict)
        self.assertIsNot(r2, r1)

    def test_2_not_equal2_r(self):
        r1 = r.Rectangle(2, 5, 14)
        r1_dict = r1.to_dictionary()
        r2 = r.Rectangle.create(**r1_dict)
        self.assertNotEqual(r2, r1)

    def test_create_original_s(self):
        s1 = s.Square(2, 5, 14)
        s_dict = s1.to_dictionary()
        s2 = s.Square.create(**s_dict)
        self.assertEqual(str(s1), "[Square] ({}) 5/14 - 2".format(s1.id))

    def test_create_new_s(self):
        s1 = s.Square(2, 5, 14)
        s_dict = s1.to_dictionary()
        s2 = s.Square.create(**s_dict)
        self.assertEqual(str(s2), "[Square] ({}) 5/14 - 2".format(s1.id))

    def test_2_not_equal_s(self):
        s1 = s.Square(2, 5, 14)
        s_dict = s1.to_dictionary()
        s2 = s.Square.create(**s_dict)
        self.assertIsNot(s2, s1)

    def test_2_not_equal2_s(self):
        s1 = s.Square(2, 5, 14)
        s_dict = s1.to_dictionary()
        s2 = s.Square.create(**s_dict)
        self.assertNotEqual(s2, s1)


class TestBase_load_from_file(unittest.TestCase):
    """Tests for the load from file method"""

    @classmethod
    def tearDown(self):
        files = ["r.Rectangle.json", "s.Square.json"]
        for f in files:
            try:
                os.remove(f)
            except FileNotFoundError:
                pass

    def test_load_1_r(self):
        r1 = r.Rectangle(2, 5, 14)
        r2 = r.Rectangle(10, 12, 5, 2, 1)
        r.Rectangle.save_to_file([r1, r2])
        list_output = r.Rectangle.load_from_file()
        self.assertEqual(str(r1), str(list_output[0]))

    def test_load_2_r(self):
        r1 = r.Rectangle(2, 5, 14)
        r2 = r.Rectangle(10, 12, 5, 2, 1)
        r.Rectangle.save_to_file([r1, r2])
        list_output = r.Rectangle.load_from_file()
        self.assertEqual(str(r2), str(list_output[1]))

    def test_type_r(self):
        r1 = r.Rectangle(2, 5, 14)
        r2 = r.Rectangle(10, 12, 5, 2, 1)
        r.Rectangle.save_to_file([r1, r2])
        list_output = r.Rectangle.load_from_file()
        self.assertTrue(all(type(obj)) == r.Rectangle for obj in list_output)

    def test_load_1_s(self):
        s1 = s.Square(2, 5, 14)
        s2 = s.Square(10, 12, 2, 1)
        s.Square.save_to_file([s1, s2])
        list_output = s.Square.load_from_file()
        self.assertEqual(str(s1), str(list_output[0]))

    def test_load_2_s(self):
        s1 = s.Square(2, 5, 14)
        s2 = s.Square(10, 5, 2, 1)
        s.Square.save_to_file([s1, s2])
        list_output = s.Square.load_from_file()
        self.assertEqual(str(s2), str(list_output[1]))

    def test_type_s(self):
        s1 = s.Square(2, 5, 14)
        s2 = s.Square(12, 5, 2, 1)
        s.Square.save_to_file([s1, s2])
        list_output = s.Square.load_from_file()
        self.assertTrue(all(type(obj)) == s.Square for obj in list_output)

    def test_more_args(self):
        with self.assertRaises(TypeError):
            b.Base.load_from_file([], 2)


if __name__ == "__main__":
    unittest.main()
