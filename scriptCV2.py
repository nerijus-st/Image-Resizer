import cv2
import glob
import os

images = glob.glob("Images/*.jpg")
directory = "Resized\\"
dimensions = (100, 100)

file_count = 0

for image in images:
    image_name = image.replace("Images\\", "")
    img = cv2.imread(image, 1)
    resized_image = cv2.resize(img, dimensions)
    if not os.path.exists(directory):
        os.makedirs(directory)
    cv2.imwrite(directory + image_name, resized_image)
    file_count += 1
print("Total " + str(file_count) + " files resized.")
