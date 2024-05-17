from setuptools import setup

with open("requirements.in") as requirements_file:
    requirements = [l for l in requirements_file.read().splitlines() if l and not l.startswith("--") and not l.startswith("#")]

setup(
    name='shhhhhhhhhhhhhhhhhhhhhhh',
    version='0.0.1',
    author='Scott Pierce',
    author_email='ddrscott@gmail.com',
    description='A package to help transcribe stuff,',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/ddrscott/shhhhhhhhhhhhhhhhhhhhhhh',
    packages=['shhhhhhhhhhhhhhhhhhhhhhh'],
    package_dir={'':'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    install_requires=requirements,
    entry_points={
        'console_scripts':[
            "shhhhhhhhhhhhhhhhhhhhhhh = shhhhhhhhhhhhhhhhhhhhhhh.cli:cli",
        ],
    }
)
