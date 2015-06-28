import os
import re
import sys
import codecs

from setuptools import setup, find_packages, Command
from setuptools.command.test import test as TestCommand


here = os.path.abspath(os.path.dirname(__file__))

setup_requires = ['pytest', 'tox']
install_requires = ['tox', 'factory-boy', 'requests']
dev_requires = ['pyflakes', 'pep8', 'pylint', 'check-manifest',
                'ipython', 'ipdb', 'sphinx', 'sphinx_rtd_theme',
                'sphinxcontrib-napoleon']
tests_require = ['pytest-cov', 'pytest-cache', 'pytest-timeout']


# find the first version number in CHANGES
with open(os.path.join(here, 'CHANGES')) as f:
    for line in f:
        version = line.strip()
        if re.search("^[0-9]+\.[0-9]+\.[0-9]+$", version):
            break
    else:
        raise RuntimeError('Could not determine a version from CHANGES file.')


# Get the long description from the relevant file
with codecs.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


class VersionCommand(Command):
    description = "print library version"
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        print(version)


class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['--strict', '--verbose', '--tb=long',
                          '--cov', 'hystrix', '--cov-report',
                          'term-missing', 'tests']
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)


setup(
    name='factory-rest',
    version=version,

    description='Extension to factory-boy to create fixtures over http',
    long_description=long_description,

    # The project URL.
    url='https://github.com/bertonha/factory-boy-rest',

    # Author details
    author='Christofer Bertonha',
    author_email='christoferbertonha@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',

        # Who the project is intended for.
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Testing',

        # Supported Python versions.
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.4',
    ],
    keywords='testing test fixtures',
    packages=find_packages(exclude=['tests']),
    setup_requires=setup_requires,
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'dev': dev_requires,
        'test': tests_require,
    },
    cmdclass={"version": VersionCommand, 'test': PyTest},
)
