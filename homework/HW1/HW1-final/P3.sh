grep '[0-9]' apollo13.txt | wc -l
grep --help | grep "\-c, \-\-count"
ls | grep '\.py$' | wc -l
find . -type f -exec ls -l {} \; | grep -E '^\-.{6}\-\-.' | wc -l
ls -l | grep -E '^[-d].{6}\-\-.' | wc -l
