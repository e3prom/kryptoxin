# PowerShell

Kryptoxin supports [PowerShell](https://learn.microsoft.com/en-us/powershell/) as an output language for script templates.

## Overview

The PowerShell execution environment is a well known attack vector for Windows hosts. It stems from the fact that a lot of system utilities and libraries are using it. These libraries can be leveraged to get information about a Windows-based system. The execution environment also supports access to native API functions via .NET reflection methods.

## Print Script (`print`)

The `print` template generates a basic printing script. The latter can be used to "transmit" a secret string to a target, as a starting script or even be used for debugging purposes.

### Usage Example

The below example shows a PowerShell script which include a base64 decoding function and routines to perform AES decryption; all using system libraries only. This script can be readily copy/pasted to a windows host. Upon execution, it will print the encrypted message to the console of the target host.

=== "Generate an encrypted message"
    ```{.sh .no-copy}
    $ python -m kryptoxin encrypt -k s3cret --random-iv --random-salt \
    --lang powershell --action print
    this is a secret message.
    2023-03-04 13:42:09,010 - INFO - The Initialization Vector (IV) is: d086829cb5dc86fd7d96fb886961535a
    2023-03-04 13:42:09,010 - INFO - The PBKDF2 Salt is: 65bb0cb28ded98aa90948d1d17d33c3e

    $base64EncData = "IJwkiZX5xSgNSKWhViyAvljc8A8omkslt9zlG+wUzXM="



    function ConvertFrom-Base64ToByteArray {
    [...]

    [System.Text.Encoding]::UTF8.GetString($data)
    ```
