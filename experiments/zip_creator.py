import zipfile
import pathlib

def make_archive(filepaths, dest_folder, compressed_file_name):
    dest_path = pathlib.Path(dest_folder, compressed_file_name)
    with zipfile.ZipFile(dest_path, 'w') as archive:

        for path in filepaths:
            path = pathlib.Path(path)
            archive.write(path, arcname=path.name)


# good for debugging
if __name__ == "__main__":
    source_paths = ['C:/Users/james/Desktop/code/Python/py_mega_course/mega_course_project/experiments/bonus6.py', 'C:/Users/james/Desktop/code/Python/py_mega_course/mega_course_project/experiments/bonus9_password_function']
    destination_path = "C:/Users/james/Desktop/code/Python/py_mega_course/mega_course_project/experiments"
    make_archive(source_paths, destination_path, "compressed.zip")
    print(f"archived to {destination_path}")
