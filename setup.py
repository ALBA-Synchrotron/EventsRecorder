# setup.py
from setuptools import setup
from setuptools import find_packages

# The version is updated automatically with bumpversion
# Do not update manually
__version = '0.1.0'


setup(
    name='EventsRecorder',
    description='Python Tango client',
    version=__version,
    author='Roberto J. Homs Puron',
    author_email='rhoms@cells.es',
    url='https://github.com/ALBA-Synchrotron/EventsRecorder',
    packages=find_packages(),
    license="GPLv3",
    long_description="Python script to record on a file the Tango events "
                     "generated by an attribute",
    # classifiers=[
    #     'Development Status :: 5 - Production/Stable',
    #     'Intended Audience :: Developers',
    #     'Intended Audience :: End Users/Desktop',
    #     'License :: OSI Approved :: Python Software Foundation License',
    #     'Natural Language :: English',
    #     'Operating System :: POSIX',
    #     'Operating System :: Microsoft :: Windows',
    #     'Programming Language :: Python',
    #     'Topic :: Communications',
    #     'Topic :: Software Development :: Libraries',
    # ],
    entry_points={
        'console_scripts': [
            'eventsrecorder = eventsrecorder.__main__:main',
        ]
    }
)
