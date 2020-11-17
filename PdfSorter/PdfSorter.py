#source: https://bskinn.github.io/Scan-PDF-Merging/

import itertools as itt
import sys
import PySimpleGUI as sg
import PyPDF2 as PDF


def GetFilesToMerge():
    #open a window and select two files to merge idealy the odd page document has the extention _odd.pdf
    print("Start GetFilesToMerge")
    FilesToMerge = [[sg.Text('Select documents to merge ')],
                    [sg.Text('Document containing the odd pages') , sg.InputText(key = 'odd_pages'), sg.FileBrowse()],
                    [sg.Text('Document containing the even pages'), sg.InputText(key = 'even_pages'), sg.FileBrowse()],
                    [sg.Submit(), sg.Cancel()]
                    ]
    window = sg.Window('File merger', FilesToMerge)
    event, values = window.read()
    window.close()
    return event, values


def main():
    #fbase = sys.argv[1]
    #fbase = '/Users/k.chan/Pictures/Kadenza - 20140213 - ASR pensioen Startbrief pensioenregeling'
    button, values= GetFilesToMerge()
    fbase_odd, fbase_even = values['odd_pages'], values['even_pages']
    pdf_out = PDF.PdfFileWriter()

    with open(fbase_odd, 'rb') as f_odd:
        with open(fbase_even, 'rb')  as f_even:
            pdf_odd = PDF.PdfFileReader(f_odd)
            pdf_even = PDF.PdfFileReader(f_even)

            for p in itt.chain.from_iterable(
                itt.zip_longest(
                    pdf_odd.pages,
                    reversed(pdf_even.pages),
                )
            ):
                if p:
                    pdf_out.addPage(p)

            with open(fbase_odd.replace('_odd.pdf','_merged.pdf'), 'wb') as f_out:
                pdf_out.write(f_out)

    return 0


main()
