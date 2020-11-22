from os import listdir
from os.path import isfile, join
from pathlib import Path
import numpy
import cv2
import argparse
import numpy
import csv

my_file = Path("csv/details.csv")
if my_file.is_file():
    f = open(my_file, "w+")
    with open('csv/details.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["S.No.", "Name", "Hieght","Width","Channels","Avg Blue","Avg Red","Avg Green"])
    f.close()
    pass
else:
    with open('csv/details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["S.No.", "Name", "Hieght","Width","Channels","Avg Blue","Avg Red","Avg Green"])

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Path to folder")
args = vars(ap.parse_args())


mypath=args["image"]
onlyfiles = [ f for f in listdir(mypath) if isfile(join(mypath,f)) ]
images = numpy.empty(len(onlyfiles), dtype=object)
for n in range(0, len(onlyfiles)):
    path = join(mypath,onlyfiles[n])
    images[n] = cv2.imread(join(mypath,onlyfiles[n]),cv2.IMREAD_UNCHANGED)
    img = cv2.imread(path)
    h,w,c = img.shape
    print(h,w,c)
    avg_color_per_row = numpy.average(img, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    with open('csv/details.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([n+1, onlyfiles[n], h,w,c,avg_color[0],avg_color[1],avg_color[2]])
        file.close()
