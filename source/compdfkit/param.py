"""
This module contains all the parameter classes used in the ComPDFKit API Libraries.
"""
import json
from .enums import CPDFConversionEnum, CPDFDocumentAIEnum, CPDFDocumentEditorEnum
from .utils import ParameterValidator


class CPDFFileParameter:
    """
    CPDFFileParameter class

    This class defines the common parameters for all the file conversion types.
    """

    def to_cpdf_json_str(self):
        """
        Convert the parameter object to json string.
        """
        pass


class CCSVToPDFParameter(CPDFFileParameter):
    pass


class CExcelToPDFParameter(CPDFFileParameter):
    pass


class CHtmlToPDFParameter(CPDFFileParameter):
    pass


class CPDFAddWatermarkParameter(CPDFFileParameter):
    TYPE_TEXT = "text"
    TYPE_IMAGE = "image"

    VERTALIGN_TOP = "top"
    VERTALIGN_CENTER = "center"
    VERTALIGN_BOTTOM = "bottom"

    HORIZALIGN_LEFT = "left"
    HORIZALIGN_CENTER = "center"
    HORIZALIGN_RIGHT = "right"

    def __init__(self):
        self._type = None
        self._scale = None
        self._opacity = None
        self._rotation = None
        self._target_pages = None
        self._vertalign = None
        self._horizalign = None
        self._xoffset = None
        self._yoffset = None
        self._content = None
        self._text_color = None
        self._front = None
        self._full_screen = None
        self._horizontal_space = None
        self._vertical_space = None
        self._extension = None

    @property
    def type(self):
        """
        Type of the watermark.Must be 'text' or 'image'.
        """
        return self._type

    @type.setter
    def type(self, value):
        if value not in [self.TYPE_TEXT, self.TYPE_IMAGE]:
            raise ValueError("Invalid value for type. Must be 'text' or 'image'.")
        self._type = value

    @property
    def scale(self):
        """
        Scale of the watermark. Must be greater than 0.
        """
        return self._scale

    @scale.setter
    def scale(self, value):
        if float(value) <= 0:
            raise ValueError("Invalid value for scale. Must be greater than 0.")
        self._scale = value

    @property
    def opacity(self):
        """
        Opacity of the watermark. Must be between 0 and 1.
        """
        return self._opacity

    @opacity.setter
    def opacity(self, value):
        if float(value) < 0 or float(value) > 1:
            raise ValueError("Invalid value for opacity. Must be between 0 and 1.")
        self._opacity = value

    @property
    def rotation(self):
        """
        Rotation of the watermark.
        """
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value

    @property
    def target_pages(self):
        """
        Target pages of the watermark. Must be in format like 1,2,3 or 1-3,4,5.
        """
        return self._target_pages

    @target_pages.setter
    def target_pages(self, value):
        self._target_pages = ParameterValidator.validate_pages(value)

    @property
    def vertalign(self):
        """
        Vertical alignment of the watermark. Must be 'top', 'center' or 'bottom'.
        """
        return self._vertalign

    @vertalign.setter
    def vertalign(self, value):
        if value not in [self.VERTALIGN_TOP, self.VERTALIGN_CENTER, self.VERTALIGN_BOTTOM]:
            raise ValueError("Invalid value for vertAlign. Must be 'top', 'center' or 'bottom'.")
        self._vertalign = value

    @property
    def horizalign(self):
        """
        Horizontal alignment of the watermark. Must be 'left', 'center' or 'right'.
        """
        return self._horizalign

    @horizalign.setter
    def horizalign(self, value):
        if value not in [self.HORIZALIGN_LEFT, self.HORIZALIGN_CENTER, self.HORIZALIGN_RIGHT]:
            raise ValueError("Invalid value for horizAlign. Must be 'left', 'center' or 'right'.")
        self._horizalign = value

    @property
    def xoffset(self):
        """
        x offset of the watermark.
        """
        return self._xoffset

    @xoffset.setter
    def xoffset(self, value):
        self._xoffset = value

    @property
    def yoffset(self):
        """
        y offset of the watermark.
        """
        return self._yoffset

    @yoffset.setter
    def yoffset(self, value):
        self._yoffset = value

    @property
    def content(self):
        """
        Content of the watermark.
        """
        return self._content

    @content.setter
    def content(self, value):
        self._content = value

    @property
    def text_color(self):
        """
        Text color of the watermark. Must be in hex format like #000000.
        """
        return self._text_color

    @text_color.setter
    def text_color(self, value):
        self._text_color = ParameterValidator.validate_color(value)

    @property
    def front(self):
        """
        The watermark is in front of page or not.
        """
        return self._front

    @front.setter
    def front(self, value):
        self._front = value

    @property
    def full_screen(self):
        """
        The watermark is full screen or not.
        """
        return self._full_screen

    @full_screen.setter
    def full_screen(self, value):
        self._full_screen = value

    @property
    def horizontal_space(self):
        """
        The horizontal space of full screen watermark.
        """
        return self._horizontal_space

    @horizontal_space.setter
    def horizontal_space(self, value):
        self._horizontal_space = value

    @property
    def vertical_space(self):
        """
        The vertical space of full screen watermark.
        """
        return self._vertical_space

    @vertical_space.setter
    def vertical_space(self, value):
        self._vertical_space = value

    @property
    def extension(self):
        """
        The extension message about watermark.
        """
        return self._extension

    @extension.setter
    def extension(self, value):
        self._extension = value

    def to_cpdf_json_str(self):
        json_dict = {}
        if self._type is not None:
            json_dict["type"] = self._type
        if self._scale is not None:
            json_dict["scale"] = self._scale
        if self._opacity is not None:
            json_dict["opacity"] = self._opacity
        if self._rotation is not None:
            json_dict["rotation"] = self._rotation
        if self._target_pages is not None:
            json_dict["targetPages"] = self._target_pages
        if self._vertalign is not None:
            json_dict["vertAlign"] = self._vertalign
        if self._horizalign is not None:
            json_dict["horizAlign"] = self._horizalign
        if self._xoffset is not None:
            json_dict["xOffset"] = self._xoffset
        if self._yoffset is not None:
            json_dict["yOffset"] = self._yoffset
        if self._content is not None:
            json_dict["content"] = self._content
        if self._text_color is not None:
            json_dict["textColor"] = self._text_color
        if self._front is not None:
            json_dict["front"] = self._front
        if self._full_screen is not None:
            json_dict["fullScreen"] = self._full_screen
        if self._horizontal_space is not None:
            json_dict["horizontalSpace"] = self._horizontal_space
        if self._vertical_space is not None:
            json_dict["verticalSpace"] = self._vertical_space
        if self._extension is not None:
            json_dict["extension"] = self._extension
        return json.dumps(json_dict)


