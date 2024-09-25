import tkinter as tk
import random
import pyperclip
def generate_password():
    nletters = int(letter_entry.get())
    nnumbers = int(number_entry.get())
    nsymbols = int(symbol_entry.get())
    exclude_chars = exclude_entry.get()

    letters = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
    numbers = "1 2 3 4 5 6 7 8 9 0".split()
    symbols = """! @ # $ % ^ & * ( ) ~ < > , . ? _ - + = " : ;""".split()

    all_chars = list(set(letters + numbers + symbols) - set(exclude_chars))

    if len(all_chars) == 0:
        password_var.set("No valid characters left after exclusion.")
        return

    lgen = [random.choice(letters) for _ in range(nletters)]
    ngen = [random.choice(numbers) for _ in range(nnumbers)]
    sgen = [random.choice(symbols) for _ in range(nsymbols)]

    lgen = [ch for ch in lgen if ch in all_chars]
    ngen = [ch for ch in ngen if ch in all_chars]
    sgen = [ch for ch in sgen if ch in all_chars]

    combined_chars = lgen + ngen + sgen

    if len(combined_chars) == 0:
        password_var.set("No valid characters after generation.")
        return

    random.shuffle(combined_chars)
    password = ''.join(combined_chars)

    password_var.set(password)

def copy_to_clipboard():
    password = password_var.get()
    if password:
        pyperclip.copy(password)
        copy_status_var.set("Password copied to clipboard!")
root = tk.Tk()
root.title("Password Generator")
tk.Label(root, text="How many letters?:").grid(row=0, column=0, padx=10, pady=10)
letter_entry = tk.Entry(root)
letter_entry.grid(row=0, column=1, padx=10, pady=10)
tk.Label(root, text="How many numbers?:").grid(row=1, column=0, padx=10, pady=10)
number_entry = tk.Entry(root)
number_entry.grid(row=1, column=1, padx=10, pady=10)
tk.Label(root, text="How many symbols?:").grid(row=2, column=0, padx=10, pady=10)
symbol_entry = tk.Entry(root)
symbol_entry.grid(row=2, column=1, padx=10, pady=10)
tk.Label(root, text="Exclude characters:").grid(row=3, column=0, padx=10, pady=10)
exclude_entry = tk.Entry(root)
exclude_entry.grid(row=3, column=1, padx=10, pady=10)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=4, column=0, columnspan=2, pady=20)
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.grid(row=5, column=0, columnspan=2, pady=10)
password_var = tk.StringVar()
tk.Label(root, text="Generated Password:").grid(row=6, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, textvariable=password_var, width=40)
password_entry.grid(row=6, column=1, padx=10, pady=10)
copy_status_var = tk.StringVar()
tk.Label(root, textvariable=copy_status_var, fg="green").grid(row=7, column=0, columnspan=2, pady=10)
root.mainloop()
