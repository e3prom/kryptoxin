# Reference

Kryptoxin is supporting various encryption features and options, this section of the documentation lists and details the internal parameters of the tool.

## Default Parameters

To keep the usage simple and streamlined, Kryptoxin implicitly uses parameters by default. Some of them have been selected due to their wide support across frameworks and operating systems. Therefore, most of the time you don't have to explicitly specify them to achieve a specific goal such as encrypting a payload.

### Encryption and Decryption

* Encryption Algorithm: `Advanced Encryption Standard` or `AES`
* Encryption key size: `256 bits`
* Block Cipher Mode of Operation: `Cipher Block Chaining` or `CBC`
* Key-Derivation Function: `PBKDF2`
    * Hash-Based Message Authentication Code (HMAC): `SHA-1`
    * Iteration Count: `10000`
    * Derived Key Length: `32 bytes`
* Initialization Vector (IV): `0x0` (16 bytes)
* IV Prepending: `Disabled` (as of version 0.9.5)
* Salt: `0x0` (16 bytes)
* Padding: `PKCS#7`

### Output

* File Encoding: `UTF-8` (Linux/Unix)
* Data Encoding: `base64`

## Supported Parameters

### Command-line Options

By using the command-line options, you can control and fine tune the encryption and decryption operations.

#### Cryptographic Options

The options listed below allow you to control the various cryptographic parameters:

???+ warning "Recommended use of the Initialization Vector"
    By default, Kryptoxin uses a null or all-zero Initialization vector (IV). This is inherently **insecure**, but allow for a easy decryption operations when handling codes over various operating systems and frameworks. For maximum privacy and security, the use of a random IV (`--random-iv` option) is strongly recommended.

* Encryption Key (`-k`, `--key`)
* Key Size (`-s`, `--key_size`)
    * Support between 256 and 4096 bits keys.
* Encryption Algorithms (`-a`, `--alg`)
    * Advanced Encryption Standard: `AES`
* Block Cipher Mode of Operations (`-m`, `--mode`)
    * Cipher Block Chaining: `CBC`
    * Cipher Feedback: `CFB`
    * Output FeedBack: `OFB`
    * Encrypt-then-Authenticate-then-Translate: `EAX`
* Initialization Vector (`--iv`)
    * Generate a random iv: `--random-iv`
* Salt (`--salt`)
    * Generate a random salt: `--random-salt`
* Hash-based Message Authentication Code Algorithms (`-h`, `--hmac`)
    * `SHA1`
    * `SHA256`
    * `SHA512`
* PBKDF2 Iteration Count (`--iter`)

### Templates Options

When using templates, you must specify the output programming language and the desired action.

* Output Programming Language (`-l`, `--lang`)
    * `powershell`
* Action (`-a`, `--action`)
    * PowerShell Script
        * `print`: Print the plaintext directly onto the console after decryption.
