import setuptools 


setuptools.setup(
    name='mytoolbox',
    version='0.0.1',
    author='Hong Zhu',
    author_email='zhuhong@microsoft.com',
    description='Example customized package',
    url='https://github.com/felihong/Azure-functionapps-demo',
    license='MIT',
    packages=['mytoolbox'],
    install_requires=['requests'],
)