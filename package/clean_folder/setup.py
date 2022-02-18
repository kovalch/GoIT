import setuptools

setuptools.setup(
    name="clean-my-folder",
    version="0.0.1",
    author="Nataliia Kovalchuk",
    author_email="nataliia.kovalchuk90@gmail.com",
    description="Cleanup wanted folder",
    long_description="Cleanup wanted folder",
    long_description_content_type="text/markdown",
    url="https://github.com/kovalch/GoIT",
    project_urls={
        "Bug Tracker": "https://github.com/kovalch/GoIT/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        'console_scripts': [
            'clean-folder = clean_folder.clean:sort_all_files',
        ],
    },
)