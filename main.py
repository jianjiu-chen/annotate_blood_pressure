import os
import shutil

from utils import input_person, input_today, open_image_and_get_input, store_input


#######################
# get person and date
#######################
person = input_person()
assert person in ('pimama', 'dad'), 'The input should be either "pimama" or "dad".'

today = input_today()
assert len(today) == 8, 'The input should be a 8 digits string.'
assert int(today[0:4]) in range(2024, 2029), 'The input year should be between 2024 and 2029.'
assert int(today[4:6]) in range(1, 13), 'The input year should be between 1 and 12.'
assert int(today[6:8]) in range(1, 31), 'The input year should be between 1 and 31.'

#######################
# rename all jpg files
# store the new file names
# move the files to the designated path
#######################
download_dir = '/Users/Chen/Downloads'
pic_old_names = [i for i in os.listdir(download_dir) if '.jpg' in i]
pic_new_names = []
pic_new_names_fullpath = []
assert len(pic_old_names) != 0, 'There should be 1 or more jpg files in Downloads directory!'

for i, pic_i in enumerate(pic_old_names):
    old_filename = os.path.join(download_dir, pic_i)
    new_filename_sub = f"{person}_{today}_{i+1}.jpg"
    new_filename = os.path.join(download_dir, new_filename_sub)
    os.rename(old_filename, new_filename)
    #
    pic_new_names.append(new_filename_sub)
    #
    src_filepath = new_filename
    dst_filepath = os.path.join(f"/Users/Chen/project/annotate_blood_pressure/data/data_{person}",
                                new_filename_sub)
    shutil.move(src_filepath, dst_filepath)
    #
    pic_new_names_fullpath.append(dst_filepath)


#######################
# data entry for each picture
#######################
data_dict = {'sys_bp_val': None,
             'dia_bp_val': None,
             'hr_val': None}

for pic_nam_i, pic_path_i in zip(pic_new_names, pic_new_names_fullpath):
    open_image_and_get_input(pic_path_i, data_dict)  # update values in data_dict
    store_input(data_dict, pic_nam_i)
