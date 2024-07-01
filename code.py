import tkinter as tk
from tkinter import filedialog, messagebox
from convert import convert_to_bae, convert_to_py
from run import execute_bae_code

class BaeLangEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("BaeLang Editor")

        self.text_area = tk.Text(self.root)
        self.text_area.pack(expand=1, fill='both')

        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Open", command=self.open_bae_file)
        file_menu.add_command(label="Save As .bae", command=self.save_as_bae)
        self.menu_bar.add_cascade(label="Run", command=self.run_bae_code)
        file_menu.add_command(label="Exit", command=root.quit)

    def open_bae_file(self):
        file_path = filedialog.askopenfilename(defaultextension=".bae", filetypes=[("BaeLang files", "*.bae")])
        if file_path:
            with open(file_path, "r") as bae_file:
                bae_code = bae_file.read()
                py_code = convert_to_py(bae_code)
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert(tk.END, py_code)

    def save_as_bae(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".bae", filetypes=[("BaeLang files", "*.bae")])
        if file_path:
            py_code = self.text_area.get("1.0", tk.END)
            bae_code = convert_to_bae(py_code)
            with open(file_path, "w") as bae_file:
                bae_file.write(bae_code)

    def run_bae_code(self):
        py_code = self.text_area.get("1.0", tk.END)
        bae_code = convert_to_bae(py_code)
        try:
            execute_bae_code(bae_code)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred while executing the code:\n{e}")

if __name__ == "__main__":
    root = tk.Tk()
    editor = BaeLangEditor(root)
    root.mainloop()
