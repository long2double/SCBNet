import torch.utils.data as data

from PIL import Image
import os
import os.path
import numpy as np

IMG_EXTENSIONS = [
    '.jpg', '.JPG', '.jpeg', '.JPEG',
    '.png', '.PNG', '.ppm', '.PPM', '.bmp', '.BMP',
]


def is_image_file(filename):
    return any(filename.endswith(extension) for extension in IMG_EXTENSIONS)

def dataloader(filepath):

  left_fold  = 'colored_0/'
  right_fold = 'colored_1/'


  image = [img for img in os.listdir(filepath+left_fold) if img.find('_10') > -1]


  left_test  = [filepath+left_fold+img for img in image]
  right_test = [filepath+right_fold+img for img in image]
  left_test.sort()
  right_test.sort()
  return left_test, right_test
