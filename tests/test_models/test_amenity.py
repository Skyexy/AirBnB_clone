#!/usr/bin/python3
"""
unittest for Amenity
"""

import os
import time
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
from datetime import datetime
from models import storage


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_create_istance(self):
        """create a new instance"""
        new_state = Amenity()
        self.assertIsInstance(new_state, Amenity)

    def test_create_istance2(self):
        """create a new instance"""
        new_state = Amenity()
        self.assertIsInstance(new_state, BaseModel)

    def test_init(self):
        """test amenity init"""
        snapshot1 = datetime.now()
        am1 = Amenity()
        snapshot2 = datetime.now()

        self.assertIsInstance(am1.id, str)
        self.assertTrue(len(am1.id) > 0)
        self.assertTrue('Amenity.' + am1.id in storage.all().keys())

        self.assertIsInstance(am1.created_at, datetime)
        self.assertLess(am1.created_at, snapshot2)
        self.assertGreater(am1.created_at, snapshot1)

        self.assertIsInstance(am1.updated_at, datetime)
        self.assertLess(am1.updated_at, snapshot2)
        self.assertGreater(am1.updated_at, snapshot1)

        am1.save()
        self.assertIsInstance(am1.updated_at, datetime)
        self.assertGreater(am1.updated_at, snapshot1)
        self.assertGreater(am1.updated_at, snapshot2)
        del am1

    def test_attribute(self):
        """test attribute"""
        am2 = Amenity()

        self.assertTrue(hasattr(am2, "name"))
        self.assertIsInstance(am2.name, str)

    def test_init_dict(self):
        """test basemodel dict init"""
        test_dict = {'updated_at': datetime(2022, 11, 22, 12, 30, 00, 716921)
                     .isoformat('T'),
                     'id': '5361a11b-615c-42bf-9bdb-e2c3790ada14',
                     'created_at': datetime(2022, 11, 22, 12, 30, 00, 716921)
                     .isoformat('T')}
        am3 = Amenity(**test_dict)

        self.assertIsInstance(am3.id, str)
        self.assertTrue(len(am3.id) > 0)
        self.assertTrue(am3.id == test_dict['id'])

        self.assertIsInstance(am3.created_at, datetime)
        self.assertTrue(am3.created_at.isoformat('T') == test_dict
                        ['created_at'])
        self.assertIsInstance(am3.updated_at, datetime)
        self.assertTrue(am3.updated_at.isoformat('T') == test_dict
                        ['updated_at'])
        am3.save()
        self.assertGreater(am3.updated_at, am3.created_at)
        del am3


if __name__ == '__main__':
    unittest.main()
