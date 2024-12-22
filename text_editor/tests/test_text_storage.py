import pytest
from text_storage.gap_buffer import GapBuffer

@pytest.fixture
def gap_buffer():
    '''Fixture to create a new GapBuffer instance for each test'''
    return GapBuffer()

def test_insert(gap_buffer):
    '''Test inserting characters into the buffer'''
    gap_buffer.insert("a")
    gap_buffer.insert("b")
    gap_buffer.insert("c")
    assert gap_buffer.get_text() == "abc"

def test_delete(gap_buffer):
    '''Test deleting characters from the buffer'''
    gap_buffer.insert("a")
    gap_buffer.insert("b")
    gap_buffer.insert("c")
    gap_buffer.delete()
    assert gap_buffer.get_text() == "ab"

def test_get_length(gap_buffer):
    '''Test getting the length of the buffer'''
    gap_buffer.insert("a")
    gap_buffer.insert("b")
    gap_buffer.insert("c")
    assert gap_buffer.get_length() == 3

def test_move_cursor(gap_buffer):
    '''Test moving the cursor within the buffer'''
    gap_buffer.insert("a")
    gap_buffer.insert("b")
    gap_buffer.insert("c")
    gap_buffer.move_cursor(1)
    gap_buffer.insert("x")
    assert gap_buffer.get_text() == "axbc"

def test_move_cursor_left(gap_buffer):
    '''Test moving the cursor to the left within the buffer'''
    gap_buffer.insert("a")
    gap_buffer.insert("b")
    gap_buffer.insert("c")
    gap_buffer.move_cursor(1)
    assert gap_buffer.get_text() == "abc"

def test_move_cursor_right(gap_buffer):
    '''Test moving the cursor to the right within the buffer'''
    gap_buffer.insert("a")
    gap_buffer.insert("b")
    gap_buffer.insert("c")
    gap_buffer.move_cursor(1)
    gap_buffer.move_cursor(2)
    assert gap_buffer.get_text() == "abc"

def test_expand_buffer(gap_buffer):
    '''Test expanding the buffer when the gap is full'''
    for i in range(15):
        gap_buffer.insert("a")
    assert len(gap_buffer.buffer) == 20
    assert gap_buffer.get_text() == "a" * 15