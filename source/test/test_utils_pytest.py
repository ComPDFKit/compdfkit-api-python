from compdfkit.utils import ParameterValidator


def test_validate_color():
    """
    Test validate_color method.
    """
    assert ParameterValidator.validate_color('#000000') == '#000000'
    assert ParameterValidator.validate_color('#ffffff') == '#ffffff'
    assert ParameterValidator.validate_color('#123456') == '#123456'
    assert ParameterValidator.validate_color('#ABCDEF') == '#ABCDEF'
    assert ParameterValidator.validate_color('#abcdef') == '#abcdef'
    assert ParameterValidator.validate_color('#AbCdEf') == '#AbCdEf'
    assert ParameterValidator.validate_color('#123abc') == '#123abc'
    assert ParameterValidator.validate_color('#123abC') == '#123abC'
    assert ParameterValidator.validate_color('#123Abc') == '#123Abc'
    assert ParameterValidator.validate_color('#123aBc') == '#123aBc'


def test_validate_color_error():
    """
    Test validate_color method with invalid color.
    """
    try:
        ParameterValidator.validate_color('000000')
    except ValueError as e:
        assert str(e) == 'color should be in hex format'
    else:
        assert False

    try:
        ParameterValidator.validate_color('#00000')
    except ValueError as e:
        assert str(e) == 'color should be in hex format'
    else:
        assert False

    try:
        ParameterValidator.validate_color('#0000000')
    except ValueError as e:
        assert str(e) == 'color should be in hex format'
    else:
        assert False

    try:
        ParameterValidator.validate_color('#00000g')
    except ValueError as e:
        assert str(e) == 'color should be in hex format'
    else:
        assert False

    try:
        ParameterValidator.validate_color('#00000G')
    except ValueError as e:
        assert str(e) == 'color should be in hex format'
    else:
        assert False

    try:
        ParameterValidator.validate_color('#00000/')
    except ValueError as e:
        assert str(e) == 'color should be in hex format'
    else:
        assert False

    try:
        ParameterValidator.validate_color('#00000\\')
    except ValueError as e:
        assert str(e) == 'color should be in hex format'
    else:
        assert False


def test_validate_page():
    """
    Test validate_page method.
    """
    assert ParameterValidator.validate_pages('1') == '1'
    assert ParameterValidator.validate_pages('1,2,3') == '1,2,3'
    assert ParameterValidator.validate_pages('1-3,4,5') == '1-3,4,5'
    assert ParameterValidator.validate_pages('1,2,3,4,5') == '1,2,3,4,5'
    assert ParameterValidator.validate_pages('1-3,4,5,6-8') == '1-3,4,5,6-8'
    assert ParameterValidator.validate_pages('10-29') == '10-29'


def test_validate_page_error():
    """
    Test validate_page method with invalid pages.
    """
    try:
        ParameterValidator.validate_pages('1,2,3,4,5,')
    except ValueError as e:
        assert str(e) == 'pages should be in format like 1,2,3 or 1-3,4,5'
    else:
        assert False

    try:
        ParameterValidator.validate_pages('1-3,4,5,6-8,')
    except ValueError as e:
        assert str(e) == 'pages should be in format like 1,2,3 or 1-3,4,5'
    else:
        assert False

    try:
        ParameterValidator.validate_pages('1-3,c,5,a,9')
    except ValueError as e:
        assert str(e) == 'pages should be in format like 1,2,3 or 1-3,4,5'
    else:
        assert False

    try:
        ParameterValidator.validate_pages('1+3,4,5,6-s8,9,')
    except ValueError as e:
        assert str(e) == 'pages should be in format like 1,2,3 or 1-3,4,5'
    else:
        assert False


