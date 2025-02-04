from abc import ABC, abstractmethod


class TextStorage(ABC):
    @abstractmethod
    def insert(self, char: str):
        '''Insert a characer at the current cursor position'''
        pass

    @abstractmethod
    def delete(self):
        '''Delete the character before the cursor'''
        pass

    @abstractmethod
    def move_cursor(self, position: int):
        '''Move the cursor to a new position'''
        pass

    @abstractmethod
    def get_text(self) -> str:
        '''
        Return the text as a single string.

        Returns:
            str: The text in the text editor.
        '''
        pass

    @abstractmethod
    def get_length(self) -> int:
        '''Return the length of the text'''
