import os
import datetime
import piexif

folder_path = '/Users/your_user/Holding/'

# known timestamp and date
known_timestamp = 280902568783911
known_date = datetime.datetime(2014, 9, 25, 14, 0, 0)

for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path) and filename.endswith('.jpg'):
        # Get the timestamp from the file name
        timestamp = int(filename.split('.')[0])
        # calculate the difference between timestamp and known timestamp
        timestamp_diff = timestamp - known_timestamp
        # calculate the date from the known date
        date_time = known_date + datetime.timedelta(seconds=timestamp_diff)
        exif_datetime = date_time.strftime('%Y:%m:%d %H:%M:%S')
        # Open the image file
        with open(file_path, 'rb') as f:
            # Read the exif data
            exif_dict = piexif.load(f.read())
            # Modify the exif data
            exif_dict["0th"][piexif.ImageIFD.DateTime] = exif_datetime
            exif_bytes = piexif.dump(exif_dict)
            # save the image with modified exif data
            piexif.insert(exif_bytes, file_path)
