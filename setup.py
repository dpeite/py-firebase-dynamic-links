from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="py-firebase-dynamic-links",
    version="1.0.1",
    author="Daniel Vilar Peiteado",
    author_email="danielvilar2@gmail.com",
    description="Python client for Firebase Dynamic Links API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    maintainer="Daniel Vilar Peiteado",
    maintainer_email="danielvilar2@gmail.com",
    keywords=["firebase", "dynamic links", "url shortener"],
    url="https://github.com/dpeite/py-firebase-dynamic-links",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    install_requires=["requests"],
    project_urls={
        'Bug Reports': 'https://github.com/dpeite/py-firebase-dynamic-links/issues',
        'Source': 'https://github.com/dpeite/py-firebase-dynamic-links',
    },

)