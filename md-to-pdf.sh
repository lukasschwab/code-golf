#!/usr/bin/env bash
# ARG WRANGLING
if [[ $# -eq 0 ]] ; then
    echo 'Usage: `topdf somefile.md`'
    exit 0
fi
INFILE=$1
NAME=${1%.md}
PDFNAME=${NAME}.pdf
# PROCESSING
sed -e 's/––/---/g' ${INFILE} | # Add any other operations after this...
pandoc --from=markdown --latex-engine=xelatex -o ${PDFNAME} # ...and before this.
# CONVENIENCE
echo "Done: created" $PDFNAME
open $PDFNAME
