#/bin/bash

$lz_path_/.venv/bin/python $lz_path_/src/lazyls_print.py

target_path="$($lz_path_/.venv/bin/python $lz_path_/src/lazyls_parse.py | grep '::LZOUT::' | cut -f 2)"

if [ -d "$target_path" ]; then
  cd "$target_path"
else
  echo "$target_path"
fi
