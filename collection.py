import os
import shutil

file_path = os.path.dirname(os.path.realpath(__file__)) + r"\image_name.jpg"
save_path = os.path.dirname(os.path.realpath(__file__)) + r"\collection"
i = 0
new_file_path = save_path + r"\{}.jpg"
while (os.path.isfile(new_file_path.format(i))):
    i+=1
    print(new_file_path.format(i))
shutil.copy(file_path, new_file_path.format(i))