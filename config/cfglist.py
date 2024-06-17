from enum import Enum


class CfgList(Enum):
    INIT = "init"
    AI_MODEL_PATH = "ai_model_path"
    AI_MODEL_CUSTOM_PATH = "ai_model_custom_path"
    USE_CUSTOM_PATH = "use_custom_path"
    OLLAMA_URL = "ollama_url"
