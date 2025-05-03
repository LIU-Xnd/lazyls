#/bin/bash

$lz_path_/.venv/bin/python $lz_path_/src/lazyls_print.py

target_path=$($lz_path_/.venv/bin/python $lz_path_/src/lazyls_parse.py | grep '::LZOUT::' | cut -f 2) && cd $target_path
