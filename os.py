import os

file_path = os.getcwd()
for folder, sub_folders,files in os.walk(file_path):
    print(f"currently looking at {folder}")
    print('\n')
    print('subfolders are : ')
    for sub_fold in sub_folders:
        print(f"subfolder: {sub_fold}")

    print('\n')
    print("the files are: ")
    for f in files:
        print(f"\t File: {f}")
    print('\n')