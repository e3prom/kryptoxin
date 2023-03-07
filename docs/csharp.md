# C\# (.NET)

Kryptoxin supports the [C# programming language](https://learn.microsoft.com/en-us/dotnet/csharp/) as an output language for templates.

## Overview

The C# language is very valuable in the security field, as it provides access to the .NET framework capabilities. Managed programs and DLLs can be written to perform system API calls while granting access to more sophisticated functions such as AES decryption.

All templates shipped with Kryptoxin can be directly pasted into [Visual Studio](https://visualstudio.microsoft.com) (we recommended versions >= `2022`) and be compiled without modification.

## Print Program (`print`)

This basic console program simply prints the UTF-8 encoded text encrypted by Kryptoxin. It uses the `System.Security.Cryptography` .NET class, which is widely supported by current Windows hosts.

``` sh
$ python -m kryptoxin encrypt -k s3cret --random-iv --random-salt \
--alg AES --key_size 192 --iter 5000 --lang csharp --action print
```

``` {.c# .no-copy}
using System.Security.Cryptography;

class Program // (1)!
{

    [...]
  
    static void Main(string[] args) // (2)!
    {
        [...]
    }
}
```

1. The class generated must be imported in a `C# .NET Console Program` project.
2. The main entry point is `Main()`, the latter will call the decoding and decryption routines.
