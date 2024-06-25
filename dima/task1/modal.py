import tkinter as tk
from tkinter import messagebox


def show_error_message(message: str) -> None:
    """
    Отображает модальное окно с сообщением об ошибке.
    """
    root: tk.Tk = tk.Tk()
    root.withdraw()  # Прячет главное окно

    messagebox.showerror("Ошибка", message)

    root.destroy()
