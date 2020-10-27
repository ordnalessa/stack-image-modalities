import os
from sys import exit

import tkinter as tk
from tkinter import filedialog, ttk

from merge_pictures import MergePictures

LARGEFONT = ("Verdana", 12)


# faf_path = ""
# nir_path = ""
# cfp_path = ""
# OUT_PATH = ""


class StackImagesApp:
    def Page0(self, root):
        self.root = root
        self.root.title("Merge Image Modalities")
        # self.screenwidth = self.root.winfo_screenwidth()
        # self.screenheight = self.root.winfo_screenheight()
        # self.root.geometry('{}x{}'.format(self.screenwidth // 2, self.screenheight // 2))

        self.root.columnconfigure(2, weight=1)

        self.faf_path = tk.StringVar()
        self.nir_path = tk.StringVar()
        self.cfp_path = tk.StringVar()
        self.out_path = tk.StringVar()

        nir_lbl0 = tk.Label(self.root, text="Enter NIR directory.", )
        nir_lbl0.grid(column=2, row=1, pady=(15, 1), sticky=tk.E + tk.W + tk.N + tk.S)
        nir_lbl1 = tk.Label(self.root, fg="red", )
        nir_lbl1.grid(column=2, row=3, sticky=tk.E + tk.W + tk.N + tk.S)
        self.nir_txt = tk.Entry(self.root, )
        self.nir_txt.grid(column=2, row=2, padx=5, sticky=tk.E + tk.W + tk.N + tk.S)
        nir_btn0 = tk.Button(
            self.root, text="File Explorer", command=loadfile(self.nir_txt),
        )
        nir_btn0.grid(column=3, row=2, padx=(1, 15), sticky=tk.E + tk.W + tk.N + tk.S)
        nir_btn1 = tk.Button(
            self.root,
            text="Check",
            command=check_dir(nir_lbl1, self.nir_txt),
        )
        nir_btn1.grid(column=1, row=2, padx=15, sticky=tk.E + tk.W + tk.N + tk.S)

        faf_lbl0 = tk.Label(self.root, text="Enter FAF directory.", )
        faf_lbl0.grid(column=2, row=4, pady=(15, 1), sticky=tk.E + tk.W + tk.N + tk.S)
        faf_lbl1 = tk.Label(self.root, fg="red", )
        faf_lbl1.grid(column=2, row=6, sticky=tk.E + tk.W + tk.N + tk.S)
        self.faf_txt = tk.Entry(self.root, )
        self.faf_txt.grid(column=2, row=5, padx=5, sticky=tk.E + tk.W + tk.N + tk.S)
        faf_btn0 = tk.Button(
            self.root, text="File Explorer", command=loadfile(self.faf_txt),
        )
        faf_btn0.grid(column=3, row=5, padx=(1, 15), sticky=tk.E + tk.W + tk.N + tk.S)
        faf_btn1 = tk.Button(
            self.root,
            text="Check",
            command=check_dir(faf_lbl1, self.faf_txt),

        )
        faf_btn1.grid(column=1, row=5, padx=15, sticky=tk.E + tk.W + tk.N + tk.S)

        cfp_lbl0 = tk.Label(self.root, text="Enter CFP directory.", )
        cfp_lbl0.grid(column=2, row=7, pady=(15, 1), sticky=tk.E + tk.W + tk.N + tk.S)
        cfp_lbl1 = tk.Label(self.root, fg="red", )
        cfp_lbl1.grid(column=2, row=9, sticky=tk.E + tk.W + tk.N + tk.S)
        self.cfp_txt = tk.Entry(self.root, )
        self.cfp_txt.grid(column=2, row=8, padx=5, sticky=tk.E + tk.W + tk.N + tk.S)
        cfp_btn0 = tk.Button(
            self.root, text="File Explorer", command=loadfile(self.cfp_txt),
        )
        cfp_btn0.grid(column=3, row=8, padx=(1, 15), sticky=tk.E + tk.W + tk.N + tk.S)
        cfp_btn1 = tk.Button(
            self.root,
            text="Check",
            command=check_dir(cfp_lbl1, self.cfp_txt),
        
        )
        cfp_btn1.grid(column=1, row=8, padx=15, sticky=tk.E + tk.W + tk.N + tk.S)

        out_lbl0 = tk.Label(self.root, text="Enter output directory.", )
        out_lbl0.grid(column=2, row=10, pady=(15, 1), sticky=tk.E + tk.W + tk.N + tk.S)
        out_lbl1 = tk.Label(self.root, fg="red", )
        out_lbl1.grid(column=2, row=12, sticky=tk.E + tk.W + tk.N + tk.S)
        self.out_txt = tk.Entry(self.root, )
        self.out_txt.grid(column=2, row=11, padx=5, sticky=tk.E + tk.W + tk.N + tk.S)
        out_btn0 = tk.Button(
            self.root, text="File Explorer", command=loadfile(self.out_txt),
        )
        out_btn0.grid(column=3, row=11, padx=(1, 15), sticky=tk.E + tk.W + tk.N + tk.S)
        out_btn1 = tk.Button(
            self.root, text="Create", command=makedir(out_lbl1, self.out_txt),
        )
        out_btn1.grid(column=1, row=11, padx=15, sticky=tk.E + tk.W + tk.N + tk.S)

        exit_btn = tk.Button(self.root, text="Exit", command=exit, )
        exit_btn.grid(column=13, row=13, pady=(5, 15), padx=(1, 15), sticky=tk.E + tk.W + tk.N + tk.S)

        next_btn = tk.Button(self.root, text="Next", command=self.Page1, )
        next_btn.grid(column=12, row=13, pady=(5, 15), padx=(1, 1), sticky=tk.E + tk.W + tk.N + tk.S)

    def Page1(self):
        page1 = tk.Toplevel(self.root)
        page1.title("File lists")

        nir_lbl = tk.Label(page1, text="NIR files:", )
        nir_lbl.grid(column=1, row=1, pady=(15, 1))
        self.nir_listbox = tk.Listbox(page1, )
        self.nir_listbox.grid(column=1, row=2, pady=5, padx=(15, 1), sticky=tk.E + tk.W + tk.N + tk.S)

        faf_lbl = tk.Label(page1, text="FAF files:", )
        faf_lbl.grid(column=2, row=1, pady=(15, 1))
        self.faf_listbox = tk.Listbox(page1, )
        self.faf_listbox.grid(column=2, row=2, pady=5, padx=(1, 1), sticky=tk.E + tk.W + tk.N + tk.S)

        cfp_lbl = tk.Label(page1, text="CFP files:", )
        cfp_lbl.grid(column=3, row=1, pady=(15, 1))
        self.cfp_listbox = tk.Listbox(page1, )
        self.cfp_listbox.grid(column=3, row=2, pady=5, padx=(1, 15), sticky=tk.E + tk.W + tk.N + tk.S)

        self.refresh_lists()

        prev_btn = tk.Button(
            page1, text="Previous", command=page1.destroy,
        )
        prev_btn.grid(column=11, row=13, pady=(5, 15), padx=(1, 1), sticky=tk.E + tk.W + tk.N + tk.S)

        refr_btn = tk.Button(
            page1, text="Refresh", command=self.refresh_lists,
        )
        refr_btn.grid(column=10, row=13, pady=(5, 15), padx=(1, 1), sticky=tk.E + tk.W + tk.N + tk.S)

        next_btn = tk.Button(page1, text="Confirm", command=self.Page2, )
        next_btn.grid(column=12, row=13, pady=(5, 15), padx=(1, 1), sticky=tk.E + tk.W + tk.N + tk.S)

    def Page2(self):

        self.merge_pictures = MergePictures(
            self.nir_txt.get(),
            self.faf_txt.get(),
            self.cfp_txt.get(),
            self.out_txt.get(),
        )

        page2 = tk.Toplevel(self.root)
        page2.title("Processing images...")

        progress_var = tk.IntVar()
        progress_var.set(0)

        progressbar = ttk.Progressbar(
            page2,
            variable=progress_var,
            length=300,
            mode="determinate",
            style="black.Horizontal.TProgressbar",
        )
        progressbar["maximum"] = 100
        progressbar.grid(column=1, row=3, padx=15, pady=15, sticky=tk.E + tk.W + tk.N + tk.S)

        lbl0 = tk.Label(page2, text="Processing files for image ID:", )
        lbl0.grid(column=1, row=1, pady=(15, 1), sticky=tk.E + tk.W + tk.N + tk.S)
        lbl1 = tk.Label(page2, )
        lbl1.grid(column=1, row=2, pady=(1, 1), sticky=tk.E + tk.W + tk.N + tk.S)

        stackable = matchfiles(
            self.nir_txt.get(), self.faf_txt.get(), self.cfp_txt.get()
        )

        num_imgs = len(stackable)
        prog_mul = 100.0 / num_imgs
        for i, pid in enumerate(stackable):
            page2.update_idletasks()
            lbl1.configure(text=pid)
            progress_var.set((i + 1) * prog_mul)

            self.merge_pictures(pid)

        progressbar.destroy()
        lbl0.configure(text="Process finished.")
        lbl1.configure(text="Select 'Finish' to exit the program.")

        finish_btn = tk.Button(page2, text="Finish", command=exit, )
        finish_btn.grid(column=1, row=3, pady=(15, 15), padx=(15, 15), sticky=tk.E + tk.W + tk.N + tk.S)

    def refresh_lists(self):
        nir_path = self.nir_txt.get()
        faf_path = self.faf_txt.get()
        cfp_path = self.cfp_txt.get()
        if os.path.isdir(nir_path):
            nir_filelist = os.listdir(nir_path)
            self.nir_listbox.delete(0, tk.END)
            if not nir_filelist:
                self.nir_listbox.insert(tk.END, "Directory is empty.")
            else:
                for f in nir_filelist:
                    self.nir_listbox.insert(tk.END, f)
        else:
            self.nir_listbox.insert(tk.END, "Directory does not exist.")

        if os.path.isdir(faf_path):
            faf_filelist = os.listdir(faf_path)
            self.faf_listbox.delete(0, tk.END)
            if not faf_filelist:
                self.faf_listbox.insert(tk.END, "Directory is empty.")
            else:
                for f in faf_filelist:
                    self.faf_listbox.insert(tk.END, f)
        else:
            self.faf_listbox.insert(tk.END, "Directory does not exist.")

        if os.path.isdir(cfp_path):
            cfp_filelist = os.listdir(cfp_path)
            self.cfp_listbox.delete(0, tk.END)
            if not cfp_filelist:
                self.cfp_listbox.insert(tk.END, "Directory is empty.")
            else:
                for f in cfp_filelist:
                    self.cfp_listbox.insert(tk.END, f)
        else:
            self.cfp_listbox.insert(tk.END, "Directory does not exist.")


