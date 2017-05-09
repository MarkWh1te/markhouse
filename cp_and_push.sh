#!/usr/bin/env bash
cp -r output/* ../markwh1te.github.io
cd ../markwh1te.github.io && git add .&& git commit -m 'update' && git push origin master
