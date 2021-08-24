#Example
#  before
# common_string_file_1.py
# common_string_file_2.py
# common_string_file_3.py
# common_string_file_4.py

# after
# file_1.py
# file_2.py
# file_3.py
# file_4.py

import os
# string before which you want to delete all characters in name
DELETE_BEFORE = "file"
ENDSWITH = ".py"
path = r'C:\\Users\sujal\Desktop\\folder_with_target_files\\'

for f_name in os.listdir(path):
    if f_name.endswith(ENDSWITH):
        idx = (f_name.index(DELETE_BEFORE))

        # sets the new name of the string by taking all the characters present after the common string
        new_name = f_name[idx:]
        print(new_name)
        src = path + f_name
        dst = path + new_name
        os.rename(src, dst)
 
