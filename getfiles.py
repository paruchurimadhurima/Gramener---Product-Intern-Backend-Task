import glob
import sys
import os

def files_in_driectory(directory_path, files_list):
    for file_name in glob.glob1(directory_path, "*"):
        file_path = os.path.join(directory_path, file_name)
        files_list.append(file_name)
        if(os.path.isdir(file_path)):
            files_in_driectory(file_path, files_list) #recursion if the file is a directory

def print_filenames_in_directory(directory_path):
    files_list = []
    files_in_driectory(directory_path, files_list)
    print("\n".join(files_list))

def main(argv=None):
    if argv is None:
        argv = sys.argv
    try:
        input_directory_path = argv[1]
        print_filenames_in_directory(input_directory_path)
        return 0
    except Exception as err:
        print(err, file = sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())