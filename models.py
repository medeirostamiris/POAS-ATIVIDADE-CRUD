from typing import Optional
from sqlmodel import SQLModel, Field
from datetime import datetime


class Usuario(SQLModel, table=True):
    __tablename__ = "usuarios"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    email: str = Field(unique=True)
    senha_hash: str
    criado_em: Optional[datetime] = Field(default_factory=datetime.utcnow)


class Papel(SQLModel, table=True):
    __tablename__ = "papeis"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str = Field(unique=True)


class Produto(SQLModel, table=True):
    __tablename__ = "produtos"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str
    descricao: str
    preco: float
    criado_em: datetime = Field(default_factory=datetime.now)


class Categoria(SQLModel, table=True):
    __tablename__ = "categorias"

    id: Optional[int] = Field(default=None, primary_key=True)
    nome: str


class Pedido(SQLModel, table=True):
    __tablename__ = "pedidos"

    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id")
    total: float
    status: str
    criado_em: datetime = Field(default_factory=datetime.now)


class Pagamento(SQLModel, table=True):
    __tablename__ = "pagamentos"

    id: Optional[int] = Field(default=None, primary_key=True)
    pedido_id: int = Field(foreign_key="pedidos.id")
    valor: float
    metodo: str
    status: str
    pago_em: Optional[datetime] = None


class Endereco(SQLModel, table=True):
    __tablename__ = "enderecos"

    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id")
    rua: str
    cidade: str
    estado: str
    cep: str


class Avaliacao(SQLModel, table=True):
    __tablename__ = "avaliacoes"

    id: Optional[int] = Field(default=None, primary_key=True)
    usuario_id: int = Field(foreign_key="usuarios.id")
    produto_id: int = Field(foreign_key="produtos.id")
    nota: int
    comentario: str
    criado_em: datetime = Field(default_factory=datetime.now)


class Estoque(SQLModel, table=True):
    __tablename__ = "estoque"

    id: Optional[int] = Field(default=None, primary_key=True)
    produto_id: int = Field(foreign_key="produtos.id", unique=True)
    quantidade: int
    atualizado_em: datetime = Field(default_factory=datetime.now)