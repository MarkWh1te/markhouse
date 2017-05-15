#!/usr/bin/env bash
make html
cd ../markwh1te.github.io && git stash && git pull && rm -rf *&& cd ../markhouse
cp -r output/* ../markwh1te.github.io
cd ../markwh1te.github.io && git add .&& git commit -m 'update' && git push origin master
