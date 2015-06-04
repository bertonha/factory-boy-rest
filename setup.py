import os
import re
import codecs

from setuptools import setup, find_packages, Command


here = os.path.abspath(os.path.dirname(__file__))


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

    install_requires=[
        'factory-boy',
        'requests',
    ],

    cmdclass={"version": VersionCommand},
)
