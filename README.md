[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Python Version](https://img.shields.io/badge/Python-3.9+-3E73A0.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Release](https://img.shields.io/github/tag/the-flx/flx.py.svg?label=release&logo=github)](https://github.com/the-flx/flx.py/releases/latest)
[![PyPI - Version](https://img.shields.io/pypi/v/the-flx?logo=pypi)](https://pypi.org/project/the-flx/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/the-flx)](https://pypi.org/project/the-flx/)

# flx.py
> Rewrite emacs-flx in Python

[![CI](https://github.com/the-flx/flx.py/actions/workflows/test.yml/badge.svg)](https://github.com/the-flx/flx.py/actions/workflows/test.yml)
[![Publish](https://github.com/the-flx/flx.py/actions/workflows/publish.yml/badge.svg)](https://github.com/the-flx/flx.py/actions/workflows/publish.yml)

## 🔨 Usage

```python
from flx import flx

print(flx.score("switch-to-buffer", "stb").score)  # 237
```

## 🛠️ Development

This project uses [PyTest][] to do the unit tests.

Simply run `pytest` to run and discover tests:

```sh
$ pytest
```

## 🔗 Links

- [Publishing a Python Package from GitHub to PyPI in 2024](https://medium.com/@blackary/publishing-a-python-package-from-github-to-pypi-in-2024-a6fb8635d45d)

## ⚜️ License

`flx.py` is distributed under the terms of the MIT license.

See [`LICENSE`](./LICENSE) for details.


<!-- Links -->

[flx]: https://github.com/lewang/flx
[Emacs]: https://www.gnu.org/software/emacs/

[PyTest]: https://github.com/pytest-dev/pytest
