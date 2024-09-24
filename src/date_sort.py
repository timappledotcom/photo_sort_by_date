import os
from PIL import Image
from PIL.ExifTags import TAGS
import shutil

def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if exif_data is not None:
        for tag, value in exif_data.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "DateTimeOriginal":
                return value
    return None

def organize_photos_by_year():
    current_directory = os.getcwd()
    for root, dirs, files in os.walk(current_directory):
        for file in files:
            if file.lower().endswith(('jpg', 'jpeg', 'png')):
                file_path = os.path.join(root, file)
                date_taken = get_exif_data(file_path)
                if date_taken:
                    year = date_taken.split(':')[0]
                    year_folder = os.path.join(current_directory, year)
                    if not os.path.exists(year_folder):
                        os.makedirs(year_folder)
                    shutil.move(file_path, os.path.join(year_folder, file))

if __name__ == "__main__":
    organize_photos_by_year()

