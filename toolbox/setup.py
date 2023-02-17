import setuptools


setuptools.setup(
    name='toolbox',
    version='0.0.1',
    author='Hong Zhu',
    author_email='zhuhong@microsoft.com',
    description='Example customized package',
    url='https://github.com/felihong/Azure-functionapps-demo/tree/main/custom_pkg',
    license='MIT',
    packages=['toolbox'],
    install_requires=['requests'],
)