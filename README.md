# Lazyls - A light weight navigator

## Demo

![demo](img/lazyls_demo.gif)

## Install

```bash
$ cd ~
$ git clone https://github.com/LIU-Xnd/lazyls.git
```
After downloading, add this to your `.bashrc`:
```bash
# Replace this path to where this project is placed
export lz_path_="$HOME/lazyls"

function lz () { source "$lz_path_/src/lazyls.sh"; }
```

## Get Started

After installation,
```bash
$ lz  # ls -a preceeded with indices, followed by interactive navigation
```