"""
ComPDFKit API Libraries Enums Module

This module contains all the enums used in the ComPDFKit API Libraries.

Dependencies:
    enum: Handle enumerations.
"""
from enum import Enum

class CPDFConversionEnum(Enum):
    """
    CPDFConversionEnum class

    Defines all the conversion types and url suffixes supported by the ComPDFKit API.
    """
    DOC_TO_PDF = "doc/pdf"
    DOCX_TO_PDF = "docx/pdf"
    XLSX_TO_PDF = "xlsx/pdf"
    XLS_TO_PDF = "xls/pdf"
    PPT_TO_PDF = "ppt/pdf"
    PPTX_TO_PDF = "pptx/pdf"
    TXT_TO_PDF = "txt/pdf"
    PNG_TO_PDF = "png/pdf"
    HTML_TO_PDF = "html/pdf"
    CSV_TO_PDF = "csv/pdf"
    RTF_TO_PDF = "rtf/pdf"

    PDF_TO_WORD = "pdf/docx"
    PDF_TO_EXCEL = "pdf/xlsx"
    PDF_TO_PPT = "pdf/pptx"
    PDF_TO_TXT = "pdf/txt"
    PDF_TO_PNG = "pdf/png"
    PDF_TO_JPG = "pdf/jpg"
    PDF_TO_HTML = "pdf/html"
    PDF_TO_RTF = "pdf/rtf"
    PDF_TO_CSV = "pdf/csv"
    PDF_TO_JSON = "pdf/json"
    IMAGE_TO_JSON = "img/json"

    @staticmethod
    def get_instance(value):
        for pdf_to_office_enum in CPDFConversionEnum:
            if pdf_to_office_enum.value == value:
                return pdf_to_office_enum
        return None


class CPDFDocumentAIEnum(Enum):
    """
    CPDFDocumentAIEnum class

    Defines all the document AI types and url suffixes supported by the ComPDFKit API.
    """
    OCR = "documentAI/ocr"
    MAGICCOLOR = "documentAI/magicColor"
    TABLEREC = "documentAI/tableRec"
    LAYOUTANALYSIS = "documentAI/layoutAnalysis"
    DEWARP = "documentAI/dewarp"
    DETECTIONSTAMP = "documentAI/detectionStamp"

    def get_value(self):
        return self.value

    @staticmethod
    def get_instance(value):
        for pdf_server_enum in CPDFDocumentAIEnum:
            if pdf_server_enum.value == value:
                return pdf_server_enum
        return None


class CPDFDocumentEditorEnum(Enum):
    """
    CPDFDocumentEditorEnum class

    Defines all the document page edit types and url suffixes supported by the ComPDFKit API.
    """
    SPLIT = "pdf/split"
    MERGE = "pdf/merge"
    COMPRESS = "pdf/compress"
    DELETE = "pdf/delete"
    EXTRACT = "pdf/extract"
    ROTATION = "pdf/rotation"
    INSERT = "pdf/insert"
    ADD_WATERMARK = "pdf/addWatermark"
    DEL_WATERMARK = "pdf/delWatermark"

    def get_value(self):
        return self.value

    @classmethod
    def get_instance(cls, value):
        for pdf_server_enum in cls:
            if pdf_server_enum.value == value:
                return pdf_server_enum
        return None
