# editor_logic.py
from text_storage.gap_buffer import GapBuffer


class EditorLogic:
    def __init__(self):
        self.text_storage = GapBuffer(initial_size=50)  # Text storage
        self.cursor_position = 0  # Current cursor position

    def insert_character(self, char):
        '''
        Insert a character into the text editor.
        :param char: The character to insert.
        '''

        self.text_storage.insert(char)
        self.cursor_position += 1

    def delete_character(self):
        '''
        Delete a character from the text editor.
        '''
        if self.cursor_position == 0:
            return

        self.text_storage.delete()
        self.cursor_position -= 1

    def delete_next_character(self):
        '''
        Deletes the next character in the text editor
        '''
        if self.cursor_position + 1 > self.text_storage.get_length():
            return

        self.move_right()
        self.delete_character()

    def move_left(self):
        '''
        Move the cursor to the left
        '''
        # Ensure the cursor position does not go below 0
        self.cursor_position = max(0, self.cursor_position - 1)
        self.text_storage.move_cursor(self.cursor_position)

    def move_right(self):
        '''
        Move the cursor to the right
        '''
        # Limit the cursor position to the length of the text
        self.cursor_position = min(self.text_storage.get_length(),
                                   self.cursor_position + 1)
        self.text_storage.move_cursor(self.cursor_position)

    def get_text(self):
        '''
        Return the current text in the text editor.
        :return: The current text as a string.
        '''
        return self.text_storage.get_text()
