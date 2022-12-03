#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import cv2
from os import listdir
from os.path import isfile, join
SHAPE = 96


def getImagesFromDir(directory):
    onlyfiles = [f for f in listdir(directory) if isfile(join(directory, f))]
    return onlyfiles, directory

def resizeImages(files, directory):
    for f in files:
        print(f)
        image = cv2.imread(join(directory, f))
        img = cv2.resize(image, (SHAPE, SHAPE), interpolation=cv2.INTER_AREA)
        cv2.imwrite(join(directory, f), img)

# files = getImagesFromDir('/home/user/Efficient-CapsNet/covid-chestxray-dataset/images_ok/bacteria')
# print(files)

# bacteria_files = getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/images_ok/bacteria')
# print(bacteria_files)

# resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/images_ok/bacteria'))
# resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/images_ok/healthy'))
# resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/images_ok/viral/covid-19'))
# resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/images_ok/viral/other'))

resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/train/bacteria'))
resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/train/healthy'))
resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/train/viral_covid-19'))
resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/train/viral_other'))


resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/test/bacteria'))
resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/test/healthy'))
resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/test/viral_covid-19'))
resizeImages(*getImagesFromDir('/root/Efficient-CapsNet/covid-chestxray-dataset/test/viral_other'))

