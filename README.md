# Change Image EXIF Datetime
Change Image EXIF datetime information based on the datetime in the image name.

### Dependencies
* Pillow - `pip3 install Pillow`
* piexif - `pip3 install piexif`

### Usage
There are two Python scripts here, `unix_time_image_change.py` and `custom_time_image_change.py`, both which take the timestamp in the file name (the file name must be the the timestamp), and changes the EXIF datetime to that specific datetime.

`unix_time_image_change.py` takes the unix time from the file name while `custom_time_image_change.py` takes a custom time stamp and with a reference custom time stamp and known date, it gets the correct datetime and sets the right EXIF setting.
