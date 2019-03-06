import os
import cv2
from glob import glob

#檔案位置
DATAS_FOLDER = "./data"
BLOCK_DATA_FOLDER = os.path.join(DATAS_FOLDER, "dogimg")

#讀取檔案
images_per_class = {}
for class_folder_name in os.listdir(BLOCK_DATA_FOLDER):
    class_folder_path = os.path.join(BLOCK_DATA_FOLDER, class_folder_name)
    class_label = class_folder_name
    images_per_class[class_label] = []
    for image_path in glob(os.path.join(class_folder_path, "*.png")):
        image_bgr = cv2.imread(image_path, cv2.IMREAD_COLOR)
        images_per_class[class_label].append(image_bgr)

for key,value in images_per_class.items():
    print("{0} -> {1}".format(key, len(value))) 
