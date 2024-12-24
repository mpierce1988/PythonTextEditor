# gap_buffer.py
from text_storage.text_storage import TextStorage


DEFAULT_INITIAL_SIZE = 10


class GapBuffer(TextStorage):
    '''A gap buffer implementation for text storage'''
    def __init__(self, initial_size=DEFAULT_INITIAL_SIZE):
        '''
        Initialize the gap buffer

        Args:
            initial_size (int): The initial size of the buffer.
        '''
        self.buffer = [""] * initial_size
        self.gap_start = 0
        self.gap_end = initial_size

    def get_text(self):
        '''
        Return the current text as a single string.
        '''
        return "".join(self.buffer[:self.gap_start]) + "".join(
            self.buffer[self.gap_end:])

    def get_length(self):
        '''
        Return the length of the text
        '''
        # return len(self.get_text())
        return len(self.buffer) - (self.gap_end - self.gap_start)

    def insert(self, char):
        '''
        Insert a character at the current gap position

        Args:
            char (str): The character to insert.
        '''
        if self.gap_start == self.gap_end:
            self._expand_buffer()
        self.buffer[self.gap_start] = char
        self.gap_start += 1

    def delete(self):
        '''
        Delete the character before the cursor
        '''
        if self.gap_start > 0:
            self.gap_start -= 1

    def move_cursor(self, position):
        '''
        Move the cursor to a new position, adjusting the gap.

        Args:
            position (int): The new cursor position.
        '''
        if position < self.gap_start:
            # Move the gap left
            self._move_cursor_left(position)
        elif position > self.gap_start:
            self._move_cursor_right(position)

    def _move_cursor_left(self, position):
        '''
        Move the cursor to the left, adjusting the gap.

        Args:
            position (int): The new cursor position.
        '''
        while position < self.gap_start:
            self.gap_start -= 1
            self.buffer[self.gap_end - 1] = self.buffer[self.gap_start]
            self.gap_end -= 1

    def _move_cursor_right(self, position):
        '''
        Move the cursor to the right, adjusting the gap.

        Args:
            position (int): The new cursor position.
        '''
        while position > self.gap_start:
            self.buffer[self.gap_start] = self.buffer[self.gap_end]
            self.gap_start += 1
            self.gap_end += 1

    def _expand_buffer(self):
        '''
        Expand the size of the buffer when the gap is full.
        Example:
            Original: [a][b][_][_][c][d]  ([] = cell, _ = gap)
            New:      [a][b][_][_][_][_][c][d]
        '''
        # Double the size of the buffer, filling with empty strings
        new_buffer = [""] * (len(self.buffer) * 2)

        # Copy content before gap to new buffer
        # e.g., [a][b] -> [a][b][_][_][_][_][_][_]
        new_buffer[:self.gap_end] = self.buffer[:self.gap_end]

        # Calculate where to place content that was after the gap
        # If original buffer was size 6 with gap_end=4,
        # and new buffer is size 12,
        # then after_gap_index would be 10 (12 - (6 - 4))
        gap_end_to_buffer_end_length = len(self.buffer) - self.gap_end
        after_gap_index = len(new_buffer) - gap_end_to_buffer_end_length

        # Copy content after gap to end of new buffer
        # e.g., [a][b][_][_][_][_][_][_] -> [a][b][_][_][_][_][c][d]
        new_buffer[after_gap_index:] = self.buffer[self.gap_end:]

        # Adjust gap_end to account for new buffer size
        buffer_size_increase = len(new_buffer) - len(self.buffer)
        self.gap_end += buffer_size_increase

        # Replace old buffer with new expanded buffer
        self.buffer = new_buffer
