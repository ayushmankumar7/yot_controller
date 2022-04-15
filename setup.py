from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name = 'Yot',
    version = '1.0.0',
    author = "Ayushman Kumar",
    author_email="ayushmankumar7@gmail.com",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/ayushmankumar7/yot_controller",
    packages = find_packages(),
    entry_points = {
        'console_scripts': [
            'yot = yot.__main__:main', 
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],

    
    )