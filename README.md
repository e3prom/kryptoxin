# Kryptoxin

[![Latest Release](https://img.shields.io/github/release/e3prom/Kryptoxin.svg?style=for-the-badge)](https://github.com/e3prom/Kryptoxin/releases)
[![GitHub issues](https://img.shields.io/github/issues-raw/e3prom/kryptoxin?style=for-the-badge)](https://github.com/e3prom/kryptoxin/issues)
[![GitHub Workflow - Docs](https://img.shields.io/github/actions/workflow/status/e3prom/kryptoxin/docs-deploy.yml?label=docs&style=for-the-badge)](https://e3prom.github.io/kryptoxin/)
[![GitHub Workflow - Tests](https://img.shields.io/github/actions/workflow/status/e3prom/kryptoxin/python-unittest.yml?label=Tests&style=for-the-badge)](https://github.com/e3prom/kryptoxin/actions/workflows/python-unittest.yml)
[![License](https://img.shields.io/github/license/e3prom/kryptoxin?style=for-the-badge)](https://raw.githubusercontent.com/e3prom/kryptoxin/master/LICENSE)

- [Kryptoxin](#kryptoxin)
  - [Description](#description)
  - [Features](#features)
  - [Installation](#installation)
    - [With pip (latest release)](#with-pip-latest-release)
    - [With git (development version)](#with-git-development-version)
  - [Usages](#usages)
    - [Read, Encrypt and Decrypt from stdin](#read-encrypt-and-decrypt-from-stdin)
    - [Read and Encrypt from a file](#read-and-encrypt-from-a-file)
    - [Encrypt using AES-128-CBC](#encrypt-using-aes-128-cbc)
  - [Documentation](#documentation)
  - [License](#license)

## Description

Kryptoxin is a Python tool allowing you to quickly and easily generate encrypted payloads. It supports various object types and various programming languages. This software is intended for use in the security field for storing encrypted objects on target hosts. It can also be used for concealing scripts and binary objects from scrutiny.

The name `Kryptoxin` comes from the contraction of `Kryptos` (meaning `conceal`, `hidden` or `secret` in Greek) and the word `Toxin` (meaning `poison`). As the name implies, the intended goal of this project is to provide a fast and efficient way of concealing or hiding payloads such as implants, thus avoiding AV and EDR detection. Most of our templates are "living off the land", using libraries and encryption routines commonly found in base operating systems installations.

## Features

The features below are currently supported, or are planned to be released in the near future:

- Provides encryption algorithms such as the `Advanced Encryption Standard` or `AES`.
- Provides decryption of base64 encoded ciphertext.
- Handles `Text Files`, `Scripts`, `Portable Executables (PE)`, `Dynamic Link Libraries (DLLs)`, and `shellcodes`.
- Generates compact, portable scripts or source codes as outputs for the below programming languages (not yet available):
  - [ ] PowerShell
  - [ ] C
  - [ ] C++
  - [ ] C# (.NET)
- Supports multiple block cipher algorithms, key sizes and modes of operations, such as `AES256-CBC`.
- Implements key derivations functions such as `PBKDF2`.
- Offers proper encoding and formatting schemes for usage-specific variables.
- Supports out-of-band key storage, with conditional trigger mechanisms (not yet available).
- Includes scripts and source code templates to be used for security-related tasks and experimentation (not yet available).

## Installation

### With pip (latest release)

``` sh
pip install kryptoxin
```

### With git (development version)

``` sh
git clone https://github.com/e3prom/kryptoxin
cd kryptoxin
sudo make install
```

## Usages

### Read, Encrypt and Decrypt from stdin
``` {sh .no-copy}
$ echo -n 'test' | python -m kryptoxin encrypt -k 1234
tRQYHkQkS9Z7z7i7rzmJSPTuOfE2UUUERsR9CRtdwSM=

$ echo -n 'tRQYHkQkS9Z7z7i7rzmJSPTuOfE2UUUERsR9CRtdwSM=' | \
> python -m kryptoxin decrypt -k 12345
test
```

### Read and Encrypt from a file

``` {sh .no-copy}
$ python -m kryptoxin encrypt -k 12345 -i input_file.txt
tRQYHkQkS9Z7z7i7rzmJSPTuOfE2UUUERsR9CRtdwSM=
```

### Encrypt using AES-128-CBC

``` {sh .no-copy}
$ echo -n 'test' | python -m kryptoxin encrypt -k 12345 --alg aes --key_size 128 --mode CBC
Z+1df03i+mSayvEFYB+rmB55N4dYoz7Rbr2LhzNjqH8=
```

## Documentation

You can directly visit the [online documentation](https://e3prom.github.io/kryptoxin/) or build it locally using the `make docs` command.

## License

Kryptoxin is released under the AGPL-3 license. See [LICENSE](LICENSE) for more detail.
