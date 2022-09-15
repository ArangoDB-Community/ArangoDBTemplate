import os
import shutil
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')

    if '{{ cookiecutter.create_PyPI_package}}' != 'y':
        remove_file('setup.py')

    if '{{ cookiecutter.include_notebooks}}' != 'y':
        shutil.rmtree('notebooks')

    if '{{ cookiecutter.import_IMDB_Movie_Graph}}' != 'y':
        shutil.rmtree('IMDB_Movie_Graph')

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')
