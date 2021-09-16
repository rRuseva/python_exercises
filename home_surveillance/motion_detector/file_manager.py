import os
from datetime import datetime
import config as cfg

current_time = datetime.now().strftime("%Y%m%d_%H")

if not os.path.isdir(cfg.dest_path):
    print("uups")
    os.mkdir(cfg.dest_path)
result_dir = os.path.join(cfg.dest_path, current_time) 
if not os.path.isdir(result_dir):
    os.mkdir(result_dir)