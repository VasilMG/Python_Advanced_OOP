from wild_zoo.project import Category
from wild_zoo.project import Topic
from wild_zoo.project import Document
class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category:Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic:Topic):
        if topic not in self.topics:
            self.topics.append(topic)
    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name:str):
        for c in self.categories:
            if c.id == category_id:
                c.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        for t in self.topics:
            if t.id == topic_id:
                t.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        for d in self.documents:
            if d.id == document_id:
                d.edit(new_file_name)

    def delete_category(self, category_id):
        for c in self.categories:
            if c.id == category_id:
                self.categories.remove(c)

    def delete_topic(self, topic_id):
        for t  in self.topics:
            if t.id == topic_id:
                self.topics.remove(t)

    def delete_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                self.documents.remove(d)

    def get_document(self, document_id):
        for d in self.documents:
            if d.id == document_id:
                return repr(d)

    def __repr__(self):
        return '\n'.join([repr(x) for x in self.documents])
