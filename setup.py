from pathlib import Path
from setuptools import setup

setup(
    name="the-flx",
    description="Rewrite emacs-flx in Python",
    version="0.1.2",
    url="https://github.com/the-flx/flx.py",
    project_urls={
        "Source Code": "https://github.com/the-flx/flx.py",
    },
    author="Jen-Chieh Shen",
    author_email="jcs090218@gmail.com",
    license="MIT",
    python_requires=">=3.9",
    packages=["flx"],
    install_requires= [],
    long_description=Path("README.md").read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
)
