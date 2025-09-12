# 🔐 Password Generator

Python password generator with two usage modes:
- Interactive console interface (`main.py`)
- Tkinter graphical interface (`gui.py`)

Both share the same generation engine (`password_generator.py`).

## ✨ Features

- Custom length (4 to 50)
- Optional inclusion of:
  - Lowercase letters
  - Uppercase letters
  - Digits
  - Special characters
- Random shuffle with at least one character from each selected set
- Copy button in the GUI

## 🧰 Requirements & Setup

- Python 3.8 or newer.
- Tkinter (required for the GUI):
  - Ubuntu/WSL: `sudo apt update && sudo apt install -y python3-tk`
  - Fedora: `sudo dnf install python3-tkinter`
  - Arch: `sudo pacman -S tk`
  - Windows/macOS: use Python from python.org (Tkinter is included by default).

Optional (recommended for development): Python virtual environment

```
python3 -m venv .venv
# Linux/macOS
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

This project has no pip dependencies; no `pip install -r requirements.txt` is needed.

WSL notes:
- On Windows 11 (WSLg), Tkinter apps display natively.
- On Windows 10/WSL, use an X server (e.g., VcXsrv) or run `gui.py` with Windows Python (`py -3 gui.py`).

## ▶️ Usage (Console)

```
python main.py
```

Example:

```
Enter password length (4-50): 12
Include lowercase letters? (y/n) : y
Include uppercase letters? (y/n) : y
Include digits? (y/n) : y
Include special characters? (y/n) : y

Generated password : D4r!p@q9W1s#
```

## 🖼️ Usage (GUI)

```
python gui.py
```

UI features:
- Length selector (Spinbox + slider)
- Checkboxes for each character category
- Generate button to create a password
- Read-only field for the result + Copy button
- Status message for validations

## 🧩 Structure

- `password_generator.py` — generation logic
- `main.py` — console version
- `gui.py` — graphical version

## 🗂️ Contributing / Development

- Create and activate a virtual environment (see above).
- Run the console version: `python main.py`
- Run the GUI: `python gui.py`
- Please keep the file structure and avoid unnecessary dependencies.

## 🧽 .gitignore

This repository includes a Python-appropriate `.gitignore` to avoid committing temporary files and build artifacts.

---

Feel free to fork and enhance the project.

[![GitHub release](https://img.shields.io/github/v/release/Hugo-Rodrigues-Dev/password-generator?style=flat&label=release)](https://github.com/Hugo-Rodrigues-Dev/password-generator/releases/tag/v1.0.0)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
