from unittest import TestCase
from unittest.mock import patch

from hexgen.draw import HexGridDraw


class TestHexGridDraw(TestCase):

    def test_uses_default_font_when_freesans_is_unavailable(self):
        original_truetype = HexGridDraw._load_font.__globals__['ImageFont'].truetype

        def unavailable_freesans(font, *args, **kwargs):
            if font == 'FreeSans.ttf':
                raise OSError
            return original_truetype(font, *args, **kwargs)

        with patch('hexgen.draw.ImageFont.truetype', side_effect=unavailable_freesans):
            font = HexGridDraw._load_font()

        self.assertIsNotNone(font)
