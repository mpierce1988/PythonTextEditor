from abc import ABC, abstractmethod


class TextStorage(ABC):
    @abstractmethod
    def insert(self, char):
        '''Insert a characer at the current cursor position'''
        pass

    @abstractmethod
    def delete(self):
        '''Delete the character before the cursor'''
        pass

    @abstractmethod
    def move_cursor(self, position):
        '''Move the cursor to a new position'''
        pass

    @abstractmethod
    def get_text(self):
        '''Return the text as a single string.'''
        pass

    @abstractmethod
    def get_length(self):
        '''Return the length of the text'''
