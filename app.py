# Developer: Farhan Ellahi
# Date: Tuesday, May 25, 2021
# Email: support@thenanosoft.com
# Title: Pdf to Images

from pdf2image import convert_from_path
import os
import sys
import datetime

outputdir = 'images/'

def convert(file, outputdir):
    currentdatetime = datetime.datetime.now()
    outputdir = outputdir + os.path.splitext(file)[0] + ' ' + str(currentdatetime.strftime('%d-%m-%y %H')) + '/'
    if not os.path.exists(outputdir):
        os.makedirs(outputdir)

    pages = convert_from_path(file, 500)

    counter = 1
    
    for page in pages:
        myFile = outputdir + 'page' + str(counter) + '.jpg'
        counter = counter + 1
        page.save(myFile, 'JPEG')
        print(myFile)

args = sys.argv
if len(args) > 1:
    file = args[1]
    convert(file, outputdir)