#Week 7 Challenge Problem A & B

import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import simpledialog

class WordFileWriteReadGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title('Word File Analyser')

        self.top_frame = tkinter.Frame()
        self.bottom_frame = tkinter.Frame()
        
        self.label1 = tkinter.Label(self.top_frame, text='How many words do you wish to write?')
        self.entry1 = tkinter.Entry(self.top_frame, width = 10)
        self.label1.pack()
        self.entry1.pack()
        
        self.label2 = tkinter.Label(self.top_frame, text='Which file do you wish to write in?')
        self.entry2 = tkinter.Entry(self.top_frame, width=12)
        self.label2.pack()
        self.entry2.pack()
        
        self.write_button = tkinter.Button(self.bottom_frame, text ='Write Words to File', command=self.writeToFile)
        self.read_button = tkinter.Button(self.bottom_frame, text ='Analyse File', command=self.readFile)
        self.quit_button = tkinter.Button(self.bottom_frame, text='Quit', bg = 'red', command=self.main_window.destroy)
        self.write_button.pack()
        self.read_button.pack()
        self.quit_button.pack()
 
        self.top_frame.pack()
        self.bottom_frame.pack()
        tkinter.mainloop()

    def writeToFile(self):
        try:
            num_words = int(self.entry1.get())
            if num_words <= 0:
                tkinter.messagebox.showerror("Error", "Positive number required.")
                return
            
            filename = self.entry2.get()
            
            word_file = open(filename, 'w')
            
            for i in range(num_words):
                word = tkinter.simpledialog.askstring("Write", f"Enter word #{i + 1}:")
                word_file.write(word + '\n')
            
            tkinter.messagebox.showinfo("Success", f"{num_words} words have been written to '{filename}")
            # self.words = self.readWords(filename)

            word_file.close()
            messagebox.showinfo("Info", "Please click on the Analyse File button to read your file.")
        
        except ValueError:
            tkinter.messagebox.showerror("Error", "Please enter a number.")
        except IOError:
            tkinter.messagebox.showerror("Error", "Could not write to the file.")

    def readFile(self):
        disp_string = ""
        try:
            filename = self.entry2.get()
            word_file = open(filename,'r')
            count = 0
            disp_string = "Here are the file stats:"
            list1 = []
            total_length = 0
            for line in word_file:
                count += 1
                list1.append(line)
                total_length += len(line)

            disp_string = "Total words: "+str(count)+"\nLongest word in file: " + max(list1, key=len)+"Average word length: "+str((total_length/count)-1)+""





            word_file.close()
            messagebox.showinfo("File Statistics", disp_string)

        except IOError:
            messagebox.showinfo("Error", "Could not open file")

mygui = WordFileWriteReadGUI()