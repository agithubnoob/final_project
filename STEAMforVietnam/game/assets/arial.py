import functools

from pygame.font import Font

FONT_PATH = ASSET_DIR / "fonts" / "arial.ttf"


@functools.lru_cache(maxsize=None)
def get_font(font_size):
    """
    Font loading is slow, but PyGame doesn't let you load a font without specifying a font size,
    so we cache the loaded ones to improve performance.
    If you get some error around here, that is probably due to using an older Python version.
    In that case, remove the decorator line `@functools.lru_cache(maxsize=None)` and try again.
    """
    return Font(FONT_PATH, font_size)
