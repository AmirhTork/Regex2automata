from setuptools import setup, find_packages

setup(
    name="regex2automata",
    version="1.0.0",
    description="Convert regular expressions to NFA, DFA, and minimized DFA with visualization support.",
    author="Amirhossein Tork",
    author_email="ahtpub@example.com",
    url="https://github.com/AmirhTork/regex2automata",
    packages=find_packages(),
    install_requires=[
        "graphviz>=0.20.1",
    ],
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "regex2automata=regex2automata.cli:main",
        ]
    },
    include_package_data=True,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Topic :: Text Processing :: Linguistic",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Environment :: Console",
    ],
)
