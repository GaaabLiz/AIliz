import unittest

from ai.ollamapi import *


class TestOllama(unittest.TestCase):

    def setUp(self):
        self.ollama_url = "http://192.168.0.205:11434"
        pass

    def test_connection(self):
        res = check_ollama_status(self.ollama_url)
        self.assertTrue(res.is_successful())

    def test_get_models(self):
        res = get_installed_models(self.ollama_url)
        self.assertTrue(res.is_successful())







if __name__ == "__main__":
    unittest.main()