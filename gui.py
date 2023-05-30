import tkinter as tk
import fibonacci_module

def calculate_fibonacci():
    n = int(entry.get())
    fibs = fibonacci_module.print_fibonacci_range(range(n + 1))
    fibonacci_label["text"] = f"Fibonacci sequence up to {n}:\n{', '.join(map(str, fibs))}"

root = tk.Tk()
root.title("Fibonacci Calculator")

frame = tk.Frame(root)
frame.pack(pady=20)

label = tk.Label(frame, text="Enter a number:")
label.grid(row=0, column=0)

entry = tk.Entry(frame)
entry.grid(row=0, column=1)

button = tk.Button(frame, text="Calculate", command=calculate_fibonacci)
button.grid(row=0, column=2, padx=10)

fibonacci_label = tk.Label(root, text="Fibonacci sequence will be displayed here.")
fibonacci_label.pack(pady=20)

root.mainloop()