class CPDFCompressParameter(CPDFFileParameter):
    def __init__(self):
        super().__init__()
        self._quality = None

    @property
    def quality(self):
        return self._quality

    @quality.setter
    def quality(self, value):
        if int(value) < 0 or int(value) > 100:
            raise ValueError("Invalid value for quality. Must be between 0 and 100.")
        self._quality = value

    def to_cpdf_json_str(self):
        json_dict = {"quality": self._quality}
        return json.dumps(json_dict)


class CPDFDeleteWatermarkParameter(CPDFFileParameter):
    pass


class CPDFFormRecognizerParameter(CPDFFileParameter):
    LANG_AUTO = "auto"
    LANG_ENGLISH = "english"
    LANG_CHINESE = "chinese"
    LANG_CHINESE_TRA = "chinese_tra"
    LANG_KOREAN = "korean"
    LANG_JAPANESE = "japanese"
    LANG_LATIN = "latin"
    LANG_DEVANAGARI = "devanagari"

    def __init__(self):
        super().__init__()
        self._lang = None

    @property
    def lang(self):
        """
        The ocr language. Must be 'auto', 'english', 'chinese', 'chinese_tra', 'korean', 'japanese', 'latin' or
        'devanagari'.
        """
        return self._lang

    @lang.setter
    def lang(self, value):
        if value not in [self.LANG_AUTO, self.LANG_ENGLISH, self.LANG_CHINESE, self.LANG_CHINESE_TRA,
                         self.LANG_KOREAN, self.LANG_JAPANESE, self.LANG_LATIN, self.LANG_DEVANAGARI]:
            raise ValueError("Invalid value for lang. Must be 'auto', 'english', 'chinese', 'chinese_tra', "
                             "'korean', 'japanese', 'latin' or 'devanagari'.")
        self._lang = value

    def to_cpdf_json_str(self):
        json_dict = {"lang": self._lang}
        return json.dumps(json_dict)


