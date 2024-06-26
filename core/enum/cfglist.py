from enum import Enum


class CfgList(Enum):
    INIT = "init"
    AI_MODEL_PATH = "ai_model_path"
    AI_MODEL_CUSTOM_PATH = "ai_model_custom_path"
    AI_POWER = "ai_power"
    USE_CUSTOM_PATH = "use_custom_path"
    OLLAMA_URL = "ollama_url"
    OLLAMA_URL_SET = "ollama_url_set"
    OLLAMA_URL_LAST = "ollama_url_last"
