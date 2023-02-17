from setuptools import setup, find_packages


setup(
    name='mytoolbox',
    version='0.0.1',
    author='Hong Zhu',
    author_email='zhuhong@microsoft.com',
    description='Example customized package',
    url='https://github.com/felihong/Azure-functionapps-demo',
    license='MIT',
    packages=find_packages('mytoolbox'),
    package_dir={'': 'mytoolbox'},
    install_requires=['requests'],
)