class CPDFImageSharpeningEnhancementParameter(CPDFFileParameter):
    pass


class CPDFLayoutAnalysisParameter(CPDFFileParameter):
    pass


class CPDFOcrParameter(CPDFFileParameter):
    LANG_AUTO = "auto"
    LANG_ENGLISH = "english"
    LANG_CHINESE = "chinese"
    LANG_CHINESE_TRA = "chinese_tra"
    LANG_KOREAN = "korean"
    LANG_JAPANESE = "japanese"
    LANG_LATIN = "latin"
    LANG_DEVANAGARI = "devanagari"

    def __init__(self):
        super().__init__()
        self._lang = None

    @property
    def lang(self):
        """
        The ocr language. Must be 'auto', 'english', 'chinese', 'chinese_tra', 'korean', 'japanese', 'latin' or
        'devanagari'.
        """
        return self._lang

    @lang.setter
    def lang(self, value):
        if value not in [self.LANG_AUTO, self.LANG_ENGLISH, self.LANG_CHINESE, self.LANG_CHINESE_TRA,
                         self.LANG_KOREAN, self.LANG_JAPANESE, self.LANG_LATIN, self.LANG_DEVANAGARI]:
            raise ValueError("Invalid value for lang. Must be 'auto', 'english', 'chinese', 'chinese_tra', "
                             "'korean', 'japanese', 'latin' or 'devanagari'.")
        self._lang = value

    def to_cpdf_json_str(self):
        json_dict = {"lang": self._lang}
        return json.dumps(json_dict)


class CPDFPageDeleteParameter(CPDFFileParameter):

    def __init__(self):
        super().__init__()
        self._page_options = []

    @property
    def page_options(self):
        """
        The pages of the file to be deleted. The item in list must be in format like "1" or "1-3".
        """
        return self._page_options

    @page_options.setter
    def page_options(self, value):
        self._page_options = value

    def to_cpdf_json_str(self):
        json_dict = {"pageOptions": self._page_options}
        return json.dumps(json_dict)


class CPDFPageExtractParameter(CPDFFileParameter):

    def __init__(self):
        super().__init__()
        self._page_options = []

    @property
    def page_options(self):
        """
        The pages of the file to be extracted. The item in list must be in format like "1" or "1-3".
        """
        return self._page_options

    @page_options.setter
    def page_options(self, value):
        self._page_options = value

    def to_cpdf_json_str(self):
        json_dict = {"pageOptions": self._page_options}
        return json.dumps(json_dict)


class CPDFPageInsertParameter(CPDFFileParameter):

    def __init__(self):
        self._target_page = None
        self._width = "595"
        self._height = "842"
        self._number = "1"

    @property
    def target_page(self):
        """
        The target page index of the file to be inserted.
        """
        return self._target_page

    @target_page.setter
    def target_page(self, value):
        self._target_page = ParameterValidator.validate_pages(value)

    @property
    def width(self):
        """
        The width of the page to be inserted. Must be greater than 0.
        """
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        """
        The height of the page to be inserted. Must be greater than 0.
        """
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def number(self):
        """
        The number of the pages to be inserted. Must be greater than 0.
        """
        return self._number

    @number.setter
    def number(self, value):
        if int(value) <= 0:
            raise ValueError("Invalid value for number. Must be greater than 0.")
        self._number = value

    def to_cpdf_json_str(self):
        json_dict = {"targetPage": self._target_page,
                     "width": self._width,
                     "height": self._height,
                     "number": self._number}
        return json.dumps(json_dict)


