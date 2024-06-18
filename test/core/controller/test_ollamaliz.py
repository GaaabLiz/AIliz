import os
import unittest
from unittest import TestCase

import rich

from dotenv import load_dotenv

from core.enum.ai_power import AiPower
from util.ai import ollamapi
from core.controller import ollamaliz


class TestOllamaliz(TestCase):

    def setUp(self):
        load_dotenv()
        self.ollama_url = os.getenv('OLLAMA_URL')
        pass

    def test_download_models_list(self):
        models = ollamaliz.download_models_list(self.ollama_url)
        self.assertTrue(len(models) > 0)

    def test_is_model_installed(self):
        models = ollamaliz.download_models_list(self.ollama_url)
        self.assertTrue(ollamaliz.is_model_installed('llava:13b', models))

    def test_download_required_models(self):
        models = ollamaliz.download_models_list(self.ollama_url)
        for model in models:
            print(model)
        ollamaliz.download_required_models(AiPower.MEDIUM.value, models)
        models = ollamaliz.download_models_list(self.ollama_url)
        self.assertTrue(len(models) > 0)
