import base64

import rich

from core.api.service.ollamaliz import scan_image_with_llava
from core.enum.ai_power import AiPower
from core.model.ailiz_image import AilizImage


def scan():
    pass


def scan_image(
        file_path: str,
        ai: bool = False,
) -> AilizImage | None:
    if ai:
        rich.print("Scanning image " + file_path + " with ai...")
        # TODO: fare controllo ollama e modello llava
        return scan_image_with_llava(file_path, AiPower.MEDIUM)
    else:
        rich.print("Scanning image " + file_path + "...")
        return AilizImage(file_path)