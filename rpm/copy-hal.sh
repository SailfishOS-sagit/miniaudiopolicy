#!/bin/sh

set -e

OUT_DEVICE=${HABUILD_DEVICE:-$DEVICE}

if [ ! -f ./out/target/product/${OUT_DEVICE}/system/bin/miniaudiopolicyservice ]; then
    echo "Please build Fingerprint support as per HADK instructions"
    exit 1
fi

fold=$(dirname "$0")/../out
rm -rf $fold
mkdir $fold
mv ./out/target/product/${OUT_DEVICE}/system/bin/miniaudiopolicyservice $fold

ls -lh $fold

