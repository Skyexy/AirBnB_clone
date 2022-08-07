#!/usr/bin/python3
"""
Test file for city class
"""

import os
import time
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestClass(unittest.TestCase):
    """Test cases"""

    def setUp(self):
        self.city = City()
        return super().setUp()

    def tearDown(self):
        del(self.city)
        return super().tearDown()

    def test_create_istance(self):
        """create a new instance"""
        self.assertIsInstance(self.city, City)

    def test_create_istance_check_parent(self):
        """check if it's instance of parent"""
        self.assertIsInstance(self.city, BaseModel)

    def test_class_attribut(self):
        """initialze class attribute"""
        self.city.name = "kigali"
        self.assertIs(self.city.name, 'kigali')
    def test_id(self):
        """initialze class attribute"""
        self.city.state_id = "kigali"
        self.assertIs(self.city.state_id, 'kigali')

        cm = City()

        self.assertTrue(hasattr(cm, "state_id"))
        self.assertTrue(hasattr(cm, "name"))

        self.assertIsInstance(cm.state_id, str)
        self.assertIsInstance(cm.name, st)

    def test_id(self):
        """Initialze class attribute"""
        self.city.state_id = "Kigali"
        self.assertIs(self.city.state_id, 'Kigali')

    def test_parent_of_city(self):
        """check if city is parent of BaseModel"""
        self.assertEqual(isinstance(self.city, BaseModel), True)

    def test_init(self):
        """test init"""
        snapshot1 = datetime.now()
        cm1 = City()
        snapshot2 = datetime.now()

        self.assertIsInstance(cm1.id, str)
        self.assertTrue(len(cm1.id) > 0)
        self.assertTrue('City.' + cm1.id in storage.all().keys())

        self.assertIsInstance(cm1.created_at, datetime)
        self.assertLess(cm1.created_at, snapshot2)
        self.assertGreater(cm1.created_at, snapshot1)

        self.assertIsInstance(cm1.updated_at, datetime)
        self.assertLess(cm1.updated_at, snapshot2)
        self.assertGreater(cm1.updated_at, snapshot1)

        cm1.save()
        self.assertIsInstance(cm1.updated_at, datetime)
        self.assertGreater(cm1.updated_at, snapshot1)
        self.assertGreater(cm1.updated_at, snapshot2)
        del cm1

    def test_init_dict(self):
        """test basemodel init"""
        test_dict = {'updated_at': datetime(2022, 5, 22, 12, 30, 00, 716921)
                     .isoformat('T'),
                     'id': '5361a11b-615c-42bf-9bdb-e2c3790ada14',
                     'created_at': datetime(2022, 5, 22, 12, 30, 00, 716921)
                     .isoformat('T')}
        cm2 = City(**test_dict)

        self.assertIsInstance(cm2.id, str)
        self.assertTrue(len(cm2.id) > 0)
        self.assertTrue(cm2.id == test_dict['id'])

        self.assertIsInstance(cm2.created_at, datetime)
        self.assertTrue(cm2.created_at.isoformat('T') == test_dict
                        ['created_at'])
        self.assertIsInstance(cm2.updated_at, datetime)
        self.assertTrue(cm2.updated_at.isoformat('T') == test_dict
                        ['updated_at'])
        cm2.save()
        self.assertGreater(cm2.updated_at, cm2.created_at)
        del cm2


if __name__ == '__main__':
    unittest.main()
