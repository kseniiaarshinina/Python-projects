import os
import shutil
import requests


def main():
    print_header()
    folder = create_or_read_directory()
    print('Found or created folder:' + folder)
    download_cats(folder)
    #display_cats()


def print_header():
    print("---------------------------")
    print("        CAT FACTORY")
    print("---------------------------")


def create_or_read_directory():
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = 'cat pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating it now at {}'.format(full_path))
        os.mkdir(full_path)
    return full_path


def download_cats(folder):
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading cat {}'.format(name))
        get_cat(folder, name)


def get_cat(folder, name):
    url = 'https://rand.cat/pic'
    data = get_url_for_cats(url)
    save_image(folder, name, data)


def get_url_for_cats(url):
    response = requests.get(url, stream=True)
    return response.raw


def save_image(folder, name, data):
    file_name = os.path.join(folder, name + '.jpeg')
    with open(file_name, 'wb') as file:
        data.decode_content = True
        shutil.copyfileobj(data, file)


if __name__ == "__main__":
    main()

