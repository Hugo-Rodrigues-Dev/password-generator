import tkinter as tk
from tkinter import ttk, messagebox
from password_generator import generate_password


class PasswordGeneratorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator 🔐")
        self.geometry("480x340")
        self.resizable(False, False)

        # Variables
        self.length_var = tk.IntVar(value=12)
        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)
        self.password_var = tk.StringVar(value="")

        self._build_ui()

    def _build_ui(self):
        container = ttk.Frame(self, padding=16)
        container.pack(fill=tk.BOTH, expand=True)

        # Length selector
        length_frame = ttk.Frame(container)
        length_frame.pack(fill=tk.X, pady=(0, 12))
        ttk.Label(length_frame, text="Password length (4-50)").pack(anchor=tk.W)
        length_row = ttk.Frame(length_frame)
        length_row.pack(fill=tk.X)
        self.length_spin = ttk.Spinbox(
            length_row,
            from_=4,
            to=50,
            textvariable=self.length_var,
            width=6,
        )
        self.length_spin.pack(side=tk.LEFT)
        length_scale = ttk.Scale(
            length_row,
            from_=4,
            to=50,
            orient=tk.HORIZONTAL,
            command=self._sync_scale_to_spin,
        )
        length_scale.set(self.length_var.get())
        length_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(12, 0))

        # Options
        opts = ttk.LabelFrame(container, text="Character sets")
        opts.pack(fill=tk.X, pady=(0, 12))
        ttk.Checkbutton(opts, text="Lowercase", variable=self.lower_var).grid(row=0, column=0, sticky=tk.W, padx=8, pady=4)
        ttk.Checkbutton(opts, text="Uppercase", variable=self.upper_var).grid(row=0, column=1, sticky=tk.W, padx=8, pady=4)
        ttk.Checkbutton(opts, text="Digits", variable=self.digits_var).grid(row=1, column=0, sticky=tk.W, padx=8, pady=4)
        ttk.Checkbutton(opts, text="Special", variable=self.special_var).grid(row=1, column=1, sticky=tk.W, padx=8, pady=4)

        # Generate + result
        actions = ttk.Frame(container)
        actions.pack(fill=tk.X)
        self.generate_btn = ttk.Button(actions, text="Generate", command=self.on_generate)
        self.generate_btn.pack(side=tk.LEFT)

        self.copy_btn = ttk.Button(actions, text="Copy", command=self.on_copy)
        self.copy_btn.pack(side=tk.LEFT, padx=(8, 0))

        self.result_entry = ttk.Entry(container, textvariable=self.password_var, state="readonly")
        self.result_entry.pack(fill=tk.X, pady=(12, 0))

        # Status/feedback
        self.status_var = tk.StringVar(value="")
        self.status_label = ttk.Label(container, textvariable=self.status_var, foreground="#666")
        self.status_label.pack(fill=tk.X, pady=(8, 0))

    def _sync_scale_to_spin(self, value):
        try:
            self.length_var.set(int(float(value)))
        except Exception:
            pass

    def on_generate(self):
        length = int(self.length_var.get())
        use_lower = bool(self.lower_var.get())
        use_upper = bool(self.upper_var.get())
        use_digits = bool(self.digits_var.get())
        use_special = bool(self.special_var.get())

        pwd = generate_password(length, use_lower, use_upper, use_digits, use_special)

        # The generator returns error messages as strings; detect and show.
        if isinstance(pwd, str) and ("must be between" in pwd or "You must enable" in pwd):
            self.status_var.set(pwd)
            self.password_var.set("")
        else:
            self.password_var.set(pwd)
            self.status_var.set("Password generated. Tip: click Copy to clipboard.")

    def on_copy(self):
        value = self.password_var.get()
        if not value:
            messagebox.showinfo("Copy", "No password to copy yet.")
            return
        try:
            self.clipboard_clear()
            self.clipboard_append(value)
            self.status_var.set("Copied to clipboard ✔")
        except Exception:
            messagebox.showerror("Copy", "Failed to copy to clipboard.")


if __name__ == "__main__":
    app = PasswordGeneratorGUI()
    app.mainloop()

