#!/bin/bash
echo "Please wait, we will finish update soon!"
date
git pull
echo "Processing..."
git add -A
git commit -m "Update"
git push --progress -u origin master
date
echo "Done! 🎶"