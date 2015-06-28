# coding: utf-8

from __future__ import (absolute_import, division, generators, print_function,
                        unicode_literals, nested_scopes, with_statement)

from six.moves.urllib.parse import urljoin

from factory import fuzzy
from factory_rest import rest
import httpretty
import requests


@httpretty.activate
def test_factory_create_should_issue_post_to_proper_endpoint():
    base_url = 'https://api.twitter.com/1.1'
    base_session = requests.session()

    class DirectMessageFactory(rest.RestFactory):

        class Meta:
            create_url = urljoin(base_url, '/direct_messages/new.json')
            create_method = 'POST'
            request_session = base_session

        screen_name = fuzzy.FuzzyText()
        text = fuzzy.FuzzyText()

    httpretty.register_uri(httpretty.POST, urljoin(base_url, '/direct_messages/new.json'),
                           body='{"sent": true}', status=200)
    dm = DirectMessageFactory()
    assert 'sent' in dm
    assert dm['sent'] is True