class CPDFPageMergeParameter(CPDFFileParameter):
    def __init__(self):
        super().__init__()
        self._page_options = []

    @property
    def page_options(self):
        """
        The pages of the file to be merged. The item in list must be in format like "1" or "1-3".
        """
        return self._page_options

    @page_options.setter
    def page_options(self, value):
        self._page_options = value

    def to_cpdf_json_str(self):
        json_dict = {"pageOptions": self._page_options}
        return json.dumps(json_dict)


class CPDFPageRotationParameter(CPDFFileParameter):

    def __init__(self):
        super().__init__()
        self._page_options = []
        self._rotation = ""

    @property
    def page_options(self):
        """
        The pages of the file to be rotated. The item in list must be in format like "1" or "1-3".
        """
        return self._page_options

    @page_options.setter
    def page_options(self, value):
        self._page_options = value

    @property
    def rotation(self):
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        self._rotation = value

    def to_cpdf_json_str(self):
        json_dict = {"pageOptions": self._page_options,
                     "rotation": self._rotation}
        return json.dumps(json_dict)


class CPDFPageSplitParameter(CPDFFileParameter):

    def __init__(self):
        super().__init__()
        self._page_options = []

    @property
    def page_options(self):
        """
        The pages of the file to be split. The item in list must be in format like "1" or "1-3".
        """
        return self._page_options

    @page_options.setter
    def page_options(self, value):
        self._page_options = value

    def to_cpdf_json_str(self):
        json_dict = {"pageOptions": self._page_options}
        return json.dumps(json_dict)


class CPDFStampInspectionParameter(CPDFFileParameter):
    pass


class CPDFToCSVParameter(CPDFFileParameter):
    IS_CSV_MERGE = "1"
    NOT_IS_CSV_MERGE = "0"

    def __init__(self):
        super().__init__()
        self._is_csv_merge = None

    @property
    def is_csv_merge(self):
        """
        Whether to merge the csv files or not.
        """
        return self._is_csv_merge

    @is_csv_merge.setter
    def is_csv_merge(self, value):
        if value not in [self.IS_CSV_MERGE, self.NOT_IS_CSV_MERGE]:
            raise ValueError("Invalid value for isCsvMerge. Must be '1' or '0'.")
        self._is_csv_merge = value

    def to_cpdf_json_str(self):
        json_dict = {"isCsvMerge": self._is_csv_merge}
        return json.dumps(json_dict)


