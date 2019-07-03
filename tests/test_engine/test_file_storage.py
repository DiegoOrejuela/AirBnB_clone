#!/usr/bin/python3
'''Unittest for FileStorage'''
import unittest
from models.engine.file_storage import FileStorage
import os
import pep8


class test_FileStorage(unittest.TestCase):
    '''Tests FileStorage class'''

    @classmethod
    def setUpClass(cls):
        '''set up before every test method'''
        cls.files1 = FileStorage()

    @classmethod
    def teardown(cls):
        '''remove test instances'''
        del cls.files1
        try:
            os.remove("file.json")
        except BaseException:
            pass

    def test_pep8_test_style(self):
        '''Pep8 style test'''
        pepe = pep8.StyleGuide(quiet=True)
        res = pepe.check_files(['models/engine/file_storage.py'])
        self.assertEqual(res.total_errors, 0, "Fix Style")

    def test_all(self):
        self.assertIsNotNone(FileStorage.all)

    def test_new(self):
        self.assertIsNotNone(FileStorage.new)

    def test_save(self):
        self.assertIsNotNone(FileStorage.save)

    def test_reload(self):
        self.assertIsNotNone(FileStorage.reload)
