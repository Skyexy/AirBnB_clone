#!/usr/bin/python3
"""
Test file for user class
"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.review import Review
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_init(self):
        """test blank init"""
        snapshot = datetime.now()
        rm1 = Review()
        snapshot2 = datetime.now()

        self.assertIsInstance(rm1.id, str)
        self.assertTrue(len(rm1.id) > 0)
        self.assertTrue('Review.' + rm1.id in storage.all().keys())

        self.assertIsInstance(rm1.created_at, datetime)
        self.assertLess(rm1.created_at, snapshot2)
        self.assertGreater(rm1.created_at, snapshot)

        self.assertIsInstance(rm1.updated_at, datetime)
        self.assertLess(rm1.updated_at, snapshot2)
        self.assertGreater(rm1.updated_at, snapshot)

        rm1.save()
        self.assertIsInstance(rm1.updated_at, datetime)
        self.assertGreater(rm1.updated_at, snapshot)
        self.assertGreater(rm1.updated_at, snapshot2)
        del rm1

    def test_init_dict(self):
        """test basemodel dict init"""
        test_dict = {'updated_at': datetime(2022, 11, 06, 12, 30, 00, 716921)
                     .isoformat('T'),
                     'id': '5361a11b-615c-42bf-9bdb-e2c3790ada14',
                     'created_at': datetime(2022, 11, 06, 12, 30, 00, 716921)
                     .isoformat('T')}
        rm2 = City(**test_dict)

        self.assertIsInstance(rm2.id, str)
        self.assertTrue(len(rm2.id) > 0)
        self.assertTrue(rm2.id == test_dict['id'])

        self.assertIsInstance(rm2.created_at, datetime)
        self.assertTrue(rm2.created_at.isoformat('T') == test_dict
                        ['created_at'])
        self.assertIsInstance(rm.updated_at, datetime)
        self.assertTrue(rm2.updated_at.isoformat('T') == test_dict
                        ['updated_at'])
        rm2.save()
        self.assertGreater(rm2.updated_at, rm2.created_at)
        del rm2

    def test_attribute(self):
        """test attributes"""
        rm3 = Review()

        self.assertTrue(hasattr(rm3, "place_id"))
        self.assertTrue(hasattr(rm3, "user_id"))
        self.assertTrue(hasattr(rm3, "text"))

        self.assertIsInstance(rm3.place_id, str)
        self.assertIsInstance(rm3.user_id, str)
        self.assertIsInstance(rm3.text, str)

    def test_create_istance(self):
        """create a new instance"""
        new_state = Review()
        self.assertIsInstance(new_state, Review)

    def test_create_istance2(self):
        """create a new instance"""
        new_state = Review()
        self.assertIsInstance(new_state, BaseModel)


if __name__ == '__main__':
    unittest.main()
