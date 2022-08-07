#!/usr/bin/python3
"""
Test file for user class
"""

import os
import time
import unittest
from datetime import datetime
from models import storage
from models.state import State
from models.base_model import BaseModel


class TestClass(unittest.TestCase):
    """Test cases"""

    def test_init(self):
        """test basemodel init"""
        snapshot = datetime.now()
        sm1 = State()
        snapshot2 = datetime.now()

        self.assertIsInstance(sm1.id, str)
        self.assertTrue(len(sm1.id) > 0)
        self.assertTrue('State.' + sm1.id in storage.all().keys())

        self.assertIsInstance(sm1.created_at, datetime)
        self.assertLess(sm1.created_at, snapshot2)
        self.assertGreater(sm1.created_at, snapshot)

        self.assertIsInstance(sm1.updated_at, datetime)
        self.assertLess(sm1.updated_at, snapshot2)
        self.assertGreater(sm1.updated_at, snapshot)

        sm1.save()
        self.assertIsInstance(sm1.updated_at, datetime)
        self.assertGreater(sm1.updated_at, snapshot)
        self.assertGreater(sm1.updated_at, snapshot2)
        del sm1

    def test_init_dict(self):
        """test basemode dict init"""
        test_dict = {'updated_at': datetime(2022, 5, 22, 12, 30, 00, 716921)
                     .isoformat('T'),
                     'id': '5361a11b-615c-42bf-9bdb-e2c3790ada14',
                     'created_at': datetime(2022, 5, 22, 12, 30, 00, 716921)
                     .isoformat('T')}
        sm2 = State(**test_dict)

        self.assertIsInstance(sm2.id, str)
        self.assertTrue(len(sm2.id) > 0)
        self.assertTrue(sm2.id == test_dict['id'])

        self.assertIsInstance(sm2.created_at, datetime)
        self.assertTrue(sm2.created_at.isoformat('T') == test_dict
                        ['created_at'])
        self.assertIsInstance(sm2.updated_at, datetime)
        self.assertTrue(sm2.updated_at.isoformat('T') == test_dict
                        ['updated_at'])
        sm2.save()
        self.assertGreater(sm2.updated_at, sm2.created_at)
        del sm2

    def test_attribute(self):
        """testcase for attributes"""
        sm3 = State()

        self.assertTrue(hasattr(sm3, "name"))
        self.assertIsInstance(sm3.name, str)

    def test_create_istance(self):
        """create a new instance"""
        new_state = State()
        self.assertIsInstance(new_state, State)

    def test_create_istance2(self):
        """create a new instance"""
        new_state = State()
        self.assertIsInstance(new_state, BaseModel)


if __name__ == '__main__':
    unittest.main()
