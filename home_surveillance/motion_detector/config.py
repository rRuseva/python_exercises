import os
import sys
from datetime import datetime
dest_path = "..//result_data"

### global variables for video processing
resolution = (640, 480) 
min_area = 7000 			### minimum size of detected object
diff_thresh = 80			### threshold for detection of motion
