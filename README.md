# Kryptoxin

[![Latest Release](https://img.shields.io/github/release/e3prom/Kryptoxin.svg?style=for-the-badge)](https://github.com/e3prom/Kryptoxin/releases)
[![Software License](https://img.shields.io/badge/license-GPL-blue.svg?style=for-the-badge)](/LICENSE)

- [Kryptoxin](#kryptoxin)
  - [Description](#description)
  - [Features](#features)
  - [Usage](#usage)
    - [Read and encrypt from a file](#read-and-encrypt-from-a-file)
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

## Usage

### Read and encrypt from a file

```sh
$ python -m kryptoxin encrypt -k 12345 -i input_file.txt
tRQYHkQkS9Z7z7i7rzmJSPTuOfE2UUUERsR9CRtdwSM=
```

## License

The Kryptoxin tool is released under the GPL-3 license. See [LICENSE](LICENSE) for more detail.
