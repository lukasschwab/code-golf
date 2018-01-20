#!/usr/bin/env bash
# ARG WRANGLING
if [[ $# -lt 3 ]] ; then
    echo 'Usage: `topdf input_pdf.pdf input_code.pdf output_filename.pdf`'
    exit 0
fi
INPDF=$1
INCODE=$2
OUTFILE=$3
# CONCATENATE
# Generate PDF of the python code
echo "Converting ${INCODE} to PDF..."
enscript --color=1 --highlight=python -q -Z -p - -f Courier10 __main__.py | ps2pdf - __CONCAT__.pdf
# Concatenate PDFs
echo "Appending code to ${INPDF}..."
gs -q -dNOPAUSE -dBATCH -sDEVICE=pdfwrite -sOutputFile=${OUTFILE} ${INPDF} __CONCAT__.pdf
# Cleanup
rm __CONCAT__.pdf
echo "Done: created" $OUTFILE
open ${OUTFILE}