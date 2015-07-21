Contributing
============

Development Installation
------------------------

Create a virtualenv:

.. code-block:: sh

    mkproject --python=<fullpath_to_python_3> factory-boy-rest


Get the code:


.. code-block:: sh
    
    git clone https://github.com/bertonha/factory-boy-rest.git .


Install it:

.. code-block:: sh

    python setup.py develop


The last command enter your code in "Development Mode" it creates an
``egg-link`` in your virtualenv's ``site-packages`` making it available
on this environment ``sys.path``. For more info see `setuptools development mode
<https://pythonhosted.org/setuptools/setuptools.html#development-mode>`_


Development and test dependencies
---------------------------------

``setup.py`` will handle test dependencies, to install development use:

.. code-block:: sh

    pip install -e .[dev]


Tests
-----

You have many forms to run tests.

The following command will handle test dependencies installation. Perfect for
first run.

.. code-block:: sh
    
    python setup.py test

Don't forget to run the test suite against all python versions before submit a
pull request. It's ease just do:

.. code-block:: sh

    tox


If you want to run only for Python3 you can do:

.. code-block:: sh

    tox -e py34


