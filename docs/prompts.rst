=======
Prompts
=======

When you create a package, you are prompted to enter these values.

Templated Values
----------------

The following appear in various parts of your generated project.

full_name
    Your full name.

email
    Your email address.

github_username
    Your GitHub username.

project_name
    The name of your new Python package project. This is used in documentation, so spaces and any characters are fine here.

project_slug
    The namespace of your Python package. This should be Python import-friendly. Typically, it is the slugified version of project_name. Note: your PyPi project and Travis links will use project_slug, so change those in the README afterwards.

project_short_description
    A 1-sentence description of what your Python package does.

pypi_username
    Your Python Package Index account username.

version
    The starting version number of the package.

Options
-------

The following package configuration options set up different features for your project.

use_pytest
    Whether to use `pytest <https://docs.pytest.org/en/latest/>`_.

use_black
    Whether to use `black <https://pypi.org/project/black/>`_.

use_pyArango
    Whether to use `pyArango <https://github.com/ArangoDB-Community/pyArango>`_.

use_arango
    Whether to use `arango <https://pypi.org/project/arango/>`_.

use_python-arango
    Whether to use `python-arango <https://github.com/ArangoDB-Community/python-arango>`_.

use_arangopipe
    Whether to use `arangopipe <https://github.com/arangoml/arangopipe>`_.

use_networkx_adapter
    Whether to use `networkx-adapter <https://github.com/arangoml/networkx-adapter>`_.

use_oasis
    Whether to use the `Oasis-Tool <https://github.com/arangodb/cloud>`_ to connect to this service.

use_sphinx
    Whether to use `Sphinx <https://pypi.org/project/Sphinx/>`_.

create_author_file
    Whether to create an authors file, or not

import_IMDB_Movie-Graph
    Whether to import this pre build project or not, it can also be found in `this <>`_ notebook.

create_PyPI_package
    Whether to import the basics needed for to create and upload a PyPI package

include_notebooks
    Whether to include some explanatory Notebooks for the packages mentioned above.

open_source_license
    Choose a `license <https://choosealicense.com/>`_. Options: [1. MIT License, 2. BSD license, 3. ISC license, 4. Apache Software License 2.0, 5. GNU General Public License v3, 6. Not open source]
