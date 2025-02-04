import pytest
from text_editor.editor_logic import EditorLogic
from text_storage.gap_buffer import GapBuffer

@pytest.fixture
def editor():
    text_storage = GapBuffer(initial_size=50)
    return EditorLogic(text_storage)

def test_insert_character(editor):
    editor.insert_character('a')
    assert editor.get_text() == 'a'
    assert editor.cursor_position == 1

def test_delete_character(editor):
    editor.insert_character('a')
    editor.insert_character('b')
    editor.delete_character()
    assert editor.get_text() == 'a'
    assert editor.cursor_position == 1

def test_delete_next_character(editor):
    editor.insert_character('a')
    editor.insert_character('b')
    editor.insert_character('c')
    editor.move_left()
    editor.move_left()
    editor.delete_next_character()
    assert editor.get_text() == 'ac'
    assert editor.cursor_position == 1

def test_move_left(editor):
    editor.insert_character('a')
    editor.insert_character('b')
    editor.insert_character('c')
    editor.move_left()
    assert editor.get_text() == 'abc'
    assert editor.cursor_position == 2

def test_move_left_delete_cursor_position(editor):
    editor.insert_character('a')
    editor.move_left()
    editor.delete_character()
    assert editor.cursor_position == 0
    assert editor.get_text() == 'a'

def test_move_right(editor):
    editor.insert_character('a')
    editor.insert_character('b')
    editor.move_left()
    editor.move_right()
    assert editor.cursor_position == 2 

def test_get_text(editor):
    editor.insert_character('a')
    editor.insert_character('b')
    assert editor.get_text() == 'ab'

def test_move_cursor_within_bounds(editor):
    editor.insert_character('a')
    editor.insert_character('b')
    editor.insert_character('c')
    editor.move_cursor(1)
    assert editor.cursor_position == 1

def test_move_cursor_out_of_bounds(editor):
    editor.insert_character('a')
    editor.insert_character('b')
    editor.insert_character('c')
    editor.move_cursor(5)
    assert editor.cursor_position == 3  # Should be at the end of the text

def test_move_cursor_to_start(editor):
    editor.insert_character('a')
    editor.insert_character('b')
    editor.insert_character('c')
    editor.move_cursor(0)
    assert editor.cursor_position == 0

def test_move_cursor_negative_position(editor):
    editor.insert_character('a')
    editor.insert_character('b')
    editor.insert_character('c')
    editor.move_cursor(-1)
    assert editor.cursor_position == 0  # Should be at the start of the text
