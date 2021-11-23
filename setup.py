from setuptools import find_packages, setup

setup(
    name="decontractions",
    packages=find_packages(),
    version="0.1.1",
    license="MIT",
    description="Expand common English contractions in text.",
    author="Akmal",
    author_email="akmal@depia.wiki",
    url="https://github.com/Wikidepia/decontractions",
    package_data={"decontractions": ["*.json"]},
    install_requires=[
        "kenlm@https://github.com/kpu/kenlm/archive/master.zip",
    ],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
    ],
)
