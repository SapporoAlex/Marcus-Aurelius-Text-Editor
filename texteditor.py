import tkinter
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename
import random as rd


marcus_aurelius_quotes = ["Very little is needed to make a happy life; it is all within yourself, in your way of "
                          "thinking.",
                          "The best revenge is to be unlike him who performed the injustice.",
                          "Waste no more time arguing about what a good man should be. Be one.",
                          "The happiness of your life depends upon the quality of your thoughts.",
                          "It is not death that a man should fear, but he should fear never beginning to live.",
                          "He who fears death either fears the loss of sensation or a different kind of sensation. But "
                          "if thou shalt have no sensation, neither will thou feel any harm; and if thou shalt acquire "
                          "another kind of sensation, thou wilt be a different kind of living being and thou wilt not "
                          "cease to live."]


def open_file(window, text_edit):
    filepath = askopenfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    text_edit.delete(1.0, tk.END)
    with open(filepath, "r") as f:
        content = f.read()
        text_edit.insert(tk.END, content)
    window.title(f"Open File: {filepath}")


def save_file(window, text_edit):
    filepath = asksaveasfilename(filetypes=[("Text Files", "*.txt")])

    if not filepath:
        return

    with open(filepath, "w") as f:
        content = text_edit.get(1.0, tk.END)
        f.write(content)
    window.title(f"Open File: {filepath}")


def insert_prewritten_text(text_edit):
    prewritten_text = marcus_aurelius_quotes[rd.randint(0, 6)]
    text_edit.insert(tk.END, prewritten_text)


def main():
    window = tk.Tk()
    window.title("Alex's Text Editor")
    window.rowconfigure(0, minsize=400)
    window.columnconfigure(1, minsize=500)

    text_edit = tk.Text(window, font=("Century", 20), bg="beige", fg="brown", wrap=tk.WORD)
    text_edit.grid(row=0, column=1)

    frame = tk.Frame(window, relief=tk.RAISED, bd=2)
    save_button = tk.Button(
        frame, text="Save", command=lambda: save_file(window, text_edit))
    open_button = tk.Button(
        frame, text="Open", command=lambda: open_file(window, text_edit))
    insert_button = tk.Button(frame, text="Aurelius", command=lambda: insert_prewritten_text(text_edit))

    save_button.grid(row=0, column=0, padx=5, pady=5, sticky="ew")
    open_button.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
    insert_button.grid(row=2, column=0, padx=5, pady=5, sticky="ew")
    frame.grid(row=0, column=0, sticky="ns")
    frame.grid(row=0, column=0, sticky="ns")
    scrollb = tkinter.Scrollbar(window, command=text_edit.yview)
    scrollb.grid(row=0, column=1, sticky='nse')
    text_edit['yscrollcommand'] = scrollb.set
    window.bind("<Control-s>", lambda x: save_file(window, text_edit))
    window.bind("<Control-o>", lambda x: open_file(window, text_edit))
    window.mainloop()


main()
