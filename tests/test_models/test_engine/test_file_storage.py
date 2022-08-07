#!/usr/bin/python3
"""
unittest for file storage.
"""


import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class TestFileStorage(unittest.TestCase):
    """A test class to test file storage"""
    def test_all(self):
        """test all"""
        fs1 = FileStorage()
        list_all = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for exists in fs1.all().keys():
            list_all.append(fs1.all()[exists])
        for exists in list_all:
            del fs1.all()[exists.name]

        self.assertIsInstance(fs1.all(), dict)
        self.assertEqual(fs1.all(), {})
        bm1, bm2 = BaseModel(), BaseModel()
        fs1.new(bm1)
        fs1.new(bm2)
        self.assertEqual(fs1.all(), {'BaseModel.' + bm1.id: bm1,
                                     'BaseModel.' + bm2.id: bm2})
        del bm1, bm2, fs1

    def test_new(self):
        """ tests new """
        dic = {"id": "67460e74-02e3-11e8-b443-00163e990bdb",
               "__class__": "BaseModel",
               "updated_at": "2022-08-06T15:45:40.260793",
               "created_at": "2022-08-06T15:45:40.260752"}
        fs2 = FileStorage()
        list_all = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for exists in fs2.all().keys():
            list_all.append(fs2.all()[exists])
        for exists in list_all:
            del fs2.all()[exists.__class__.__name__ + '.' + exists.id]
        classes = [Amenity(**dic), BaseModel(**dic), City(**dic), Place(**dic),
                   Review(**dic), State(**dic), User(**dic)]

        for cls in classes:
            fs2.new(cls)
            self.assertIn(cls.__class__.__name__ + '.' + cls.id, fs2.all())

        for cls in classes:
            name = cls.__class__.__name__
            self.assertTrue(name + '.' + cls.id in fs2.all().keys())

        for i in range(len(fs2.all().keys())):
            self.assertIn(fs2.all()[list(fs2.all().keys())[i]], classes)

        for exists in classes:
            del exists
        del fs2