class CPDFToExcelParameter(CPDFFileParameter):
    IS_CONTAIN_ANNOT = "1"
    NOT_IS_CONTAIN_ANNOT = "0"
    IS_CONTAIN_IMG = "1"
    NOT_IS_CONTAIN_IMG = "0"

    def __init__(self):
        super().__init__()
        self._content_options = None
        self._worksheet_options = None
        self._is_contain_annot = None
        self._is_contain_img = None

    @property
    def content_options(self):
        """
        The content options of the Excel file. ("1":OnlyText, "2":OnlyTable, "3":AllContent)
        """
        return self._content_options

    @content_options.setter
    def content_options(self, value):
        self._content_options = value

    @property
    def worksheet_options(self):
        """
        The worksheet options of the Excel file. ("1":ForEachTable, "2":ForEachPage, "3":ForTheDocument)
        """
        return self._worksheet_options

    @worksheet_options.setter
    def worksheet_options(self, value):
        self._worksheet_options = value

    @property
    def is_contain_annot(self):
        """
        Whether to contain the annotations or not.
        """
        return self._is_contain_annot

    @is_contain_annot.setter
    def is_contain_annot(self, value):
        if value not in [self.IS_CONTAIN_ANNOT, self.NOT_IS_CONTAIN_ANNOT]:
            raise ValueError("Invalid value for isContainAnnot. Must be '1' or '0'.")
        self._is_contain_annot = value

    @property
    def is_contain_img(self):
        """
        Whether to contain the images or not.
        """
        return self._is_contain_img

    @is_contain_img.setter
    def is_contain_img(self, value):
        if value not in [self.IS_CONTAIN_IMG, self.NOT_IS_CONTAIN_IMG]:
            raise ValueError("Invalid value for isContainImg. Must be '1' or '0'.")
        self._is_contain_img = value

    def to_cpdf_json_str(self):
        json_dict = {"contentOptions": self._content_options, "worksheetOptions": self._worksheet_options,
                     "isContainAnnot": self._is_contain_annot, "isContainImg": self._is_contain_img}
        return json.dumps(json_dict)


class CPDFToHtmlParameter(CPDFFileParameter):
    IS_CONTAIN_ANNOT = "1"
    NOT_IS_CONTAIN_ANNOT = "0"
    IS_CONTAIN_IMG = "1"
    NOT_IS_CONTAIN_IMG = "0"

    SINGLE_PAGE = "1"
    SINGLE_PAGE_NAVIGATION_BY_BOOKMARKS = "2"
    MULTIPLE_PAGES = "3"
    MULTIPLE_PAGES_SPLIT_BY_BOOKMARKS = "4"

    def __init__(self):
        super().__init__()
        self._page_options = None
        self._is_contain_annot = None
        self._is_contain_img = None

    @property
    def page_options(self):
        """
        The page options of the HTML file.
        """
        return self._page_options

    @page_options.setter
    def page_options(self, value):
        if value not in [self.SINGLE_PAGE, self.SINGLE_PAGE_NAVIGATION_BY_BOOKMARKS, self.MULTIPLE_PAGES,
                         self.MULTIPLE_PAGES_SPLIT_BY_BOOKMARKS]:
            raise ValueError("Invalid value for pageOptions. Must be '1', '2', '3' or '4'.")
        self._page_options = value

    @property
    def is_contain_annot(self):
        """
        Whether to contain the annotations or not.
        """
        return self._is_contain_annot

    @is_contain_annot.setter
    def is_contain_annot(self, value):
        if value not in [self.IS_CONTAIN_ANNOT, self.NOT_IS_CONTAIN_ANNOT]:
            raise ValueError("Invalid value for isContainAnnot. Must be '1' or '0'.")
        self._is_contain_annot = value

    @property
    def is_contain_img(self):
        """
        Whether to contain the images or not.
        """
        return self._is_contain_img

    @is_contain_img.setter
    def is_contain_img(self, value):
        if value not in [self.IS_CONTAIN_IMG, self.NOT_IS_CONTAIN_IMG]:
            raise ValueError("Invalid value for isContainImg. Must be '1' or '0'.")
        self._is_contain_img = value

    def to_cpdf_json_str(self):
        json_dict = {"pageOptions": self._page_options, "isContainAnnot": self._is_contain_annot,
                     "isContainImg": self._is_contain_img}
        return json.dumps(json_dict)


class CPDFToJpgParameter(CPDFFileParameter):
    def __init__(self):
        super().__init__()
        self._img_dpi = "300"

    @property
    def img_dpi(self):
        """
        The DPI of the image. Must be greater than 0.
        """
        return self._img_dpi

    @img_dpi.setter
    def img_dpi(self, value):
        if int(value) <= 0:
            raise ValueError("Invalid value for DPI. Must be greater than 0")

    def to_cpdf_json_str(self):
        json_dict = {"imgDpi": self._img_dpi}
        return json.dumps(json_dict)


