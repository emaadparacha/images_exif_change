import os
import datetime
import exifread
from PIL import Image
import piexif


folder_path = '/Users/your_user/Holding/'

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path) and filename.endswith('.jpg'):
        # Get the Unix timestamp from the file name
        unix_timestamp = int(filename.split('.')[0])/1000
        # Convert the Unix timestamp to a datetime object
        dt = datetime.datetime.fromtimestamp(unix_timestamp)
        # format the datetime object to exif format
        exif_datetime = dt.strftime('%Y:%m:%d %H:%M:%S')
        # Open the image file
        with open(file_path, 'rb') as f:
            # Read the exif data
            exif_dict = piexif.load(f.read())
            # Modify the exif data
            exif_dict["0th"][piexif.ImageIFD.DateTime] = exif_datetime
            exif_bytes = piexif.dump(exif_dict)
            # save the image with modified exif data
            piexif.insert(exif_bytes, file_path)
