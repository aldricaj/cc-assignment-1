from dataclasses import dataclass

@dataclass
class Document:
    document_id:str
    document_name:str
    document_path: str
    word_count: str

@dataclass
class User:
    username: str
    password_hash: str
    first: str
    last: str
    email: str
    user_id: str = ''
    documents: list = None