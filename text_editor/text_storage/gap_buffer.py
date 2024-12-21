from text_storage.text_storage import TextStorage


class GapBuffer(TextStorage):
    def __init__(self, initial_size=10):
        '''
        Initialize the hap buffer
        :param initial_size: The initial size of the buffer.
        '''
        self.buffer = [""] * initial_size
        self.gap_start = 0
        self.gap_end = initial_size

    def insert(self, char):
        '''
        Insert a character at the current gap position
        :param char: The character to insert.
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
        :param position: The new cursor position.
        '''
        if position < self.gap_start:
            # Move the gap left
            while self.gap_start > position:
                self.gap_start -= 1
                self.buffer[self.gap_end - 1] = self.buffer[self.gap_start]
                self.gap_end -= 1
        elif position > self.gap_start:
            # Move the gap right
            while self.gap_start < position:
                self.buffer[self.gap_start] = self.buffer[self.gap_end]
                self.gap_start += 1
                self.gap_end += 1

    def get_text(self):
        '''
        Return the current text as a single string.
        '''
        return "".join(self.buffer[:self.gap_start]
                       + self.buffer[self.gap_end:])

    def _expand_buffer(self):
        '''
        Expand the size of the bugger when the gap is full
        '''
        # Creates a new buffer that is twice the size of the previous buffer
        new_buffer = [""] * (len(self.buffer) * 2)
        # Copy elements from the current buffer, from before the gap,
        # to the new buffer
        new_buffer[:self.gap_end] = self.buffer[:self.gap_end]
        start_index = len(new_buffer) - (len(self.buffer) - self.gap_end)
        new_buffer[start_index:] = self.buffer[self.gap_end:]
        self.gap_end += len(new_buffer) - len(self.buffer)
        self.buffer = new_buffer
