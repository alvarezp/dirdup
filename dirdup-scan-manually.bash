#!/bin/sh

TARGET="."

if [ ! -z "$1" ]; then
	TARGET="$1"
fi

superstat() {
	stat --printf "%11s %11Y " "$1"; md5sum "$1"
}

find "$TARGET" -type f | while read FILE; do
	superstat "$FILE"
done
