#!/usr/bin/python3
"""
Test file for the base_mode class
"""

import os
import time
import json
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import models


class TestClass(unittest.TestCase):
    """Test cases"""
    def setUp(self):
        self.model = BaseModel()
        return super().setUp()

    def test_create_istance(self):
        """ Test case init instance"""
        self.assertIsInstance(self.model, BaseModel)

    def test_save(self):
        self.model.save()

        file = 'file.json'
        with open(file, mode="r+", encoding="utf-8") as f:
            file_string = f.read()
            data = json.loads(file_string)

        self.assertTrue('{}.{}'.format(type(self.model).__name__,
                        self.model.id) in data)

        self.assertDictEqual(
            self.model.to_dict(),
            data['{}.{}'.format(type(self.model).__name__, self.model.id)]
            )

    def test_assign_attribute(self):
        """ Test new attribute"""
        self.model.name = "Holberton"
        self.model.my_number = 89
        self.assertIs(self.model.name, "Holberton")
        self.assertIs(self.model.my_number, 89)

    def test_create_instance_from_dict(self):
        """create an instance using dictionary"""
        model_dict = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                      'created_at': '2017-09-28T21:03:54.052298',
                      '__class__': 'BaseModel', 'my_number': 89,
                      'updated_at': '2017-09-28T21:03:54.052302',
                      'name': 'Holberton'}

        my_model = BaseModel(**model_dict)
        self.assertIsInstance(my_model, BaseModel)
        self.assertEqual(my_model.id,
                         "56d43177-cc5f-4d6c-a0c1-e167f8c27337")
        self.assertEqual(my_model.name, "Holberton")

    def test_to_dict_success(self):

        self.model.name = "Holberton"
        self.model.my_number = 89
        my_model_json = self.model.to_dict()

        self.assertDictEqual(my_model_json, {
            'id': self.model.id,
            'created_at': self.model.created_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f'),
            'updated_at': self.model.updated_at.strftime(
                '%Y-%m-%dT%H:%M:%S.%f'),
            'name': self.model.name,
            'my_number': self.model.my_number,
            '__class__': BaseModel.__name__})

    def test_init(self):
        """test basemodel init"""
        snapshot = datetime.now()
        bm1 = BaseModel()
        snapshot2 = datetime.now()

        self.assertIsInstance(bm1.id, str)
        self.assertTrue(len(bm1.id) > 0)
        self.assertTrue('BaseModel.' + bm1.id in storage.all().keys())

        self.assertIsInstance(bm1.created_at, datetime)
        self.assertLess(bm1.created_at, snapshot2)
        self.assertGreater(bm1.created_at, snapshot)

        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertLess(bm1.updated_at, snapshot2)
        self.assertGreater(bm1.updated_at, snapshot)

        bm1.save()
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertGreater(bm1.updated_at, snapshot)
        self.assertGreater(bm1.updated_at, snapshot2)
        del bm1

    def test_init_dict(self):
        """test Basemodel dict init"""
        test_dict = {'updated_at': datetime(2022, 5, 22, 12, 30, 00, 716921)
                     .isoformat('T'),
                     'id': '5361a11b-615c-42bf-9bdb-e2c3790ada14',
                     'created_at': datetime(2022, 5, 22, 12, 30, 00, 716921)
                     .isoformat('T')}
        bm2 = BaseModel(**test_dict)

        self.assertIsInstance(bm2.id, str)
        self.assertTrue(len(bm2.id) > 0)
        self.assertTrue(bm2.id == test_dict['id'])

        self.assertIsInstance(bm2.created_at, datetime)
        self.assertTrue(bm2.created_at.isoformat('T') == test_dict
                        ['created_at'])
        self.assertIsInstance(bm2.updated_at, datetime)
        self.assertTrue(bm2.updated_at.isoformat('T') == test_dict
                        ['updated_at'])
        bm2.save()
        self.assertGreater(bm2.updated_at, bm2.created_at)
        del bm2


if __name__ == '__main__':
    unittest.main()
