
# 🔐 Password Generator GUI App

A sleek and secure password generator built with Python and Tkinter. Includes light/dark mode, purpose tagging, secure password storage, and more.

---

## ✨ Features

- 🔢 Generate strong passwords with customizable length
- ✅ Options for uppercase, lowercase, numbers, and symbols
- 🎨 Light Mode / Dark Mode toggle
- ✍️ Add a purpose or label for each password (e.g., Gmail, Bank)
- 💾 Auto-save generated passwords to a `.csv` file
- 🔐 Password-protected access to view saved passwords
- ✏️ Secure password update with identity verification
- 📋 One-click copy to clipboard
- 🎁 Modern animated GUI interface

---

## 🖼 Interface Preview

![App Screenshot](./screenshot.png)

---

## 🚀 Getting Started

### Requirements
- Python 3.10 or higher
- Modules:
  - `tkinter` (built-in)
  - `csv`
  - `random`
  - `pyperclip` (for clipboard copy)
  - `os`

Install missing packages:
```bash
pip install pyperclip
```

---

## ▶️ Running the App

```bash
python password_generator_gui.py
```

---

## 🛠 Build to .EXE (Windows)

1. Open Command Prompt
2. Navigate to your script folder:
```bash
cd "D:\VS Code\Cod_Soft\password_generator_gui.py"
```
3. Run PyInstaller:
```bash
pyinstaller --onefile --windowed pass_gen.py
```
4. Your `.exe` will be inside the `dist` folder.

---

## 📁 File Structure

```
password-generator/
│
├── password_generator_gui.py           # Main Python script
├── passwords.csv                       # Auto-generated password store
├── README.md                           # This file
├── screenshot.png                      # UI screenshot (optional)
└── dist/
    └── password_generator_gui.exe      # Final executable (after build)
```

---

## 🔐 Security Notice

- Password viewing is protected by a master key.
- Saved passwords are stored in plain CSV. For production use, consider encryption.

---

## 📬 Feedback or Issues?

Feel free to open an issue or drop a suggestion!

---

## 📜 License

This project is open-source for personal and educational use.
