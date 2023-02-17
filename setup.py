from setuptools import setup, find_packages


setup(
    name='toolbox',
    version='0.0.1',
    author='Hong Zhu',
    author_email='zhuhong@microsoft.com',
    description='Example customized package',
    url='https://github.com/felihong/Azure-functionapps-demo',
    license='MIT',
    packages=find_packages('toolbox'),
    package_dir={'': 'toolbox'},
    install_requires=['requests'],
)