class CPDFToPngParameter(CPDFFileParameter):
    def __init__(self):
        super().__init__()
        self._img_dpi = "300"

    @property
    def img_dpi(self):
        """
        The DPI of the image. Must be greater than 0.
        """
        return self._img_dpi

    @img_dpi.setter
    def img_dpi(self, value):
        if int(value) <= 0:
            raise ValueError("Invalid value for DPI. Must be greater than 0")

    def to_cpdf_json_str(self):
        json_dict = {"imgDpi": self._img_dpi}
        return json.dumps(json_dict)


class CPDFToPPTParameter(CPDFFileParameter):
    IS_CONTAIN_ANNOT = "1"
    NOT_IS_CONTAIN_ANNOT = "0"
    IS_CONTAIN_IMG = "1"
    NOT_IS_CONTAIN_IMG = "0"

    def __init__(self):
        super().__init__()
        self._is_contain_annot = None
        self._is_contain_img = None

    @property
    def is_contain_annot(self):
        """
        Whether to contain the annotations or not.
        """
        return self._is_contain_annot

    @is_contain_annot.setter
    def is_contain_annot(self, value):
        if value not in [self.IS_CONTAIN_ANNOT, self.NOT_IS_CONTAIN_ANNOT]:
            raise ValueError("Invalid value for isContainAnnot. Must be '1' or '0'.")
        self._is_contain_annot = value

    @property
    def is_contain_img(self):
        """
        Whether to contain the images or not.
        """
        return self._is_contain_img

    @is_contain_img.setter
    def is_contain_img(self, value):
        if value not in [self.IS_CONTAIN_IMG, self.NOT_IS_CONTAIN_IMG]:
            raise ValueError("Invalid value for isContainImg. Must be '1' or '0'.")
        self._is_contain_img = value

    def to_cpdf_json_str(self):
        json_dict = {"isContainAnnot": self._is_contain_annot, "isContainImg": self._is_contain_img}
        return json.dumps(json_dict)


class CPDFToRTFParameter(CPDFFileParameter):
    IS_CONTAIN_ANNOT = "1"
    NOT_IS_CONTAIN_ANNOT = "0"
    IS_CONTAIN_IMG = "1"
    NOT_IS_CONTAIN_IMG = "0"

    def __init__(self):
        super().__init__()
        self._is_contain_annot = None
        self._is_contain_img = None

    @property
    def is_contain_annot(self):
        """
        Whether to contain the annotations or not.
        """
        return self._is_contain_annot

    @is_contain_annot.setter
    def is_contain_annot(self, value):
        if value not in [self.IS_CONTAIN_ANNOT, self.NOT_IS_CONTAIN_ANNOT]:
            raise ValueError("Invalid value for isContainAnnot. Must be '1' or '0'.")
        self._is_contain_annot = value

    @property
    def is_contain_img(self):
        """
        Whether to contain the images or not.
        """
        return self._is_contain_img

    @is_contain_img.setter
    def is_contain_img(self, value):
        if value not in [self.IS_CONTAIN_IMG, self.NOT_IS_CONTAIN_IMG]:
            raise ValueError("Invalid value for isContainImg. Must be '1' or '0'.")
        self._is_contain_img = value

    def to_cpdf_json_str(self):
        json_dict = {"isContainAnnot": self._is_contain_annot, "isContainImg": self._is_contain_img}
        return json.dumps(json_dict)


class CPDFToTxtParameter(CPDFFileParameter):
    pass

