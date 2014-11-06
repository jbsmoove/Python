# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 15:20:39 2014

@author: jbrummitt0
"""

import PyPDF2 as pdf
#import io
import os

rootdir = 'C:/Users/Jbrummitt0/Desktop/WP File'
output = pdf.PdfFileWriter()
outpath = 'C:/Users/Jbrummitt0/Desktop/WP File/WP.pdf'
merger = pdf.PdfFileMerger()
pcnt = 0
n = 0
p = ''
flist = []
flistordr = []
ordr = {'W-2': 1,
       '1099-INT': 2,
       '1099-DIV' : 3,
       'Consolidated 1099' : 4,
       '1099-G' : 5,
       'IRA' : 6,
       'K-1s' : 7,
       'Sch C Support' : 8,
       '1098-INT' : 9,
       'Sch H' : 10,
       'State Info' : 11,
       'Other' : 12
       }

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file.endswith('.pdf') and file != 'WP.pdf':
            flist.append((ordr.get(subdir[len(rootdir)+1:]),
                          os.path.join(subdir, file), file))

#            flistordr.append(ordr.get(subdir[len(rootdir)+1:]))
print(flist)
flist.sort()
output = open(rootdir + r"\WP.pdf", "wb")

for item in flist:
#    print (item[0:1])
    n = n + 1
    if item[0:1] != "":
        x, y, z = item[:]
        print(y)
        input1 = pdf.PdfFileReader(y, "rb")
        if y != p:
            input1.getPage(0).createBlankPage(input1)
            pcnt += 1
        merger.merge(pcnt, input1, z)
        pcnt = pcnt + input1.getNumPages()
        p = y        

merger.write(output)
output.close()

#        merger.addBookmark(z, pcnt)


