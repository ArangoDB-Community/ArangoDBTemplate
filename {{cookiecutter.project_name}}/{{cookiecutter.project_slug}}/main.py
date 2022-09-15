#tutorial_connecter
{%- if cookiecutter.use_tutorial_connector|lower == 'y' %} {{cookiecutter._new_lines}} from adb_cloud_connector import get_temp_credentials {{cookiecutter._new_lines}} {%- endif %}

#python_arango
{%- if cookiecutter.python_driver|lower == 'python_arango' %} {{cookiecutter._new_lines}} from arango import ArangoClient {{cookiecutter._new_lines}} {%- endif %}

#py Arango
{%- if cookiecutter.python_driver|lower == 'pyarango' %} {{cookiecutter._new_lines}}from pyArango.connection import *{{cookiecutter._new_lines}} {%- endif %}

#
{%- if cookiecutter.use_arangopipe|lower == 'y' %} {{cookiecutter._new_lines}}arangopipe>=0.0.70.0.1, {{cookiecutter._new_lines}} {%- endif %}

#
{%- if cookiecutter.data_science_adapter|lower == 'networkx_adapter' %} {{cookiecutter._new_lines}} adbnx-adapter>=4.2.0, {{cookiecutter._new_lines}} {%- endif %}

#
{%- if cookiecutter.data_science_adapter|lower == 'pyg_adapter' %} {{cookiecutter._new_lines}}adbpyg-adapter>=4.2.0, {{cookiecutter._new_lines}} {%- endif %}

#
{%- if cookiecutter.data_science_adapter|lower == 'dgl_adapter' %} {{cookiecutter._new_lines}}adbdgl-adapter>=4.2.0, {{cookiecutter._new_lines}} {%- endif %}

#tutorial_connetor
{%- if cookiecutter.use_tutorial_connector|lower == 'y' %} {{cookiecutter._new_lines}}con = get_temp_credentials() {{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.use_tutorial_connector|lower == 'y' %} print(con) {{cookiecutter._new_lines}} {%- endif %}

#python_arango
{%- if cookiecutter.python_driver|lower == 'python_arango' %} "# Initialize the ArangoDB client. {{cookiecutter._new_lines}} client = ArangoClient(hosts='http://localhost:8529')" {{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.python_driver|lower == 'python_arango' %} "db = client.db('test', username='root', password='passwd')" {{cookiecutter._new_lines}} {%- endif %}

#pyArango
{%- if cookiecutter.python_driver|lower == 'pyarango' %} conn = Connection(){{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.python_driver|lower == 'pyarango' %} conn.createDatabase(name="test_db"){{cookiecutter._new_lines}} {%- endif %}
{%- if cookiecutter.python_driver|lower == 'pyarango' %} db = conn["test_db"] # all databases are loaded automatically into the connection and are accessible in this fashion
{{cookiecutter._new_lines}} {%- endif %}