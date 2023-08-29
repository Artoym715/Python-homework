from files_pack import home_functions as hf

if __name__ == '__main__':
    print("Переименование файлов в каталоге data_files")
    files_cnt = hf.group_rename_files("picture-2", ".jpg", path="./data_files")
    print(f"Переименовано: {files_cnt}")
