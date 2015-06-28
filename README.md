factory-boy-rest
=================

A REST test fixtures replacement for Python.

This is intented to be used on functional tests, to create REST-based entities
through the same [Factories][#factories] interface provided by
[Factory Boy][#factory_boy].

[#factories]: http://factoryboy.readthedocs.org/en/latest/reference.html#the-factory-class
[#factory_boy]: https://github.com/rbarrois/factory_boy

Installation
------------

```
pip install factory-rest
```


Development Installation
------------------------

Create a virtualenv:

```
mkproject --python=<fullpath_to_python_3> factory-boy-rest
```

Get the code:

```
git clone https://github.com/rbarrois/factory_boy.git .
```

Install it:

```
python setup.py develop
```

The last command enter your code in "Development Mode" it creates an
`egg-link` in your virtualenv's `site-packages` making it available
on this environment `sys.path`. For more info see [setuptools development-mode]
(https://pythonhosted.org/setuptools/setuptools.html#development-mode)


Development and test dependencies
---------------------------------

`setup.py` will handle test dependencies, to install development use:

```
pip install -e .[dev]
```


Tests
-----

```
python setup.py test
```


Defining factories
------------------

```python
from urllib.parse import urljoin

import requests

from factory import fuzzy
from factory_rest import RestFactory

base_url = 'http://127.0.0.1:8000'

class UserFactory(RestFactory):
    class Meta:
        create_url = urljoin(base_url, '/v1/users/')
        create_method = 'post'
        request_session = requests.session()

    first_name = 'John'
    last_name = 'Doe'
    admin = False


class UserFactory(RestFactory):
    class Meta:
        create_url = urljoin(base_url, '/v1/users/')
        create_method = 'post'
        request_session = requests.session()

    first_name = 'Admin'
    last_name = 'User'
    admin = True
```
