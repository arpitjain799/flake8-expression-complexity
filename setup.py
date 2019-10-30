from typing import Optional

from setuptools import setup, find_packages


package_name = 'flake8_expression_complexity'


def get_version() -> Optional[str]:
    with open('flake8_expression_complexity/__init__.py', 'r') as f:
        lines = f.readlines()
    for line in lines:
        if line.startswith('__version__'):
            return line.split('=')[-1].strip().strip("'")
    return None


def get_long_description() -> str:
    with open('README.md') as f:
        return f.read()


setup(
    name=package_name,
    description='A flake8 extension that checks expressions complexity',
    long_description=get_long_description(),
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data=True,
    keywords='flake8',
    version=get_version(),
    author='Ilya Lebedev',
    author_email='melevir@gmail.com',
    install_requires=['setuptools'],
    entry_points={
        'flake8.extension': [
            'ECE = flake8_expression_complexity.checker:ExpressionComplexityChecker',
        ],
    },
    url='https://github.com/best-doctor/flake8-expression-complexity',
    license='MIT',
    py_modules=[package_name],
    zip_safe=False,
)