import logging
import win32com.client as win32

from docx2pdf import convert
from modal import show_error_message


def convert_docx_to_pdf(docx_path, pdf_path) -> None:
    """
    Конвертирует документ .docx в .pdf
    """
    try:
        convert(docx_path, pdf_path)
        logging.info(f"Конвертация {docx_path} в {pdf_path} завершена успешно.")

    except Exception as e:
        error_message: str = f"Ошибка при конвертации {docx_path} в {pdf_path}"
        error_message_for_log = error_message + f": {e}"
        
        logging.error(error_message_for_log)
        show_error_message(error_message)


def convert_excel_to_pdf(excel_path: str, pdf_path: str) -> None:
    """
    Открывает и обрабатывает .xlsx файл, конвертируя его в .pdf
    """
    try:
        # Обьект приложения Excel
        excel: win32.CDispatch = win32.Dispatch('Excel.Application')
        excel.Visible = False  # Скрыть Excel во время работы

        wb: object = excel.Workbooks.Open(excel_path)

        # Настройка параметров печати для сохранения стилей
        for sheet in wb.Sheets:
            sheet.PageSetup.Zoom = False  # Отключить масштабирование
            sheet.PageSetup.FitToPagesWide = 1  # Вписать по ширине одной страницы
            sheet.PageSetup.FitToPagesTall = False  # Не ограничивать по высоте страниц

            used_range = sheet.UsedRange
            used_range.Borders.Weight = 2  # Установка веса границ (1 - тонкие, 2 - средние, 3 - толстые)
            used_range.Borders.LineStyle = 1  # Установка стиля линий (1 - сплошные линии)


        # Публикация в формате pdf
        wb.ExportAsFixedFormat(0, pdf_path)
        wb.Close(SaveChanges=False)

        excel.Quit()

        logging.info(f"Конвертация {excel_path} в {pdf_path} завершена успешно.")

    except Exception as e:
        error_message: str = f"Ошибка при конвертации {excel_path} в {pdf_path}"
        error_message_for_log = error_message + f": {e}"

        logging.error(error_message_for_log)
        show_error_message(error_message)

        wb.Close(SaveChanges=False)

        excel.Quit()
