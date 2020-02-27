#!/usr/bin/python3
#Author: Resul Ucar
import PyPDF2
import sys
import optparse
import itertools
import string
 
charset = string.ascii_letters + string.digits + string.punctuation
parser = optparse.OptionParser()
parser.add_option('-f','--file',dest='file',help='encrypted file')
(options, args) = parser.parse_args()
if options.file == None:
    print('./pdfCracker.py -f [file]')
    sys.exit()

file = options.file
pdf = PyPDF2.PdfFileReader(open(file,'rb'))

if not pdf.isEncrypted:
    print('No password')

else:
	for pwd in itertools.product(charset, repeat=4):
		test = ''.join(pwd)
		if pdf.decrypt(test):
			print("[+] Password Found! [%s]" % (test))
			sys.exit()
			break