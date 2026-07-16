from dataclasses import dataclass, field
import uuid

@dataclass
class ADM:
    nome: str
    login: str
    senha_hash: str
    papel: str

    status: str = "ativo"
    id: str = field(default_factory=lambda: str(uuid.uuid4()))

def oi():
    print("Oi")