from setuptools import setup, find_packages
#https://godatadriven.com/blog/a-practical-guide-to-using-setup-py/

setup(
    app=["myscript.py"],
    version='0.1.0',
    packages=find_packages(include=['hw', 'hw.*']),
    install_requires=[
        'PyYAML',
        'py2app'
    ]
)