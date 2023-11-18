import json

from PyQt5.QtWidgets import (QApplicatition, QWidget, QPushButton, QLabel, QListWidget, QLineEdit, QTextEdit, QInputDialog, QHBoxLayout)

app = QApplicatition([])
'''Інтерфейс програми'''
notes_win = QWidget()
notes_win.setWindowTittle('"Розумні замітки"')
notes_win.resize(900, 600)

list_notes = QListWitget()
list_notes_label = QLabel('Cписок заміток')
button_notes_del = QPushButton('Видалити замітку')
button_notes_create = QPushButton('Створити замiтку')
button_notes_save = QPushButton('Зберегти замітку')

frield_tag = (
    QlineEdit(''))
frield_tag.setPlaceholdertext('введiть тег...')
frield_text
notes_win.show()
app.exes_()




def add_note():
    note_name, ok =QInputDialog.getText(notes_win, "Додати замітку", "Назва замітки")
    if ok and note_name != "":
        notes[note_name] = {"Текст": "", "теги": []}
        list_notes.addItem(note_name)
        list_tags.addItems(notes[note_name]["теги"])
        print(notes)
button_note_save.clicked.connect(add_note)
def show_note():
    key = list_notes.selectedItems()[0].text()
    print(key)
    field_text.setText(notes[key]["текст"])
    list_tags.clear()
   list_tags.addItems(notes[key]["теги"])
list_notes.itemClicked.connect(show_note)
def safe_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
    notes[key]["текст"] = field_text.toPlainText()
    with open("notes_data.json", "w") as file:
        json.dump(notes, file, sort_keys=True, ensure_ascii=False)
    print(notes)
else:
    print("Замітка для збереження не вибрана!")
button_note_save.clicked.connect(safe_note)
def del_note():
    if list_notes.selectedItems():
        key = list_notes.selectedItems()[0].text()
        del notes[key]
        list_notes.clear()
        list_tags.clear()
        field_text.clear()
        list_notes.addItems(notes)
        with open("notes_data.json", "w") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False)
        print(notes)
    else:
        print("Замітка для збереження не вибрана!")
button_note_save.clicked.connect(del_note)





notes_win.show()
with open("notes_data.json", "r") as file:
    notes = json.load(file)
list_notes.addItems(notes)


app.exes_()

