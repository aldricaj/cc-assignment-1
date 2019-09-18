import dataclass from dataclasses

@dataclass
class Document:
    document_id:str
    document_name:str
    document_path: str
    word_count: str

@dataclass
class User:
    user_id: str
    username: str
    password_hash: str
    first: str
    last: str
    email: str
    documents: list = []