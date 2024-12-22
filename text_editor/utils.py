# Description: Utility functions for the text editor GUI

def get_max_chars_per_line(char_width: int, canvas_width: int) -> int:
    '''
    Return the maximum number of characters per line.
    '''
    return canvas_width // char_width - 5


def split_text_into_lines(text: str, max_chars_per_line: int) -> list[str]:
    '''
    Split the text into lines of a maximum length.
    :param text: The text to split.
    :param max_chars_per_line: The maximum number of characters per line.
    '''

    lines = []
    current_line = ""

    for char in text:
        current_line += char
        if len(current_line) >= max_chars_per_line or char == "\n":
            lines.append(current_line)
            current_line = ""

    if current_line:
        lines.append(current_line)

    return lines


def get_cursor_position(lines: list[str],
                        cursor_offset: int) -> tuple[int, int]:
    '''
    Get the cursor position on the canvas.
    :param lines: The lines of text.
    :param cursor_offset: The cursor offset in the text.
    '''

    cursor_line = 0

    for line in lines:
        if cursor_offset > len(line):
            cursor_offset -= len(line)
            cursor_line += 1
        else:
            break

    return cursor_line, cursor_offset
