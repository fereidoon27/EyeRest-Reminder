# EyeRest-Reminder: Syntax Explanation

This document explains the important lines of code used in the **EyeRest-Reminder** script to help beginners understand the syntax and logic behind it.

## 1. Importing Modules
```python
import time
import datetime
import tkinter as tk
from tkinter import font, Entry
```
### Explanation:
- `import time` – Imports the time module, which provides time-related functions like `sleep()`.
- `import datetime` – Imports the datetime module (not used in the script but useful for time-related operations).
- `import tkinter as tk` – Imports the **Tkinter** module for creating a GUI.
- `from tkinter import font, Entry` – Imports specific Tkinter components to define fonts and create input fields.

## 2. Creating the Main Tkinter Window
```python
root = tk.Tk()
```
### Explanation:
- `tk.Tk()` – Creates the main window (also called the **root window**) where all widgets (labels, input fields, etc.) will be placed.

## 3. Configuring Fullscreen Mode
```python
root.attributes('-fullscreen', True)
root.configure(bg='white')
```
### Explanation:
- `root.attributes('-fullscreen', True)` – Makes the window fullscreen, covering the entire screen.
- `root.configure(bg='white')` – Sets the background color of the window to **white**.

## 4. Creating a Label Widget for the Message
```python
label = tk.Label(
    root,
    text=message,
    font=message_font,
    bg='white',
    fg='black',
    wraplength=screen_width-100
)
label.pack(expand=True)
```
### Explanation:
- `tk.Label(root, text=message, font=message_font, bg='white', fg='black')`
  - Creates a text label in the **root** window.
  - `text=message` – Displays the **message** inside the label.
  - `font=message_font` – Uses the predefined **bold Arial** font.
  - `bg='white'` – Background color is white.
  - `fg='black'` – Text color is black.
  - `wraplength=screen_width-100` – Ensures text wraps instead of overflowing.
- `.pack(expand=True)` – Centers the label and makes it expand within the available space.

## 5. Creating an Input Field (Entry Widget)
```python
entry = Entry(root, font=input_font, justify='center')
entry.pack(pady=10)
entry.focus()
```
### Explanation:
- `Entry(root, font=input_font, justify='center')` – Creates an input box inside the root window.
  - `font=input_font` – Uses a readable font size.
  - `justify='center'` – Aligns text input in the center.
- `.pack(pady=10)` – Adds **padding** (vertical spacing).
- `.focus()` – Automatically focuses the input field so the user can type immediately.

## 6. Handling User Input (Checking if "OK" is Typed)
```python
def check_input(event=None):
    if entry.get().upper() == 'OK':
        root.destroy()
    else:
        entry.delete(0, tk.END)
```
### Explanation:
- `entry.get()` – Retrieves the text entered by the user.
- `.upper()` – Converts the input text to **uppercase** (so "ok" and "OK" both work).
- `if entry.get().upper() == 'OK':` – Checks if the user typed "OK".
  - If **true**, `root.destroy()` **closes** the window.
  - Otherwise, `.delete(0, tk.END)` **clears** the input field.

## 7. Binding the Enter Key to Check Input
```python
entry.bind('<Return>', check_input)
```
### Explanation:
- `entry.bind('<Return>', check_input)` – Calls the `check_input` function **when the user presses Enter**.
  - `<Return>` refers to the **Enter key** in Tkinter.

## 8. Preventing Window Closure via Close Button or Alt+F4
```python
def disable_close():
    pass

root.protocol("WM_DELETE_WINDOW", disable_close)
```
### Explanation:
- `def disable_close(): pass` – Defines an **empty function** that does nothing.
- `root.protocol("WM_DELETE_WINDOW", disable_close)` – Overrides the default close behavior to **disable window closure** using the "X" button or Alt+F4.

## 9. Creating an Infinite Loop for Alerts
```python
while True:
    create_fullscreen_alert(message)
    time.sleep(interval)
```
### Explanation:
- `while True:` – **Infinite loop**, ensuring that alerts keep appearing every 20 minutes.
- `create_fullscreen_alert(message)` – Calls the function to **display the alert**.
- `time.sleep(interval)` – **Pauses execution** for 20 minutes before displaying the next alert.

## 10. Running the Script (Main Entry Point)
```python
if __name__ == "__main__":
    main()
```
### Explanation:
- `if __name__ == "__main__":` – Ensures that the script runs **only when executed directly**.
- `main()` – Calls the `main()` function to start the alert system.

---

## Conclusion
This guide breaks down the key parts of the **EyeRest-Reminder** script, explaining the Python syntax and Tkinter methods used. By understanding these concepts, you can modify and expand the script for your own needs!

