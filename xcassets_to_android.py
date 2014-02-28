import sys, os, glob, operator
from PIL import Image

def get_file_names():
    files = []
    for directory in os.listdir(parent_directory):
        if "imageset" in directory:
            directory = parent_directory + "/" + directory
            for filename in os.listdir(directory):
                if "@2x.png" in filename:
                    full_filename = directory + "/" + filename
                    files.append([full_filename, filename])
    return files

def resize_image(files, image_size, drawable_folder):
    i = 0
    for file in files:
        image = Image.open(file[0])
        size = tuple(map(int, map(operator.mul, image.size, (image_size, image_size))))
        size_list = list(size)
        size_list = [1 if s == 0 else s for s in size_list]
        size = tuple(size_list)
        image.thumbnail(size, Image.ANTIALIAS)
        directory = parent_directory + "/" + drawable_folder
        if not os.path.exists(directory):
            os.makedirs(directory)
        file_name = file[1]
        at_location = file_name.index("@")
        file_name = file_name[:at_location] + ".png"
        file_name = file_name.replace("-", "_")
        image.save(directory + "/" + file_name, "PNG")
        i = i + 1

parent_directory = sys.argv[1]
files = get_file_names()
resize_image(files, 1, 'drawable-xhdpi')
resize_image(files, .75, 'drawable-hdpi')
resize_image(files, .5, 'drawable-mdpi')
resize_image(files, .375, 'drawable-ldpi')
