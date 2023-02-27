# Reference

Kryptoxin is supporting various encryption features and options, this section of the documentation lists and details the internal parameters of the tool.

## Default Parameters

To keep the usage simple and streamlined, Kryptoxin implicitly uses parameters by default. Some of these have been selected due to their wide support across frameworks and operating systems. Therefore, most of the time you don't have to explicitly specify them to achieve a specific goal such as encrypting a payload.

### Encryption and Decryption

* Encryption Algorithm: `Advanced Encryption Standard` or `AES`
* Encryption key size: `256 bits`
* Block Cipher Operation Mode: `Cipher Block Chaining` or `CBC`
* Key-Derivation Function: `PBKDF2`
  * Hash-Based Message Authentication Code (HMAC): `SHA-1`
  * Iteration Count: `10000`
  * Derived Key Length: `32 bytes`
* Initialization Vector (IV): `0x0` (16 bytes)
* IV Prepending: `Yes` (before encryption)
* Salt: `0x0` (16 bytes)
* Padding: `PKCS#7`

### Output

* File Encoding: `UTF-8` (Linux/Unix)
* Data Encoding: `base64`
