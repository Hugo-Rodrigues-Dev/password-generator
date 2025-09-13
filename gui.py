import tkinter as tk
from tkinter import ttk, messagebox
from password_generator import generate_password
from tkinter import font as tkfont


class PasswordGeneratorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Password Generator 🔐")
        self.geometry("520x410")
        self.resizable(False, False)

        # Variables
        self.length_var = tk.IntVar(value=12)
        self.lower_var = tk.BooleanVar(value=True)
        self.upper_var = tk.BooleanVar(value=True)
        self.digits_var = tk.BooleanVar(value=True)
        self.special_var = tk.BooleanVar(value=True)
        self.password_var = tk.StringVar(value="")

        self._apply_theme(mode="dark")
        self._build_ui()

    def _build_ui(self):
        container = ttk.Frame(self, style="Root.TFrame", padding=16)
        container.pack(fill=tk.BOTH, expand=True)

        # Header
        header = ttk.Frame(container, style="Root.TFrame")
        header.pack(fill=tk.X, pady=(0, 12))
        ttk.Label(
            header,
            text="Password Generator",
            style="Header.TLabel",
        ).pack(side=tk.LEFT)

        # Length selector
        length_frame = ttk.Frame(container, style="Card.TFrame")
        length_frame.pack(fill=tk.X, pady=(0, 12))
        ttk.Label(length_frame, text="Password length (4-50)", style="Muted.TLabel").pack(anchor=tk.W, padx=8, pady=(8, 4))
        length_row = ttk.Frame(length_frame, style="Card.TFrame")
        length_row.pack(fill=tk.X)
        self.length_spin = ttk.Spinbox(
            length_row,
            from_=4,
            to=50,
            textvariable=self.length_var,
            width=6,
            style="TSpinbox",
        )
        self.length_spin.pack(side=tk.LEFT, padx=(8, 0), pady=(0, 8))
        length_scale = ttk.Scale(
            length_row,
            from_=4,
            to=50,
            orient=tk.HORIZONTAL,
            command=self._sync_scale_to_spin,
            style="TScale",
        )
        length_scale.set(self.length_var.get())
        length_scale.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(12, 8))

        # Options
        opts = ttk.LabelFrame(container, text="Character sets", style="Card.TLabelframe")
        opts.pack(fill=tk.X, pady=(0, 12))
        ttk.Checkbutton(opts, text="Lowercase", variable=self.lower_var, style="Toggle.TCheckbutton").grid(row=0, column=0, sticky=tk.W, padx=8, pady=6)
        ttk.Checkbutton(opts, text="Uppercase", variable=self.upper_var, style="Toggle.TCheckbutton").grid(row=0, column=1, sticky=tk.W, padx=8, pady=6)
        ttk.Checkbutton(opts, text="Digits", variable=self.digits_var, style="Toggle.TCheckbutton").grid(row=1, column=0, sticky=tk.W, padx=8, pady=6)
        ttk.Checkbutton(opts, text="Special", variable=self.special_var, style="Toggle.TCheckbutton").grid(row=1, column=1, sticky=tk.W, padx=8, pady=6)

        # Generate + result
        actions = ttk.Frame(container, style="Root.TFrame")
        actions.pack(fill=tk.X)
        self.generate_btn = ttk.Button(actions, text="Generate", style="Accent.TButton", command=self.on_generate)
        self.generate_btn.pack(side=tk.LEFT, padx=(0, 8))

        self.copy_btn = ttk.Button(actions, text="Copy", style="Secondary.TButton", command=self.on_copy)
        self.copy_btn.pack(side=tk.LEFT)

        self.result_entry = ttk.Entry(container, textvariable=self.password_var, state="readonly", style="Result.TEntry")
        self.result_entry.pack(fill=tk.X, pady=(12, 0))

        # Status/feedback
        self.status_var = tk.StringVar(value="")
        self.status_label = ttk.Label(container, textvariable=self.status_var, style="Status.TLabel")
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

    def _apply_theme(self, mode="dark"):
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except Exception:
            pass

        # Palette (modern dark with indigo accent)
        palette = {
            "bg": "#0B1220",
            "surface": "#111827",
            "surface_alt": "#0F172A",
            "text": "#E5E7EB",
            "muted": "#9CA3AF",
            "accent": "#6366F1",
            "accent_hover": "#5458E3",
            "accent_active": "#4B50D1",
            "input_border": "#374151",
            # Toggle-specific tints
            "toggle_hover": "#1A2337",
            "toggle_selected": "#1F2A44",
            "toggle_pressed": "#19233B",
        }

        # Root background
        self.configure(background=palette["bg"])

        # Fonts
        base_font = tkfont.nametofont("TkDefaultFont")
        base_font.configure(size=10)
        header_font = tkfont.Font(family=base_font.actual("family"), size=16, weight="bold")

        # Global defaults
        style.configure(
            ".",
            background=palette["bg"],
            foreground=palette["text"],
            font=base_font,
        )

        # Frames / cards
        style.configure("Root.TFrame", background=palette["bg"]) 
        style.configure(
            "Card.TFrame",
            background=palette["surface"],
            relief="flat",
        )
        style.configure(
            "Card.TLabelframe",
            background=palette["surface"],
            foreground=palette["text"],
            borderwidth=0,
            relief="flat",
            padding=8,
        )
        style.configure(
            "Card.TLabelframe.Label",
            background=palette["surface"],
            foreground=palette["muted"],
            font=(base_font.actual("family"), 10, "bold"),
        )

        # Labels
        style.configure("Header.TLabel", background=palette["bg"], foreground=palette["text"], font=header_font)
        style.configure("Muted.TLabel", background=palette["surface"], foreground=palette["muted"]) 
        style.configure("Status.TLabel", background=palette["bg"], foreground=palette["muted"]) 

        # Buttons
        style.configure(
            "Accent.TButton",
            background=palette["accent"],
            foreground="#ffffff",
            borderwidth=0,
            focusthickness=3,
            focuscolor=palette["accent"],
            padding=(14, 8),
        )
        style.map(
            "Accent.TButton",
            background=[("active", palette["accent_hover"]), ("pressed", palette["accent_active"])],
        )
        style.configure(
            "Secondary.TButton",
            background=palette["surface_alt"],
            foreground=palette["text"],
            borderwidth=0,
            padding=(12, 8),
        )
        style.map(
            "Secondary.TButton",
            background=[("active", "#162036"), ("pressed", "#121B2E")],
        )

        # Entry
        style.configure(
            "TEntry",
            fieldbackground=palette["surface_alt"],
            foreground=palette["text"],
            insertcolor=palette["muted"],
            bordercolor=palette["input_border"],
            lightcolor=palette["input_border"],
            darkcolor=palette["input_border"],
            borderwidth=1,
            relief="flat",
            padding=8,
        )
        style.configure(
            "Result.TEntry",
            fieldbackground=palette["surface"],
            foreground=palette["text"],
        )

        # Scale
        style.configure(
            "TScale",
            background=palette["surface"],
            troughcolor=palette["surface_alt"],
            bordercolor=palette["input_border"],
        )

        # Spinbox
        style.configure(
            "TSpinbox",
            fieldbackground=palette["surface_alt"],
            foreground=palette["text"],
            arrowcolor=palette["text"],
            bordercolor=palette["input_border"],
            lightcolor=palette["input_border"],
            darkcolor=palette["input_border"],
            relief="flat",
            padding=4,
        )

        # Checkbutton (avoid white hover/active)
        style.configure(
            "Toggle.TCheckbutton",
            background=palette["surface"],
            foreground=palette["text"],
            focusthickness=2,
            focuscolor=palette["accent"],
            padding=(8, 6),
            relief="flat",
        )
        style.map(
            "Toggle.TCheckbutton",
            background=[
                ("active", palette["toggle_hover"]),
                ("selected", palette["toggle_selected"]),
                ("pressed", palette["toggle_pressed"]),
            ],
            foreground=[
                ("disabled", palette["muted"]),
            ],
        )
        # Try to tint the indicator (may vary by platform/theme support)
        try:
            style.map(
                "Toggle.TCheckbutton",
                indicatorcolor=[
                    ("selected", palette["accent"]),
                    ("!selected", palette["input_border"]),
                ],
            )
        except Exception:
            pass


if __name__ == "__main__":
    app = PasswordGeneratorGUI()
    app.mainloop()
