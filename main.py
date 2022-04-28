import os
import tkinter as tk
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename, asksaveasfile
from pathlib import Path
from PyPDF4 import PdfFileReader, PdfFileWriter
from main_widget import Main_Widget

class Clipper(Main_Widget):
    def __init__(self, *args, **kwargs):
        Main_Widget.__init__(self, *args, **kwargs)

    def openfile1(self):
        self.file1_info_text.delete('1.0', 'end')
        self.file = askopenfilename(filetypes=[('PDF files', '*.pdf')])
        if not (self.file and Path(self.file).exists()):
            return
        self.pdf = PdfFileReader(self.file, strict=False)
        if self.pdf.isEncrypted:
            self.pdf.decrypt('')
        self.pdf.getDocumentInfo()
        self.filepages = self.pdf.getNumPages()
        self.filename = self.file.split('/')
        self.file1_label.configure(text=Path(self.file))
        self.file1_info_text.configure(state='normal')
        self.file1_info_text.insert('end', f"Name: {self.filename[-1]}\n"
                                           f"Total pages: {self.filepages}\n"
                                           f"Size: {os.path.getsize(Path(self.file))} bytes\n")

    def openfile2(self):
        self.file2_info_text.delete('1.0', 'end')
        self.file2_page_num_entry.configure(state='normal')
        self.file2 = askopenfilename(filetypes=[('PDF files', '*.pdf')])
        if not (self.file2 and Path(self.file2).exists()):
            self.file2_page_num_entry.configure(state='disabled')
            return
        self.pdf2 = PdfFileReader(self.file2, strict=False)
        if self.pdf2.isEncrypted:
            self.pdf2.decrypt('')
        self.pdf2.getDocumentInfo()
        self.filepages2 = self.pdf2.getNumPages()
        self.filename2 = self.file2.split('/')
        self.file2_label.configure(text=Path(self.file2))
        self.file2_info_text.configure(state='normal')
        self.file2_info_text.insert('end', f"Name: {self.filename2[-1]}\n"
                                           f"Total pages: {self.filepages2}\n"
                                           f"Size: {os.path.getsize(Path(self.file2))} bytes\n")

        self.merge_button.configure(state='normal')

    def splitfile(self):
        try:
            self.pdf = PdfFileReader(self.file, strict=False)
            if self.pdf.isEncrypted:
                self.pdf.decrypt('')
            self.pdf.getDocumentInfo()
            self.pages = [None if x.strip() == 'None' else x for x in self.file1_page_num_entry.get().split(',')]
            for i in range(0, len(self.pages)):
                self.pages[i] = int(self.pages[i])

            self.page_nums = [i - 1 for i in self.pages]

            self.pdf_writer = PdfFileWriter()

            for page in self.page_nums:
                self.pdf_writer.addPage(self.pdf.getPage(page))

            self.output_file = asksaveasfile(defaultextension='.pdf', filetypes=(('pdf files', '*.pdf'),('All Files', '*.*')))
            with open(self.output_file.name, 'wb') as f:
                self.pdf_writer.write(f)
            self.file1_page_num_entry.delete(0, 'end')
            self.file1_info_text.insert('end', "Successfully splitted\n")

        except:
            self.file1_info_text.configure(state='normal')
            self.file1_info_text.insert('end', "Please check your page numbers\n")


    def mergefile(self):
        try:
            self.pdf = PdfFileReader(self.file, strict=False)
            if self.pdf.isEncrypted:
                self.pdf.decrypt('')
            self.pdf.getDocumentInfo()

            self.pdf2 = PdfFileReader(self.file2, strict=False)
            if self.pdf2.isEncrypted:
                self.pdf2.decrypt('')
            self.pdf2.getDocumentInfo()

            self.pages = [None if x.strip() == 'None' else x for x in self.file1_page_num_entry.get().split(',')]
            for i in range(0, len(self.pages)):
                self.pages[i] = int(self.pages[i])

            self.page_nums = [i - 1 for i in self.pages]

            self.pages2 = [None if x.strip() == 'None' else x for x in self.file2_page_num_entry.get().split(',')]
            for i in range(0, len(self.pages2)):
                self.pages2[i] = int(self.pages2[i])

            self.page_nums2 = [i - 1 for i in self.pages2]

            self.pdf_writer2 = PdfFileWriter()

            for page in self.page_nums:
                self.pdf_writer2.addPage(self.pdf.getPage(page))
            for page2 in self.page_nums2:
                self.pdf_writer2.addPage(self.pdf2.getPage(page2))

            self.output_file2 = asksaveasfile(defaultextension='.pdf', filetypes=(('pdf files', '*.pdf'),('All Files', '*.*')))
            with open(self.output_file2.name, 'wb') as f:
                self.pdf_writer2.write(f)

            self.file1_page_num_entry.delete(0, 'end')
            self.file2_page_num_entry.delete(0, 'end')
            self.file2_info_text.insert('end', "Successfully merged\n")


        except:
            self.file2_info_text.configure(state='normal')
            self.file2_info_text.insert('end', "Please check your page numbers\n")

    def clear(self):
        self.file1_label.configure(text="")
        self.file2_label.configure(text="")
        self.file1_page_num_entry.delete(0, 'end')
        self.file2_page_num_entry.delete(0, 'end')
        self.file1_info_text.delete('1.0', 'end')
        self.file2_info_text.delete('1.0', 'end')
        self.file2_page_num_entry.configure(state='disabled')
