# Getting started

Kryptoxin is a software written in Python and can be easily installed by cloning the official project's repository or by using a package installer such as `pip`.

## Installation

### With pip <small>recommended</small> { #with-pip data-toc-label="with pip" }

Open up a terminal and install Kryptoxin using pip:

=== "Latest"

    ``` sh
    pip install kryptoxin
    ```
=== "0.9.6"

    ``` sh
    pip install kryptoxin==0.9.6
    ```

The above commands will automatically install all the required dependencies.

### With git { #with-source data-toc-label="with git" }

First make sure you have `git` installed. Then, fetch the source code from the official [Kryptoxin repository](https://github.com/e3prom/kryptoxin), next checkout the latest production release and finally install the `kryptoxin` module and all its dependencies on your system:

=== "Latest Development"

    ``` sh
    git clone https://github.com/e3prom/kryptoxin
    cd kryptoxin
    sudo make install
    ```

=== "0.9.6"

    ``` sh
    git clone https://github.com/e3prom/kryptoxin
    cd kryptoxin
    git checkout tags/0.9.6
    sudo make install
    ```
