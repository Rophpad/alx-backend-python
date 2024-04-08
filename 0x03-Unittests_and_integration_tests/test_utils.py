#!/usr/bin/env python3
""" Parameterize a unit test """


import unittest
from typing import Dict, Tuple, Union
from parameterized import parameterized
from utils import *


class TestAccessNestedMap(unittest.TestCase):
    """
    Unittest access_nested_map
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int],
    ) -> None:
        """ Tests outputs for differents inputs """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]
    ) -> None:
        """ Tests for error raising """
        self.assertRaises(KeyError, lambda: (access_nested_map(nested_map, path), expected))