def makedir(lbl, txt):
    def _clicked():
        path = txt.get()
        if os.path.isdir(path):
            lbl.configure(text=f"'{path}' alredy exists.", fg="black")
        else:
            try:
                os.mkdir(path)
                lbl.configure(
                    text=f"A new directory in '{os.path.abspath(path)}' was created.",
                    fg="black",
                )
            except:
                lbl.configure(text=f"'{path}' is not a valid path.")

    return _clicked


def check_dir(lbl, txt):
    def _clicked():
        path = txt.get()
        if not os.path.isdir(path):
            lbl.configure(text=f"'{path}' is not a valid path.")
        else:
            lbl.configure(text="")

    return _clicked


def loadfile(txt):
    def _clicked():
        filename = tk.filedialog.askdirectory()
        txt.delete(0, tk.END)  # removes current text
        txt.insert(0, filename)  # insert the filename

    return _clicked


def matchfiles(nir_path, faf_path, cfp_path):
    nir_files = os.listdir(nir_path)
    faf_files = os.listdir(faf_path)
    cfp_files = os.listdir(cfp_path)

    nir_files = set([x.split(".")[0] for x in nir_files])
    faf_files = set([x.split(".")[0] for x in faf_files])
    cfp_files = set([x.split(".")[0] for x in cfp_files])

    intersection = nir_files.intersection(faf_files.intersection(cfp_files))

    return list(intersection)


def main():
    root = tk.Tk()
    app = StackImagesApp()
    app.Page0(root)
    root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = StackImagesApp()
    app.Page0(root)
    root.mainloop()
