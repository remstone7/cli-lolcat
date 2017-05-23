import os
import cat_service
import platform
import subprocess

def main():
    print_header()# print the header
    folder = get_or_create_output_folder()

    print('found or created folder: {}'.format(folder))

    download_cats(folder)
    # display cats
    display_cats(folder)

def print_header():
    print('---------------------------')
    print('          CAT FACTORY      ')
    print('---------------------------')


def get_or_create_output_folder():
    print(__file__)
    base_folder = os.path.dirname(__file__)
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count+1):
        name = 'lolcat {}'.format(i)
        print('cat ' + name)
        cat_service.get_cat(folder, name)


def display_cats(folder):
    # open folder
    if platform.system() == 'Darwin':
        subprocess.call(['open', folder])
    elif platform.system() == 'Windows':
        subprocess.call(['start', folder])
    elif platform.system() == 'Linux':
        subprocess.call(['xdg-open', folder])
    else:
        print("We don't support your os: " + platform.system())

if __name__ == '__main__':
    main()
