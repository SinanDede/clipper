import tkinter as tk
import tkinter.ttk as ttk


class Main_Widget(ttk.Frame):
    def __init__(self, master=None, **kw):
        ttk.Frame.__init__(self, master, **kw)

        #menu
        self.menu_label_frame = ttk.Labelframe(self)

        #buttons
        #file1
        self.file1_button = ttk.Button(self.menu_label_frame)
        self.file1_button.configure(text='File1')
        self.file1_button.pack(pady='5', side='top')
        self.file1_button.configure(command=self.openfile1)
        #file2
        self.file2_button = ttk.Button(self.menu_label_frame)
        self.file2_button.configure(text='File2')
        self.file2_button.pack(pady='5', side='top')
        self.file2_button.configure(command=self.openfile2)
        #split
        self.split_button = ttk.Button(self.menu_label_frame)
        self.split_button.configure(text='Split')
        self.split_button.pack(pady='5', side='top')
        self.split_button.configure(command=self.splitfile)
        #merge
        self.merge_button = ttk.Button(self.menu_label_frame)
        self.merge_button.configure(text='Merge')
        self.merge_button.pack(pady='5', side='top')
        self.merge_button.configure(command=self.mergefile, state='disabled')
        #save
        self.clear_button = ttk.Button(self.menu_label_frame)
        self.clear_button.configure(text='Clear')
        self.clear_button.pack(pady='5', side='top')
        self.clear_button.configure(command=self.clear)

        #menu config
        self.menu_label_frame.configure(text='Menu')
        self.menu_label_frame.place(anchor='nw', height='390', width='100', x='10', y='0')

        #preview label
        self.preview_label_frame = ttk.Labelframe(self)

        #file paths
        self.file1_label = ttk.Label(self.preview_label_frame)
        self.file1_label.configure(background='#ffffff', relief='groove')
        self.file1_label.place(anchor='nw', height='25', width='450', x='10', y='5')
        self.file2_label = ttk.Label(self.preview_label_frame)
        self.file2_label.configure(background='#ffffff', relief='groove')
        self.file2_label.place(anchor='nw', height='25', width='450', x='10', y='40')

        #page numbers
        self.file1_pagenum_frame = ttk.Labelframe(self.preview_label_frame)
        self.file1_page_num_entry = ttk.Entry(self.file1_pagenum_frame)
        self.file1_page_num_entry.place(anchor='nw', width='190', x='2', y='-1')
        self.file1_pagenum_frame.configure(height='200', text='File1 page numbers example 1,2,3', width='200')
        self.file1_pagenum_frame.place(anchor='nw', height='40', x='10', y='69')
        self.file2_pagenum_frame = ttk.Labelframe(self.preview_label_frame)
        self.file2_page_num_entry = ttk.Entry(self.file2_pagenum_frame)
        self.file2_page_num_entry.configure(state='disabled')
        self.file2_page_num_entry.place(anchor='nw', width='190', x='2', y='-1')
        self.file2_pagenum_frame.configure(height='200', text='File2 page numbers example 1,2,3', width='200')
        self.file2_pagenum_frame.place(anchor='nw', height='40', x='260', y='69')

        #file info
        self.file1_info_frame = ttk.Labelframe(self.preview_label_frame)
        self.file1_info_text = tk.Text(self.file1_info_frame)
        self.file1_info_text.configure(height='10', state='disabled', width='50')
        self.file1_info_text.place(anchor='nw', height='200', width='190', x='2', y='0')
        self.file1_info_frame.configure(height='200', text='File1 info', width='200')
        self.file1_info_frame.place(anchor='nw', height='225', x='10', y='140')
        self.file2_info_frame = ttk.Labelframe(self.preview_label_frame)
        self.file2_info_text = tk.Text(self.file2_info_frame)
        self.file2_info_text.configure(height='10', state='disabled', width='50')
        self.file2_info_text.place(anchor='nw', height='200', width='190', x='2', y='0')
        self.file2_info_frame.configure(height='200', text='File2 info', width='200')
        self.file2_info_frame.place(anchor='nw', height='225', x='260', y='140')

        #preview label config
        self.preview_label_frame.configure(text='Preview')
        self.preview_label_frame.place(height='390', width='480', x='110', y='0')

    def openfile1(self):
        pass

    def openfile2(self):
        pass

    def splitfile(self):
        pass

    def mergefile(self):
        pass

    def clear(self):
        pass
