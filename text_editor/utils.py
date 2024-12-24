# Description: Utility functions for the text editor GUI

def get_max_chars_per_line(char_width: int, canvas_width: int) -> int:
    '''
    Return the maximum number of characters per line.

    Args:
        char_width (int): The width of a single character.
        canvas_width (int): The width of the canvas.
    '''
    padding = 5
    return (canvas_width // char_width) - padding


def split_text_into_lines(text: str, max_chars_per_line: int) -> list[str]:
    '''
    Split the text into lines of a maximum length.

    Args:
        text (str): The text to split.
        max_chars_per_line (int): The maximum number of characters per line.
    '''

    lines = []

    if not text or text == "":
        return lines

    current_line = ""

    for char in text:
        current_line += char
        if len(current_line) >= max_chars_per_line or char == "\n":
            lines.append(current_line)
            current_line = ""

    lines.append(current_line)

    return lines


def get_cursor_position(lines: list[str],
                        cursor_offset: int) -> tuple[int, int]:
    '''
    Get the cursor position on the canvas.

    Args:
        lines (list[str]): The lines of text on the canvas.
        cursor_offset (int): The cursor offset within the text.
    '''

    if not lines:
        return 0, 0

    # If the last line is an empty string,
    # set the cursor position to the last line

    if lines[-1] == "":
        cursor_line = len(lines) - 1
        cursor_offset = 0
        return cursor_line, cursor_offset

    cursor_line = 0

    for line in lines:
        if cursor_offset > len(line):
            cursor_offset -= len(line)
            cursor_line += 1
        else:
            break

    return cursor_line, cursor_offset
