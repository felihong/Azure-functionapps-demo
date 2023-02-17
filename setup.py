import setuptools


setuptools.setup(
    name='custom_toolbox',
    version='0.0.1',
    author='Hong Zhu',
    author_email='zhuhong@microsoft.com',
    description='Example customized package',
    url='https://github.com/felihong/Azure-functionapps-demo/tree/main/custom_toolbox',
    license='MIT',
    packages=['custom_toolbox'],
    install_requires=['requests'],
)