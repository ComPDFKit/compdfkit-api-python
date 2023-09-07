"""
A module for tools used in the ComPDFKit API Libraries.

Dependencies:
    re: Handle regular expressions.
"""
import re


class ParameterValidator:
    """
    ParameterValidator class

    This class defines parameter validation methods.
    """

    @staticmethod
    def validate_color(color):
        """
        Validate color string in hex format.
        :param color: color string
        """
        if not isinstance(color, str):
            raise TypeError("color should be string")
        if not re.fullmatch(r'^#[0-9a-fA-F]{6}$', color):
            raise ValueError("color should be in hex format")
        return color

    @staticmethod
    def validate_pages(pages):
        """
        Validate pages string in format like 1,2,3 or 1-3,4,5.
        :param pages: pages string.
        """
        if not isinstance(pages, str):
            raise TypeError("pages should be string")
        if not re.fullmatch(r'\d+(?:-\d+)?(?:,\d+(?:-\d+)?)*', pages):
            raise ValueError("pages should be in format like 1,2,3 or 1-3,4,5")
        return pages
