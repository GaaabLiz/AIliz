import base64

import rich
from yaspin import yaspin

from core.api.service.ollamaliz import scan_image_with_llava
from core.enum.ai_power import AiPower
from core.enum.cfglist import CfgList
from core.enum.cfgsection import CfgSection
from core.model.ailiz_image import AilizImage
from core.util.cfgutils import read_config


def scan():
    pass


def scan_image(
        file_path: str,
        ai: bool = False,
) -> AilizImage | None:
    if ai:

        # Scanning image with llava
        with yaspin(text="Scanning image " + file_path + " with llava...", color="yellow", side="right") as spinner:
            llava_result = scan_image_with_llava(file_path)
            if llava_result is not None:
                spinner.ok("✅ ")
            else:
                spinner.fail("💥 ")
                rich.print("Error while scanning image with llava.")

        # Getting tags from llava result




        image = AilizImage(file_path)
        return image
    else:
        rich.print("Scanning image " + file_path + "...")
        return AilizImage(file_path)