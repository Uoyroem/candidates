import os
import logging

from typing import AnyStr
from convert import convert_docx_to_pdf, convert_excel_to_pdf
from modal import show_error_message


def main(input_file: str) -> None:
    """
        Выполняет основной функционал
    """
    # Путь до данной директории
    current_file: AnyStr = os.path.abspath(__file__)
    current_directory: AnyStr = os.path.dirname(current_file)

    # Путь до входного файла
    input_file_path: str = current_directory + "/files/Input/" + input_file

    # Проверка на существование файла
    if not os.path.exists(input_file_path):
        error_message: str = f"Файл {input_file_path} не существует."

        logging.error(error_message)
        show_error_message(error_message)

        return

    # Расширение файла
    file_extension = os.path.splitext(input_file)[1].lower()

    # Путь до выходного файла
    output_file_path = current_directory + "/files/Output/" + input_file.replace(file_extension, ".pdf")

    if file_extension == ".docx":
        convert_docx_to_pdf(input_file_path, output_file_path)
    elif file_extension == ".xlsx":
        convert_excel_to_pdf(input_file_path, output_file_path)
    else:
        error_message = "Неподдерживаемый формат файла. Пожалуйста, используйте .docx или .xlsx."
        logging.error(error_message)
        show_error_message(error_message)


# Настройка логирования
logging.basicConfig(filename='conversion.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s', encoding = "UTF-8")


if __name__ == "__main__":
    file_path: str = input('Введите имя файла с папки files/Input: ')
    main(file_path)
