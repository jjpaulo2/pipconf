# PIPCONF - The PIP configuration manager

![](screenshot.png)

If you need to manage multiple configurations containing indexes and trusted hosts for PIP, this project was made for you.

### Introduction

The `pipconf` is based in `pip.conf` files in `$HOME/.pip` folder. But you won't create it with this name. So, you need to create your configuration files following the template `config-file-name.conf`. 

For the first steps, create a `$HOME/.pip` folder.
```shell
# Create the folder, and enter it
$ mkdir $HOME/.pip
$ cd $HOME/.pip

# Create 2 files inside .pip folder
$ touch personal-config.conf company-config.conf
```

Inside the files, you can put the configurations like `index-url`, `timeout`, `extra-index-url`, `trusted-host`, etc. You can confer [here](https://pip.pypa.io/en/stable/user_guide/#configuration) all the options.

```toml
<!-- personal-config.conf -->

[global]
index-url = https://pypi.org/simple/
trusted-host = pypi.org
```

```toml
<!-- company-config.conf -->

[global]
index-url = http://mycompany.com/artifactory/api/pypi/pypi/simple
extra-index-url = http://mycompany.com/artifactory/api/pypi/pypi-local/simple/
trusted-host = mycompany.com
```

## Instalation

This project uses only pure Python. So, you don't need to install any project dependencies. Just run the `setuptools` installer.

```shell
$ python setup.py install
```

Coming soon, the package will be avaliable at PyPI.

## Usage

```shell
$ pipconf --help
```
The expected output should be something like the following content.

    usage: pipconf [-h] [--current] [--list] [--set FILENAME] [--local]

    ______ ___________  _____ _____ _   _ ______
    | ___ \_   _| ___ \/  __ \  _  | \ | ||  ___|
    | |_/ / | | | |_/ /| /  \/ | | |  \| || |_
    |  __/  | | |  __/ | |   | | | | . ` ||  _|
    | |    _| |_| |    | \__/\ \_/ / |\  || |
    \_|    \___/\_|     \____/\___/\_| \_/\_|  v0.1.0

    Under BSD-2-Clause License, by @jjpaulo2
    Contribute at https://github.com/jjpaulo2/pipconf

    optional arguments:
    -h, --help      show this help message and exit

    display informations:
    --current       show the current pip configuration file
    --list          list all user configurations avaliable at $HOME/.pip

    change configuration:
    --set FILENAME  set the global configuration for pip from a file in $HOME/.pip
    --local         set the pip configuration for the current directory file


### Querying the current configuration file

```shell
$ pipconf --current
```

This command will show the current file used. If you are not using anyone, it will show it too.

    The current pip configuration file is /home/jjpaulo2/.pip/personal-config.conf

### Querying the avaliable configuration files in `$HOME/.pip`

```shell
$ pipconf --list
```

This command will show the avaliable configuration files in `$HOME/.pip` folder. If someone of then is being used, you will see a `*` simbol at it left.

    * personal-config (/home/jjpaulo2/.pip/personal-config.conf)
      company-config (/home/jjpaulo2/.pip/company-config.conf)

### Setting a file from `$HOME/.pip` as current configuration file

```shell
$ pipconf --set company-config
```

This will update the current file used, and will output the following message.

    Current pip configuration successfully updated.
    The active config file is /home/jjpaulo2/.pip/company-config.conf

### Setting a `pip.conf` file from the current working directory

```shell
$ ls
pip.conf ...
```

If the current directory you are in, have a `pip.conf` file, then you can just active it.

```shell
pipconf --local
```

The output should be something like the following content.

    Geting configuration file from current directory.
    The active config file is /home/jjpaulo2/dev/myproject/pip.conf