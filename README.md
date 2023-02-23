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
    - [With pip](#with-pip)
    - [With git](#with-git)
  - [Usage](#usage)
    - [Read and encrypt from a file](#read-and-encrypt-from-a-file)
    - [Read from stdin and encrypt using AES-128-CBC](#read-from-stdin-and-encrypt-using-aes-128-cbc)
  - [Documentation](#documentation)
  - [License](#license)

## Description

Kryptoxin is a Python tool allowing you to quickly and easily generate encrypted payloads. It supports various object types and various programming languages. This software is intended for use in the security field for storing encrypted objects on target hosts. It can also be used for concealing scripts and binary objects from scrutiny.

The name `Kryptoxin` comes from the contraction of `Kryptos` (meaning `conceal`, `hidden` or `secret` in Greek) and the word `Toxin` (meaning `poison`). As the name implies, the intended goal of this project is to provide a fast and efficient way of concealing or hiding payloads such as implants, thus avoiding AV and EDR detection. Most of our templates are "living off the land", using libraries and encryption routines commonly found in base operating systems installations.

## Features

- Supports `Text Files`, `Scripts`, `Portable Executables (PE)`, `Dynamic Link Libraries (DLLs)`, and `shellcodes` as inputs.
- Generates compact, portable scripts or source codes as outputs for the below languages:
  - [ ] PowerShell
  - [ ] C
  - [ ] C++
  - [ ] C# (.NET)
- Provides multiple block cipher algorithms, key sizes and modes of operations, such as `AES256-CBC`.
- Implements key derivations functions such as `PBKDF2`.
- Offers proper encoding and formatting schemes for usage-specific variables.
- Supports out-of-band key storage, with conditional trigger mechanisms.
- Includes scripts and source code templates to be used for security-related tasks and experimentation.

## Installation

### With pip

``` sh
pip install kryptoxin
```

### With git

``` sh
git clone https://github.com/e3prom/kryptoxin
cd kryptoxin
python setup.py install
```

## Usage

### Read and encrypt from a file

``` {sh .no-copy}
$ python -m kryptoxin encrypt -k 12345 -i input_file.txt
tRQYHkQkS9Z7z7i7rzmJSPTuOfE2UUUERsR9CRtdwSM=
```

### Read from stdin and encrypt using AES-128-CBC

``` {sh .no-copy}
$ echo -n 'test' | python -m kryptoxin encrypt -k 12345 --alg aes --key_size 128 --mode CBC
Z+1df03i+mSayvEFYB+rmB55N4dYoz7Rbr2LhzNjqH8=
```

## Documentation

You can directly visit the [online documentation](https://e3prom.github.io/kryptoxin/) or build it locally using the `make docs` command.

## License

Kryptoxin is released under the AGPL-3 license. See [LICENSE](LICENSE) for more detail.
