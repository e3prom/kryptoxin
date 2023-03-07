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
    - [With git (v0.9.6)](#with-git-v096)
  - [Usages](#usages)
    - [Read, Encrypt and Decrypt from stdin](#read-encrypt-and-decrypt-from-stdin)
    - [Read and Encrypt from a file](#read-and-encrypt-from-a-file)
    - [Encrypt using AES-128-CBC](#encrypt-using-aes-128-cbc)
    - [Generate a PowerShell `print` script](#generate-a-powershell-print-script)
  - [Documentation](#documentation)
  - [Disclaimer](#disclaimer)
  - [License](#license)

## Description

Kryptoxin is a Python tool allowing you to generate encrypted payloads effortlessly. This software is primarily intended for use in the security field for storing encrypted objects on target hosts. It can also be used for concealing scripts and binary objects from scrutiny.

The name `Kryptoxin` comes from the contraction of `Kryptos` (meaning `conceal`, `hidden` or `secret` in Greek) and the word `Toxin` (meaning `poison`). As the name implies, the intended goal of this project is to provide a fast and efficient way of concealing or hiding payloads, thus saving you a lot of time and effort. Most of our templates are "living off the land", using system libraries and encryption routines commonly found in base operating systems installations.

## Features

The below features are supported:

- Provides block-cipher encryption algorithms such as the `Advanced Encryption Standard` or `AES`.
- Supports user-specifiable key sizes and block-cipher modes of operations, such as `AES256-CBC`.
- Generate random cryptographic parameters such as `Initialization Vector` and `Salt`.
- Encodes and properly formats variables for fast and streamlined copy/paste operations.
- Handles `Text Files`, `Scripts`, `Portable Executables (PE)`, `Dynamic Link Libraries (DLLs)`, and `shellcodes` objects.
- Generates compact, portable scripts or source codes as outputs for the below programming languages:
  - [x] PowerShell
  - [x] C#
  - [ ] C++
  - [ ] C
- Implement key derivation functions, such as `PBKDF2`.
- Supports out-of-band key storage, with conditional trigger mechanisms (not yet available).
- Includes scripts and source code templates to be used for security-related tasks and experimentation.

## Installation

### With pip (latest release)

``` sh
pip install kryptoxin
```

### With git (v0.9.6)

``` sh
git clone https://github.com/e3prom/kryptoxin
cd kryptoxin
git checkout tags/0.9.6
sudo make install
```

## Usages

### Read, Encrypt and Decrypt from stdin

``` {sh .no-copy}
$ echo -n 'test' | python -m kryptoxin encrypt -k 12345
5bP32GKoJa57IcKL4sWeUQ==

$ echo -n '5bP32GKoJa57IcKL4sWeUQ==' | python -m kryptoxin decrypt -k 12345
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
gtsUB3pIqtJk/dSqm6phrA==
```

### Generate a PowerShell `print` script

``` {sh .no-copy}
$ python -m kryptoxin encrypt -k secret --random-iv --random-salt --lang powershell --action print
This is a secret!
2023-03-04 17:33:42,287 - INFO - The Initialization Vector (IV) is: c15c8447204e9025a8ef1e4dd2ea80da
2023-03-04 17:33:42,287 - INFO - The PBKDF2 Salt is: 85858c9115145be223d36750464b8026

$base64EncData = "3Ud7pHQPm/qWOjgtuNOXP2WclPMxz6VuhfRTnwNXDyg="
[...]
```

## Documentation

You can directly visit the [online documentation](https://e3prom.github.io/kryptoxin/) or build it locally using the `make docs` command.

## Disclaimer

This program is distributed "AS IS" without any warranty or conditions of any kind. Under no circumstances can the developers, maintainers, or contributors be held responsible for the improper use of this software. Any damages or consequences resulting from the direct or indirect operation of this software cannot be attributed to the above-mentioned individuals or organizations. All opinions and knowledge expressed in the source codes, documentation, templates and examples are provided for educational and demonstration purposes only. By using this software you agree to the terms expressed therein.

## License

Kryptoxin is released under the AGPL-3 license. See [LICENSE](LICENSE) for more detail.
