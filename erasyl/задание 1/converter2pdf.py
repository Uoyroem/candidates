import docx2pdf
from openpyxl import load_workbook
import logging
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog


def convert_docx_to_pdf(input_docx_path, output_pdf_path, log_file_path='conversion_logs.txt'):
    try:
        docx2pdf.convert(input_docx_path, output_pdf_path)
        logging.info(f"Successfully converted")
    except Exception as e:
        logging.error(f"Error converting to PDF: {str(e)}")
        messagebox.showerror("Error", f"Conversion failed: {str(e)}")


def convert_xlsx_to_pdf(input_xlsx_path, output_pdf_path, log_file_path='conversion_logs.txt'):
    try:
        wb = load_workbook(input_xlsx_path)
        wb.save(output_pdf_path)
        logging.info(f"Successfully converted")
    except Exception as e:
        logging.error(f"Error converting to PDF: {str(e)}")
        messagebox.showerror("Error", f"Conversion failed: {str(e)}")


def main():
    # Выбор файла для конвертации
    input_file_path = filedialog.askopenfilename(title="Select a file for conversion", filetypes=[("Word Documents", "*.docx"), ("Excel Documents", "*.xlsx")])

    if not input_file_path:
        messagebox.showwarning("Warning", "No file selected for conversion.")
        return

    # Определение выходного пути и формата
    output_file_path = filedialog.asksaveasfilename(title="Save as", defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])

    if not output_file_path:
        messagebox.showwarning("Warning", "No output file selected.")
        return

    # Настройка логирования
    logging.basicConfig(filename='conversion_logs.txt', level=logging.INFO)

    # Конвертация в зависимости от формата файла
    if input_file_path.lower().endswith('.docx'):
        convert_docx_to_pdf(input_file_path, output_file_path)
    elif input_file_path.lower().endswith('.xlsx'):
        convert_xlsx_to_pdf(input_file_path, output_file_path)
    else:
        messagebox.showwarning("Warning", "Unsupported file format.")


if __name__ == "__main__":
    main()
