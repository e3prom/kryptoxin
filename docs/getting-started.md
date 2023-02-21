# Getting started

Kryptoxin is a software written in Python and can be easily installed by cloning the official project's repository or by using a package installer such as `pip`.

## Installation

### Using pip <small>recommended</small> { #using-pip data-toc-label="using pip" }

Open up a terminal and install Kryptoxin using pip:

=== "Latest"

    ``` sh
    pip install kryptoxin
    ```
=== "0.9.1"

    ``` sh
    pip install kryptoxin==0.9.1
    ```

The above commands will automatically install all the required dependencies.

### Using git { #using-source data-toc-label="using git" }

First make sure you have `git` installed:

Fetch the source code from the official Kryptoxin repository:

=== "Latest Development"

    ``` sh
    git clone https://github.com/e3prom/kryptoxin
    ```

=== "0.9.1"

    ``` sh
    git clone https://github.com/e3prom/kryptoxin
    git checkout tags/0.9.1
    ```

Enter the repository directory and launch the install script:

```sh
cd kryptoxin
python setup.py install
```
