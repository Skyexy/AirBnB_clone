#!/usr/bin/python3
"""
Test file for user class
"""

import os
import time
import unittest
from models.place import Place
from models.base_model import BaseModel
from models import storage
from datetime import datetime


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_init(self):
        """test init"""
        snapshot1 = datetime.now()
        pm = Place()
        snapshot2 = datetime.now()

        self.assertIsInstance(pm.id, str)
        self.assertTrue(len(pm.id) > 0)
        self.assertTrue('Place.' + pm.id in storage.all().keys())

        self.assertIsInstance(pm.created_at, datetime)
        self.assertLess(pm.created_at, snapshot2)
        self.assertGreater(pm.created_at, snapshot1)

        self.assertIsInstance(pm.updated_at, datetime)
        self.assertLess(pm.updated_at, snapshot2)
        self.assertGreater(pm.updated_at, snapshot1)

        pm.save()
        self.assertIsInstance(pm.updated_at, datetime)
        self.assertGreater(pm.updated_at, snapshot1)
        self.assertGreater(pm.updated_at, snapshot2)
        del pm

    def test_init_dict(self):
        """test basemodel dict init"""
        test_dict = {'updated_at': datetime(2022, 11, 22, 12, 30, 00, 716921)
                     .isoformat('T'),
                     'id': '5361a11b-615c-42bf-9bdb-e2c3790ada14',
                     'created_at': datetime(2022, 11, 22, 12, 30, 00, 716921)
                     .isoformat('T')}
        pm2 = Place(**test_dict)

        self.assertIsInstance(pm2.id, str)
        self.assertTrue(len(pm2.id) > 0)
        self.assertTrue(pm2.id == test_dict['id'])

        self.assertIsInstance(pm2.created_at, datetime)
        self.assertTrue(pm2.created_at.isoformat('T') == test_dict
                        ['created_at'])
        self.assertIsInstance(pm2.updated_at, datetime)
        self.assertTrue(pm2.updated_at.isoformat('T') == test_dict
                        ['updated_at'])
        pm2.save()
        self.assertGreater(pm2.updated_at, pm2.created_at)
        del pm2

    def test_attribute(self):
        """test attributes"""
        pm3 = Place()

        self.assertTrue(hasattr(pm3, "city_id"))
        self.assertTrue(hasattr(pm3, "user_id"))
        self.assertTrue(hasattr(pm3, "name"))
        self.assertTrue(hasattr(pm3, "description"))
        self.assertTrue(hasattr(pm3, "number_rooms"))
        self.assertTrue(hasattr(pm3, "number_bathrooms"))
        self.assertTrue(hasattr(pm3, "max_guest"))
        self.assertTrue(hasattr(pm3, "price_by_night"))
        self.assertTrue(hasattr(pm3, "latitude"))
        self.assertTrue(hasattr(pm3, "longitude"))
        self.assertTrue(hasattr(pm3, "amenity_ids"))

        self.assertIsInstance(pm3.city_id, str)
        self.assertIsInstance(pm3.user_id, str)
        self.assertIsInstance(pm3.name, str)
        self.assertIsInstance(pm3.description, str)
        self.assertIsInstance(pm3.number_rooms, int)
        self.assertIsInstance(pm3.number_bathrooms, int)
        self.assertIsInstance(pm3.max_guest, int)
        self.assertIsInstance(pm3.price_by_night, int)
        self.assertIsInstance(pm3.latitude, float)
        self.assertIsInstance(pm3.longitude, float)
        self.assertIsInstance(pm3.amenity_ids, list)

    def test_create_istance(self):
        """create a new instance"""
        new_place = Place()
        self.assertIsInstance(new_place, Place)

    def test_create_istance2(self):
        """create a new instance"""
        new_place = Place()
        self.assertIsInstance(new_place, BaseModel)


if __name__ == '__main__':
    unittest.main()
