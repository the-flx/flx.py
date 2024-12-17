[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Release](https://img.shields.io/github/tag/the-flx/flx.py.svg?label=release&logo=github)](https://github.com/the-flx/flx.py/releases/latest)

# flx.py
> Rewrite emacs-flx in Python

[![CI](https://github.com/the-flx/flx.py/actions/workflows/test.yml/badge.svg)](https://github.com/the-flx/flx.py/actions/workflows/test.yml)

## 🔨 Usage

```py
import flx

print(flx.score("switch-to-buffer", "stb).score)  # 237
```

## 🛠️ Development

This project uses [PyTest][] to do the unit tests.

Simply run `pytest` to run and discover tests:

```sh
$ pytest
```

## ⚜️ License

`flx.py` is distributed under the terms of the MIT license.

See [`LICENSE`](./LICENSE) for details.


<!-- Links -->

[flx]: https://github.com/lewang/flx
[Emacs]: https://www.gnu.org/software/emacs/

[PyTest]: https://github.com/pytest-dev/pytest
