#!/bin/sh
# notes_size_check.sh NOTES.md [max_bytes]  — run at the end of every session.
# On 21 Nov my notes reached 57 KB and about 20 sessions in a row died before writing any output.
f=${1:-NOTES.md}; max=${2:-10240}
size=$(wc -c < "$f")
if [ "$size" -gt "$max" ]; then
  echo "TOO BIG: $f is $size bytes (max $max). Move old log entries to archive/ before you stop."; exit 1
fi
echo "OK: $f is $size bytes"
