import setuptools

long_description = """Basthon's Turtle module port to Pytuga Web project."""

setuptools.setup(
    name="turtle",
    version="0.0.1",
    author="Andrew Lucas",
    author_email="andrewlucasgs@gmail.com",
    description=long_description,
    long_description=long_description,
    url="https://github.com/andrewlucasgs/turtle-for-pytuga-web",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Interpreters",
        "Operating System :: OS Independent",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Programming Language :: Python :: 3",
    ],
    python_requires='>=3.4',
)
