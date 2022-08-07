#!/usr/bin/python3
"""
Test file for user class
"""

import os
import time
import unittest
from datetime import datetime
from models import storage
from models.user import User
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_create_instance(self):
        """create a new instance"""
        new_user = User()
        self.assertIsInstance(new_user, User)

    def test_create_instance2(self):
        """create a new instance"""
        new_user = User()
        self.assertIsInstance(new_user, BaseModel)

    def test_init(self):
        """test Basemodel init"""
        snapshot = datetime.now()
        um1 = User()
        snapshot2 = datetime.now()

        self.assertIsInstance(um1.id, str)
        self.assertTrue(len(um1.id) > 0)
        self.assertTrue('User.' + um1.id in storage.all().keys())

        self.assertIsInstance(um1.created_at, datetime)
        self.assertLess(um1.created_at, snapshot2)
        self.assertGreater(um1.created_at, snapshot)

        self.assertIsInstance(um1.updated_at, datetime)
        self.assertLess(um1.updated_at, snapshot2)
        self.assertGreater(um1.updated_at, snapshot)

        um1.save()
        self.assertIsInstance(um1.updated_at, datetime)
        self.assertGreater(um1.updated_at, snapshot)
        self.assertGreater(um1.updated_at, snapshot2)
        del um1

    def test_init_dict(self):
        """test basemodel dict init"""
        test_dict = {'updated_at': datetime(2022, 11, 22, 12, 30, 00, 716921)
                     .isoformat('T'),
                     'id': '5361a11b-615c-42bf-9bdb-e2c3790ada14',
                     'created_at': datetime(2022, 11, 22, 12, 30, 00, 716921)
                     .isoformat('T')}
        um2 = User(**test_dict)

        self.assertIsInstance(um2.id, str)
        self.assertTrue(len(um2.id) > 0)
        self.assertTrue(um2.id == test_dict['id'])

        self.assertIsInstance(um2.created_at, datetime)
        self.assertTrue(um2.created_at.isoformat('T') == test_dict
                        ['created_at'])
        self.assertIsInstance(um2.updated_at, datetime)
        self.assertTrue(um2.updated_at.isoformat('T') == test_dict
                        ['updated_at'])
        um2.save()
        self.assertGreater(um2.updated_at, um2.created_at)
        del um2

    def test_attribute(self):
        """test attribute"""
        um3 = User()

        self.assertTrue(hasattr(um3, "email"))
        self.assertTrue(hasattr(um3, "password"))
        self.assertTrue(hasattr(um3, "first_name"))
        self.assertTrue(hasattr(um3, "last_name"))

        self.assertIsInstance(um3.email, str)
        self.assertIsInstance(um3.password, str)
        self.assertIsInstance(um3.first_name, str)
        self.assertIsInstance(um3.last_name, str)


if __name__ == '__main__':
    unittest.main()
