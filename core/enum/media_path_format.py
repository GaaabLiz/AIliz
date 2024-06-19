

from enum import Enum


class MediaPathFormat(Enum):
    OUTPUT_FOLDER = "All in the Output folder"
    IMAGE_YEAR_MONTH_1 = "%YEAR%/%Month%/%FileName%"
    IMAGE_YEAR_MONTH_2 = "%YEAR%/%Month_number%/%FileName%"