# coding: utf-8

import json

from factory import base, containers


def get_inner(data, keys):
    for key in keys:
        data = data[key]
    return data


class FakeModel(object):
    pass


class RestFactoryOptions(base.FactoryOptions):

    def _build_default_options(self):
        return super(RestFactoryOptions, self)._build_default_options() + [
            base.OptionDefault('request_session', None, inherit=True),
            base.OptionDefault('create_url', None, inherit=True),
            base.OptionDefault('create_method', 'post', inherit=True),
            base.OptionDefault('id_field', 'id', inherit=True),
        ]


class RestFactory(base.Factory):

    class Meta:
        abstract = True
        model = FakeModel

    _options_class = RestFactoryOptions

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        session = cls._meta.request_session
        method = cls._meta.create_method
        url = cls._get_url(**kwargs)
        data = cls._prepare_data(**kwargs)

        response = session.request(method, url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
        assert response.status_code in (200, 201, 202), 'Create {} return: {}'.format(cls.__name__, response.content)
        return response.json()

    @classmethod
    def _get_url(cls, **kwargs):
        """get url and add values on {field_name} to proper value"""
        url = cls._meta.create_url
        if '{' in url:
            start = url.index('{') + 1
            end = url.index('}')
            field = url[start:end]
            sub_levels = field.split('__')
            value = get_inner(kwargs, sub_levels)
            return url.format(**{field: value})
        return url

    @classmethod
    def _prepare_data(cls, **data):
        """Put on SubFactories fields only the id value"""

        attribute_builder = containers.AttributeBuilder(cls, data)
        model_declaration = cls.declarations({})
        for field in attribute_builder._subfields:
            factory = model_declaration[field].factory_wrapper.factory
            data[field] = factory._get_id_value(data[field])
        return data

    @classmethod
    def _get_id_value(cls, data):
        return data[cls._meta.id_field]
