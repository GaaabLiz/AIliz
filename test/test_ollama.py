import os
import unittest

import rich

from dotenv import load_dotenv


class TestOllama(unittest.TestCase):

    def setUp(self):
        load_dotenv()
        self.ollama_url = os.getenv('OLLAMA_URL')
        pass

    def test_connection(self):
        res = check_ollama_status(self.ollama_url)
        self.assertTrue(res.is_successful())

    def test_get_models(self):
        res = get_installed_models(self.ollama_url)
        self.assertTrue(res.is_successful())
        rich.print_json(res.response.text)


if __name__ == "__main__":
    unittest.main()
