# editor_logic.py
from text_storage.text_storage import TextStorage


class EditorLogic:
    # Constructor
    def __init__(self, text_storage: TextStorage):
        self.text_storage = text_storage  # Text storage
        self.cursor_position = 0  # Current cursor position

    # Public Methods
    def insert_character(self, char: str):
        '''
        Insert a character into the text editor.

        Args:
            char (str): The character to insert.
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
        self.cursor_position = self._get_bounded_position(
            self.cursor_position - 1)
        self.text_storage.move_cursor(self.cursor_position)

    def move_right(self):
        '''
        Move the cursor to the right
        '''
        # Limit the cursor position to the length of the text
        self.cursor_position = self._get_bounded_position(
            self.cursor_position + 1)
        self.text_storage.move_cursor(self.cursor_position)

    def move_cursor(self, position: int):
        '''
        Move the cursor to a specific position in the text editor.

        Args:
            position (int): The new cursor position.
        '''

        self.cursor_position = self._get_bounded_position(position)
        self.text_storage.move_cursor(self.cursor_position)

    def get_text(self) -> str:
        '''
        Return the current text in the text editor.

        Returns:
            str: The text in the text editor.
        '''
        return self.text_storage.get_text()

    # Protected Methods
    def _get_bounded_position(self, position: int) -> int:
        '''
        Ensure the cursor position is within bounds.

        Args:
            position (int): The cursor position.
        Returns:
            int: The bounded cursor position.
        '''

        # Ensure the cursor position is within bounds
        position = max(0, position)
        position = min(self.text_storage.get_length(), position)
        return position
