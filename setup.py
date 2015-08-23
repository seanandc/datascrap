from setuptools import setup, find_packages

setup(
    name='DataScrap',
    version='0.0.1',
    description='a description goes here',
    url='https://github.com/seanandc/datascrap',
    author='seanandc',
    author_email='emailhere',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 2.7',
    ],
    keywords='experimental',
    packages=find_packages(exclude=['docs',]),
    install_requires=['requests>=2.7.0','beautifulsoup4>=4.4.0'],
    # pip install -e .['dev','test]
    extras_require={
        'dev': [],
        'test': [],
    }
)