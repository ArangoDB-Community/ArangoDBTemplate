#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('HISTORY.rst') as history_file:
    history = history_file.read()

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requirements = [
{%- if cookiecutter.python_driver|lower == 'pyarango' %} 'pyArango>=2.0.1', {{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.python_driver|lower == 'python_arango' %} 'python-arango>=7.4.1', {{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.use_arangopipe|lower == 'y' %} 'arangopipe>=0.0.70.0.1', {{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.data_science_adapter|lower == 'networkx_adapter' %} 'adbnx-adapter>=4.2.0', {{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.data_science_adapter|lower == 'pyg_adapter' %} 'adbpyg-adapter>=1.0.0', {{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.data_science_adapter|lower == 'dgl_adapter' %} 'adbdgl-adapter>=2.1.0', {{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.use_tutorial_connector|lower == 'y' %} 'adb-cloud-connector>=1.0.2', {{cookiecutter._new_lines}} {%- endif %}
]


dev_requirements = [
{%- if cookiecutter.use_black|lower == 'y' %} 'black>=22.8.0', {{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.use_pytest|lower == 'y' %} 'pytest>=7.1.3', {{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.use_sphinx|lower == 'y' %} 'sphinx>=5.1.1', {{cookiecutter._new_lines}} {%- endif %}
]

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name='{{ cookiecutter.project_slug }}',
    version='{{ cookiecutter.version }}',
    author="{{ cookiecutter.full_name.replace('\"', '\\\"') }}",
    author_email='{{ cookiecutter.email }}',
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug }}',
    project_urls={
        "Bug Tracker": "https://github.com/ferie24/ArangoDBTemplate",
    },
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        {%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
        {%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        "Operating System :: OS Independent",
    ],
    {%- if cookiecutter.open_source_license in license_classifiers %}
    license="{{ cookiecutter.open_source_license }}",
    {%- endif %}
    keywords='{{ cookiecutter.project_slug }}',
    package_dir={'{{ cookiecutter.project_slug }}' : '{{ cookiecutter.project_slug }}'},
    packages=find_packages(include=['{{ cookiecutter.project_slug }}', '{{ cookiecutter.project_slug }}.*']),
    include_package_data=True,
    #-----

    install_requires=install_requirements,
    test_suite='tests',
    extras_require={
        'dev' : dev_requirements
    },
    zip_safe=False,
)
