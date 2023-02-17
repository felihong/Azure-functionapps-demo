import setuptools


setuptools.setup(
    name='custom-toolbox',
    version='0.0.1',
    author='Hong Zhu',
    author_email='zhuhong@microsoft.com',
    description='Example customized package',
    url='https://github.com/felihong/Azure-functionapps-demo',
    license='MIT',
    packages=['custom-toolbox'],
    install_requires=['requests'],
)