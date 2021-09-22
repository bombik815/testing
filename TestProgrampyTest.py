import pytest
from TEST.program import add_new_doc, delete_doc, show_all_docs_info


def test_show_all_docs_info():
    documents = [
        {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
        {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
        {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
    ]
    assert documents == show_all_docs_info()


def test_add_new_doc():
    assert add_new_doc('passport','999','Сидоров', '123')

def test_delete_doc():
    assert delete_doc('10006')

