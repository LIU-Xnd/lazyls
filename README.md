# Lazyls - A light weight navigator

## Install

```bash
$ cd ~
$ git clone https://github.com/LIU-Xnd/lazyls.git
```
After downloading, add this to your `.bashrc`:
```bash
# Replace this path to where this project is placed
export lz_path_="$HOME/lazyls"

export lz(){
    source $lz_path_/src/lazyls.sh
}
```

## Get Started

After installation,
```bash
$ lz  # ls -a preceeded with indices, followed by interactive navigation
```