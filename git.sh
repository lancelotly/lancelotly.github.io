#!/bin/bash
echo "Please wait, we will finish update soon!"
date
git pull
echo "Processing..."
make html
echo "Processing..."
make clean
echo "Processing..."
git add -A
git commit -m "lancelotly"
git push --progress -u origin master
date
echo "Done! 🎶"