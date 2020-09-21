import os
from PyPDF2 import PdfFileMerger
import tkinter as tk
from tkinter import filedialog

# Initialize Tkinter and dialogs
root = tk.Tk()
root.withdraw()
filepath = filedialog.askdirectory()

# Initialize Merger
merger = PdfFileMerger()

# Default File Extension
files = [('PDF Files', '*.pdf')]
# Get current user logged in
current_user = os.getlogin()
# Change directory to where files are located
os.chdir(filepath)


# Merger function
def merge():
    for item in os.listdir(filepath):
        if item.endswith('pdf'):
            merger.append(item)


# Save File Function
def save():
    savepath = filedialog.asksaveasfile(filetypes=files, defaultextension=files, mode='wb')
    merger.write(savepath)
    merger.close()


if __name__ == "__main__":
    merge()
    save()