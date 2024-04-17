import os
from docx2pdf import convert as convert_docx
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import load_workbook

def convert_to_pdf(file_path):
    # Извлекаем имя файла и его расширение из пути файла
    file_name, file_extension = os.path.splitext(file_path)
    
    # Определяем процесс конвертации в зависимости от типа файла
    if file_extension.lower() == '.docx':
        # Конвертируем DOCX в PDF с помощью библиотеки docx2pdf
        # Вывод PDF будет сохранен в папку 'converted'
        convert_docx(file_path, "converted", file_name + '.pdf')
        print(f"Файл '{file_path}' конвертирован в 'converted/{file_name}.pdf'")

    elif file_extension.lower() == '.xlsx':
        # Загружаем workbook из указанного файла
        wb = load_workbook(file_path)
        # Получаем активный лист workbook
        sheet = wb.active
        # Читаем данные из активного листа
        data = sheet.values
        # Извлекаем заголовки столбцов из первой строки данных
        columns = next(data)[0:]
        # Создаем DataFrame из данных для построения графика
        df = pd.DataFrame(data, columns=columns)
        # Создаем фигуру для графика с указанными размерами
        fig, ax = plt.subplots(figsize=(12, 4))
        ax.axis('tight')
        ax.axis('off')
        # Создаем таблицу внутри графика, расположив ее в центре
        ax.table(cellText=df.values, colLabels=df.columns, loc='center', cellLoc='center', rowLoc='center')
        # Сохраняем график в виде PDF в папке 'converted'
        plt.savefig('converted/' + file_name + '.pdf', format='pdf')
        print(f"Файл '{file_path}' конвертирован в 'converted/{file_name}.pdf'")
    else:
        # Выводим сообщение об ошибке, если тип файла не поддерживается
        print(f"Тип файла не поддерживается: {file_extension}")


if __name__ == "__main__":
    # Укажите путь к файлу, который нужно конвертировать
    file_path = input("Filename: ") # example.xlsx or example.docx
    convert_to_pdf(file_path)
