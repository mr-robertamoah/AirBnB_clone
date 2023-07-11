#!/usr/bin/python3

"""
Test module for base_model module
"""


from models.base_model import BaseModel
import unittest
from datetime import datetime
import io
import sys


class TestBaseModel(unittest.TestCase):
    """ A TestCase class that tests the BaseModel class """

    def test_initialization(self):
        """ test the initialization of the BaseModel class """

        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

        with self.assertRaises(TypeError):
            model = BaseModel("name")

    def test_save_instance_method(self):
        """ test the save instance method of the BaseModel class """

        model = BaseModel()
        date1 = model.updated_at
        model.save()
        date2 = model.updated_at
        self.assertNotEqual(date1, date2)

    def test_to_dict_instance_method(self):
        """ test the to_dict instance method of the BaseModel Class """

        model = BaseModel()
        m_dict = model.to_dict()
        m_dict_keys = {"__class__", "id", "created_at", "updated_at"}
        self.assertIsInstance(m_dict, dict)
        self.assertSetEqual(set(m_dict.keys()), m_dict_keys)
        self.assertIsInstance(m_dict["id"], str)
        self.assertIsInstance(m_dict["created_at"], str)
        self.assertIsInstance(m_dict["updated_at"], str)

        model = BaseModel()
        model.name = "John"
        model.age = 50
        m_dict = model.to_dict()
        m_dict_keys = {"__class__", "id", "created_at", "updated_at", "name", "age"}
        self.assertIsInstance(m_dict, dict)
        self.assertSetEqual(set(m_dict.keys()), m_dict_keys)
        self.assertIsInstance(m_dict["name"], str)
        self.assertIsInstance(m_dict["age"], int)

        with self.assertRaises(TypeError):
            m_dict = model.to_dict("argument")

    def test_str_representation(self):
        """ test the __str__ function of the BaseModel """

        model = BaseModel()
        new_stdout = io.StringIO()
        sys.stdout = new_stdout

        print(model)

        m_str = new_stdout.getvalue()
        self.assertIn("[BaseModel]", m_str)
        self.assertIn("'id': ", m_str)
        self.assertIn("'created_at': datetime.datetime", m_str)
        self.assertIn("'updated_at': datetime.datetime", m_str)
        sys.stdout = sys.__stdout__
