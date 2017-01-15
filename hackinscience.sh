#!/bin/bash

echo -e "\033[0;32mDeploying Hackinscience update to GitHub...\033[0m"

git add -A

# Commit changes with provided argument or with date as message
msg="Update Hackinscience `date +%Y-%m-%d\ %H:%M:%S`"
if [ $# -eq 1 ]
  then msg="$1"
fi
git commit -m "$msg"

git push -u origin master
