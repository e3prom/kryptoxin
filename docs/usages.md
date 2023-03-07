# Usages

To use Kryptoxin, pass the `kryptoxin` module to your Python interpreter using the `python -m kryptoxin` command. You can use the `--help` command-line parameter at any given time to lists the available options for a specific command:

``` { .sh .no-copy }
Usage: python -m kryptoxin [OPTIONS] COMMAND [ARGS]...

Options:
  --version  Show the version and exit.
  --help     Show this message and exit.

Commands:
  encrypt  This command perform encryption on the supplied input.
  decrypt  This command perform decryption on the supplied input.
```

At this time of writing, Kryptoxin supports the `encrypt` and `decrypt` commands. As their name implies they are used to respectively perform encryption and decryption of a given input.

## Encryption (`encrypt`)

As the name implies the `encrypt` command perform encryption on the supplied input.

!!! info "Default encryption parameters"
    By default Kryptoxin uses the `AES` symmetric algorithm with a 256-bits key. The block cipher operation mode is `CBC` and uses the key-derivation function `PBKDF2` with the `SHA-1` digest algorithm. These parameters have been selected because they are widely supported by popular languages and frameworks such as `PowerShell` and `.NET`.

???+ warning "Mandatory command-line option"
    Only one command-line option is required and mandatory to perform payload encryption, namely the `-k` or `--key` option. If a file is not provided using the `-i` or `--in` option, Kryptoxin will read on the standard input (or stdin) until you hit the ++ctrl+d++ keys combination.

### Quick Encryption

The commands below perform encryption using the default parameters and options:

=== "Read from the standard input"
    ```{.sh .no-copy}
    $ echo -n 'test' | python -m kryptoxin encrypt -k 12345
    5bP32GKoJa57IcKL4sWeUQ==
    ```

=== "Read from a file"
    ```{.sh .no-copy}
    $ python -m kryptoxin encrypt -k 12345 -i input_file.txt
    5bP32GKoJa57IcKL4sWeUQ==
    ```

??? question "What the above commands do ?"
    Let's break down the above commands, options and outputs:

    - `python -m kryptoxin` calls the `kryptoxin` module, which should be in your `sys.path` after installation.
    - The `-k 12345` option provide the encryption key to be passed to the block cipher algorithm.
    - Finally, `-i input_file.txt` specify the input file to read from, here a text file.
    - Alternatively, you can use the standard Unix/Linux pipes to redirect the output to the standard input or the other way around.
    
    Once the encryption operation is performed, Kryptoxin will return a base64 encoded output by default. The latter can be copy/pasted into variables, or can be stored in a file by using the `-o` or `--out` command-line option.

### Fine-tuned AES Encryption

#### Encrypt a .dll to a file

To encrypt a binary file such as a Dynamic Link Library (or .dll), you can use the command below:

```{.sh .no-copy}
$ python -m kryptoxin encrypt --key 12345 --key_size 128 \
--in MediaConverter.dll --alg AES --hmac SHA256 --mode CBC \
--iv 17ad017117ed47f902c524cd4351d0f9 --out MediaConverter.dll.encrypted
```

??? question "What the above command-line options do ?"
    For this example we use the `AES` block cipher algorithm with a 128-bits key. We also specify the `SHA256` digest algorithm for the `HMAC` function. The block cipher operation mode is `CBC` and its initialization vector is manually specified. The latter must match the block cipher's block size, which is here 16 bytes. Finally, the output is written to the file specified by the `--out` command-line option.

## Decryption (`decrypt`)

The `decrypt` command as the name implies, allow you to perform decryption of a given `ciphertext`. If the decryption process is successful, kryptoxin will write the `plaintext` directly on the console's standard output or will write the result into the file given by the `--out` option.

### Quick Decryption

To perform "a quick" decryption of a given input with the default parameters and options, you can use the command below:

=== "Read from the standard input"
    ```{.sh .no-copy}
    $ echo '5bP32GKoJa57IcKL4sWeUQ==' | python -m kryptoxin decrypt -k 12345
    test
    ```

=== "Read from a file"
    ```{.sh .no-copy}
    $ python -m kryptoxin decrypt -k 12345 -i encrypted.txt
    test
    ```
