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

First make sure you have `git` installed. Fetch the source code from the official Kryptoxin repository, and install the required the dependencies:

=== "Latest Development"

    ``` sh
    git clone https://github.com/e3prom/kryptoxin
    cd kryptoxin
    python setup.py install
    ```

=== "0.9.1"

    ``` sh
    git clone https://github.com/e3prom/kryptoxin
    cd kryptoxin
    git checkout tags/0.9.1
    python setup.py install
    ```