class CPDFToWordParameter(CPDFFileParameter):
    IS_CONTAIN_ANNOT = "1"
    NOT_IS_CONTAIN_ANNOT = "0"
    IS_CONTAIN_IMG = "1"
    NOT_IS_CONTAIN_IMG = "0"
    IS_FLOW_LAYOUT = "1"
    NOT_IS_FLOW_LAYOUT = "0"

    def __init__(self):
        super().__init__()
        self._is_contain_annot = self.IS_CONTAIN_ANNOT
        self._is_contain_img = self.IS_CONTAIN_IMG
        self._is_flow_layout = self.NOT_IS_FLOW_LAYOUT

    @property
    def is_contain_annot(self):
        """
        Whether to contain the annotations or not.
        """
        return self._is_contain_annot

    @is_contain_annot.setter
    def is_contain_annot(self, value):
        if value not in [self.IS_CONTAIN_ANNOT, self.NOT_IS_CONTAIN_ANNOT]:
            raise ValueError("Invalid value for isContainAnnot. Must be '1' or '0'.")
        self._is_contain_annot = value

    @property
    def is_contain_img(self):
        """
        Whether to contain the images or not.
        """
        return self._is_contain_img

    @is_contain_img.setter
    def is_contain_img(self, value):
        if value not in [self.IS_CONTAIN_IMG, self.NOT_IS_CONTAIN_IMG]:
            raise ValueError("Invalid value for isContainImg. Must be '1' or '0'.")
        self._is_contain_img = value

    @property
    def is_flow_layout(self):
        """
        Whether to use flow layout or not.
        """
        return self._is_flow_layout

    @is_flow_layout.setter
    def is_flow_layout(self, value):
        if value not in [self.IS_FLOW_LAYOUT, self.NOT_IS_FLOW_LAYOUT]:
            raise ValueError("Invalid value for isFlowLayout. Must be '1' or '0'.")
        self._is_flow_layout = value

    def to_cpdf_json_str(self):
        json_dict = {"isContainAnnot": self._is_contain_annot, "isContainImg": self._is_contain_img,
                     "isFlowLayout": self._is_flow_layout}
        return json.dumps(json_dict)


class CPDFTrimCorrectionParameter(CPDFFileParameter):
    pass


class CPngToPDFParameter(CPDFFileParameter):
    pass


class CPPTToPDFParameter(CPDFFileParameter):
    pass


class CRTFToPDFParameter(CPDFFileParameter):
    pass


class CTxtToPDFParameter(CPDFFileParameter):
    pass


class CWordToPDFParameter(CPDFFileParameter):
    pass


class CPDFFileParameterFactory:
    """
    Factory class to create CPDFFileParameter object.
    """

    def get_file_parameter_by_type(self, type):
        CPDFFileParameter = None

        if type is CPDFConversionEnum:
            if type == CPDFConversionEnum.PDF_TO_EXCEL:
                CPDFFileParameter = CPDFToExcelParameter()
            elif type == CPDFConversionEnum.PDF_TO_HTML:
                CPDFFileParameter = CPDFToHtmlParameter()
            else:
                raise Exception(f"Unsupported type: {type}")
        elif type is CPDFDocumentAIEnum:
            pass
        elif type is CPDFDocumentEditorEnum:
            if type == CPDFDocumentEditorEnum.INSERT:
                CPDFFileParameter = CPDFPageInsertParameter()
            elif type == CPDFDocumentEditorEnum.SPLIT:
                CPDFFileParameter = CPDFPageSplitParameter()
            elif type == CPDFDocumentEditorEnum.MERGE:
                CPDFFileParameter = CPDFPageMergeParameter()
            elif type == CPDFDocumentEditorEnum.COMPRESS:
                CPDFFileParameter = CPDFCompressParameter()
            elif type == CPDFDocumentEditorEnum.DELETE:
                CPDFFileParameter = CPDFPageDeleteParameter()
            elif type == CPDFDocumentEditorEnum.EXTRACT:
                CPDFFileParameter = CPDFPageExtractParameter()
            elif type == CPDFDocumentEditorEnum.ROTATION:
                CPDFFileParameter = CPDFPageRotationParameter()
            elif type == CPDFDocumentEditorEnum.ADD_WATERMARK:
                CPDFFileParameter = CPDFAddWatermarkParameter()
            else:
                raise Exception(f"Unsupported type: {type}")

        return CPDFFileParameter
