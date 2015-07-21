Usage
=====

Defining factories
------------------

.. code-block:: python

    python
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
    
