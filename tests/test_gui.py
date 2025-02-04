import tkinter as tk
import pytest
from unittest.mock import MagicMock
from text_editor.gui import TextEditorGUI
from text_storage.gap_buffer import GapBuffer

@pytest.fixture
def setup_gui():
    root = tk.Tk()
    text_storage = GapBuffer(initial_size=50)
    gui = TextEditorGUI(root, text_storage)
    gui.editor_logic = MagicMock()
    yield gui
    root.destroy()

def test_on_key_press_inserts_character(setup_gui):
    event = type("DummyEvent", (), {"char": "a", "keysym" : "a"})()
    setup_gui.on_key_press(event)
    setup_gui.editor_logic.insert_character.assert_called_with("a")

def test_on_key_press_handles_return(setup_gui):
    event = type("DummyEvent", (), {"char": "\r", "keysym": "Return"})()
    setup_gui.on_key_press(event)
    setup_gui.editor_logic.insert_character.assert_called_with("\r")