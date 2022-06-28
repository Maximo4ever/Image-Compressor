from distutils import extension
from pickletools import optimize
from PIL import Image
import os

downloadsFolder = 'C:/Users/chori/Downloads/'

if __name__ == "__main__":
    for filename in os.listdir(downloadsFolder):
        name, extension = os.path.splitext(downloadsFolder + filename)

        if extension in [".jpg", ".jpeg", ".png"]:
            picture = Image.open(downloadsFolder + filename)
            picture.save(downloadsFolder + "compressed_" +
                         filename, optimize=True, quality=75)
