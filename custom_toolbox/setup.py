import setuptools


setuptools.setup(
    name='custom_toolbox',
    author='Hong Zhu',
    author_email='zhuhong@microsoft.com',
    description='Example customized package',
    url='https://github.com/felihong/Azure-functionapps-demo',
    license='MIT',
    packages=['custom_toolbox'],
    install_requires=['requests'],
)