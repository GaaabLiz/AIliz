import os
from datetime import datetime

from core.enum.media_path_format import MediaPathFormat
from util import osutils
from util.datautils import convert_months_number_to_str


class AilizImage:

    def __init__(self, image_path):
        self.ai_tags = None
        self.path = image_path
        self.file_name = os.path.basename(self.path)
        self.extension = os.path.splitext(image_path)[1].lower()
        self.creation_time = osutils.get_file_c_date(self.path)
        self.year, self.month, self.day = self.creation_time.year, self.creation_time.month, self.creation_time.day
        self.size_byte = os.path.getsize(self.path)
        self.size_mb = self.size_byte / (1024 * 1024)
        self.output_path = None

    def __str__(self):
        return f"Image: {self.file_name} - {self.size_mb} MB - {self.year}/{self.month}/{self.day}"

    def __repr__(self):
        return f"Image: {self.file_name} - {self.size_mb} MB - {self.year}/{self.month}/{self.day}"

    def load_output_path(self, formato: MediaPathFormat, output_path: str):
        if formato == MediaPathFormat.IMAGE_YEAR_MONTH_1:
            str_month = convert_months_number_to_str(self.month)
            self.output_path = os.path.join(output_path, str(self.year), str_month)
        elif formato == MediaPathFormat.OUTPUT_FOLDER:
            self.output_path = output_path
        elif formato == MediaPathFormat.IMAGE_YEAR_MONTH_2:
            self.output_path = os.path.join(output_path, str(self.year), str(self.month))

    def set_ai_tags(self, tags):
        self.ai_tags = tags

    # def get_creation_time(self):
    #     try:
    #         timestamp = os.path.getctime(self.path)
    #         return datetime.fromtimestamp(timestamp)
    #     except Exception as e:
    #         print(f"Error getting creation time: {e}")
    #         return None
    #
    # def get_date_info(self):
    #     if self.creation_time:
    #         return self.creation_time.year, self.creation_time.month, self.creation_time.day
    #     return None, None, None
