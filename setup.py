from setuptools import setup


setup(
    name='example_project',
    version='0.1',
    author='Tarek Mehrez',
    description='Python project skeleton',
    packages=['example_project',
              'example_project.sub_module_1',
              'example_project.sub_module_2'],
    scripts=['bin/example_script']
)
