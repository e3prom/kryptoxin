# Usages

Kryptoxin can be used in a wide variety of scenarios and contexts. All the examples below assumes we will be using it for security purposes, let's say for a Red Team engagement.

To use Kryptoxin, pass the `kryptoxin` module to your Python interpreter using the `python -m kryptoxin` command. You can use the `--option` command-line parameter at any given time to lists the available options:

``` { .sh .no-copy }
Usage: python -m kryptoxin [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  encrypt  This command perform encryption on the supplied input.
  decrypt  This command perform decryption on the supplied input.
```

## Encryption (`encrypt`)

As the name implies the `encrypt` command perform encryption on the supplied input.

!!! info "Default encryption parameters"
    By default Kryptoxin uses the `AES` symmetric algorithm with a 256-bits key. The block cipher operation mode is `CBC` and uses the key-derivation function `PBKDF2` with the `SHA-1` digest algorithm. These parameters have been selected because they are widely supported across languages and framework such as `PowerShell` and `.NET` .

???+ warning "Mandatory command-line option"
    Only one command-line option is required and mandatory to perform payload encryption, namely the `-k` or `--key` option. If a file is not provided using the `-i` or `--in` option, it will read the standard input (or stdin); when omitted, kryptoxin will prompt you and read your input until you hit the ++ctrl+d++ keys.

### Basic Encryption

The commands below perform encryption using the default parameters and options:

=== "Read from the standard input"
    ```{.sh .no-copy}
    $ echo -n 'test' | python -m kryptoxin encrypt -k 12345
    tRQYHkQkS9Z7z7i7rzmJSPTuOfE2UUUERsR9CRtdwSM=
    ```

=== "Read from a file"
    ```{.sh .no-copy}
    $ python -m kryptoxin encrypt -k 12345 -i input_file.txt
    tRQYHkQkS9Z7z7i7rzmJSPTuOfE2UUUERsR9CRtdwSM=
    ```


??? question "What the above commands do ?"

    Let's break down the above commands, options and outputs:

    - `python -m kryptoxin` calls the `kryptoxin` module, which should be in your `sys.path` after installation.
    - The `-k 12345` option provide the encryption key to be passed to the block cipher algorithm.
    - Finally, `-i input_file.txt` specify the input file to read from, here a standard text file.
    - Alternatively, you can use the standard Unix/Linux pipes to redirect the output to the standard input.
    
    Once the encryption operation is performed, Kryptoxin will return a base64 encoded output by default. The latter can be copy/pasted into variables, or can be stored in a file by using the `-o` or `--out` command-line option.

### Encrypt to a file

To encrypt a binary file such as a Dynamic Link Library (or .dll), you can use the command below:

```{.sh .no-copy}
$ python -m kryptoxin encrypt --key 12345 --key_size 128 \
--in MediaConverter.dll --alg AES --hmac SHA256 --mode CBC \
--iv 0000000000000001 --out MediaConverter.dll.encrypted
```

??? question "What the above command-line options do ?"
    For this example we use the `AES` block cipher algorithm with a 128-bits key. We also specify the `SHA256` digest algorithm for the `HMAC` function. The block cipher operation mode is `CBC` and its initialization vector is manually specified. The latter must matches the block cipher's block size, which is 16 bytes. Finally, the output is written to the file specified by the `--out` command-line option.

## Decryption (`decrypt`)

The `decrypt` command as the name implies, allow you to perform decryption on a given `ciphertext`. If the decryption process is successful, kryptoxin will write the `plaintext` directly on the console standard output or will write the result in the file given by the `--out` option.

### Quick Decryption

To perform "a quick" decryption of a given input with the default parameters and options, you can use the command below:

=== "Read from the standard input"
    ```{.sh .no-copy}
    $ echo 'tRQYHkQkS9Z7z7i7rzmJSPTuOfE2UUUERsR9CRtdwSM=' | \
    > python -m kryptoxin decrypt -k 12345
    test
    ```

=== "Read from a file"
    ```{.sh .no-copy}
    $ python -m kryptoxin decrypt -k 12345 -i encrypted.txt
    test
    ```
