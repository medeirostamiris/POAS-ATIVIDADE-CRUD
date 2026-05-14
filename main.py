from fastapi import FastAPI, Depends
from sqlmodel import Session

from database import get_session
from models import (
    Usuario,
    Papel,
    Produto,
    Categoria,
    Pedido,
    Pagamento,
    Endereco,
    Avaliacao,
    Estoque
)

from crud import (
    criar,
    listar,
    buscar_por_id,
    atualizar,
    deletar
)

app = FastAPI()

# =========================
# USUARIOS
# =========================

@app.post("/usuarios")
def criar_usuario(usuario: Usuario, session: Session = Depends(get_session)):
    return criar(session, usuario)


@app.get("/usuarios")
def listar_usuarios(session: Session = Depends(get_session)):
    return listar(session, Usuario)


@app.get("/usuarios/{id}")
def buscar_usuario(id: int, session: Session = Depends(get_session)):
    return buscar_por_id(session, Usuario, id)


@app.put("/usuarios/{id}")
def atualizar_usuario(
    id: int,
    usuario: Usuario,
    session: Session = Depends(get_session)
):
    return atualizar(session, Usuario, id, usuario.dict(exclude_unset=True))


@app.delete("/usuarios/{id}")
def deletar_usuario(id: int, session: Session = Depends(get_session)):
    return deletar(session, Usuario, id)


# =========================
# PAPEIS
# =========================

@app.post("/papeis")
def criar_papel(papel: Papel, session: Session = Depends(get_session)):
    return criar(session, papel)


@app.get("/papeis")
def listar_papeis(session: Session = Depends(get_session)):
    return listar(session, Papel)


@app.put("/papeis/{id}")
def atualizar_papel(
    id: int,
    papel: Papel,
    session: Session = Depends(get_session)
):
    return atualizar(session, Papel, id, papel.dict(exclude_unset=True))


@app.delete("/papeis/{id}")
def deletar_papel(id: int, session: Session = Depends(get_session)):
    return deletar(session, Papel, id)


# =========================
# PRODUTOS
# =========================

@app.post("/produtos")
def criar_produto(produto: Produto, session: Session = Depends(get_session)):
    return criar(session, produto)


@app.get("/produtos")
def listar_produtos(session: Session = Depends(get_session)):
    return listar(session, Produto)


@app.put("/produtos/{id}")
def atualizar_produto(
    id: int,
    produto: Produto,
    session: Session = Depends(get_session)
):
    return atualizar(session, Produto, id, produto.dict(exclude_unset=True))


@app.delete("/produtos/{id}")
def deletar_produto(id: int, session: Session = Depends(get_session)):
    return deletar(session, Produto, id)


# =========================
# CATEGORIAS
# =========================

@app.post("/categorias")
def criar_categoria(categoria: Categoria, session: Session = Depends(get_session)):
    return criar(session, categoria)


@app.get("/categorias")
def listar_categorias(session: Session = Depends(get_session)):
    return listar(session, Categoria)


@app.put("/categorias/{id}")
def atualizar_categoria(
    id: int,
    categoria: Categoria,
    session: Session = Depends(get_session)
):
    return atualizar(session, Categoria, id, categoria.dict(exclude_unset=True))


@app.delete("/categorias/{id}")
def deletar_categoria(id: int, session: Session = Depends(get_session)):
    return deletar(session, Categoria, id)


# =========================
# PEDIDOS
# =========================

@app.post("/pedidos")
def criar_pedido(pedido: Pedido, session: Session = Depends(get_session)):
    return criar(session, pedido)


@app.get("/pedidos")
def listar_pedidos(session: Session = Depends(get_session)):
    return listar(session, Pedido)


@app.put("/pedidos/{id}")
def atualizar_pedido(
    id: int,
    pedido: Pedido,
    session: Session = Depends(get_session)
):
    return atualizar(session, Pedido, id, pedido.dict(exclude_unset=True))


@app.delete("/pedidos/{id}")
def deletar_pedido(id: int, session: Session = Depends(get_session)):
    return deletar(session, Pedido, id)


# =========================
# PAGAMENTOS
# =========================

@app.post("/pagamentos")
def criar_pagamento(pagamento: Pagamento, session: Session = Depends(get_session)):
    return criar(session, pagamento)


@app.get("/pagamentos")
def listar_pagamentos(session: Session = Depends(get_session)):
    return listar(session, Pagamento)


@app.put("/pagamentos/{id}")
def atualizar_pagamento(
    id: int,
    pagamento: Pagamento,
    session: Session = Depends(get_session)
):
    return atualizar(session, Pagamento, id, pagamento.dict(exclude_unset=True))


@app.delete("/pagamentos/{id}")
def deletar_pagamento(id: int, session: Session = Depends(get_session)):
    return deletar(session, Pagamento, id)


# =========================
# ENDERECOS
# =========================

@app.post("/enderecos")
def criar_endereco(endereco: Endereco, session: Session = Depends(get_session)):
    return criar(session, endereco)


@app.get("/enderecos")
def listar_enderecos(session: Session = Depends(get_session)):
    return listar(session, Endereco)


@app.put("/enderecos/{id}")
def atualizar_endereco(
    id: int,
    endereco: Endereco,
    session: Session = Depends(get_session)
):
    return atualizar(session, Endereco, id, endereco.dict(exclude_unset=True))


@app.delete("/enderecos/{id}")
def deletar_endereco(id: int, session: Session = Depends(get_session)):
    return deletar(session, Endereco, id)


# =========================
# AVALIACOES
# =========================

@app.post("/avaliacoes")
def criar_avaliacao(avaliacao: Avaliacao, session: Session = Depends(get_session)):
    return criar(session, avaliacao)


@app.get("/avaliacoes")
def listar_avaliacoes(session: Session = Depends(get_session)):
    return listar(session, Avaliacao)


@app.put("/avaliacoes/{id}")
def atualizar_avaliacao(
    id: int,
    avaliacao: Avaliacao,
    session: Session = Depends(get_session)
):
    return atualizar(session, Avaliacao, id, avaliacao.dict(exclude_unset=True))


@app.delete("/avaliacoes/{id}")
def deletar_avaliacao(id: int, session: Session = Depends(get_session)):
    return deletar(session, Avaliacao, id)


# =========================
# ESTOQUE
# =========================

@app.post("/estoque")
def criar_estoque(estoque: Estoque, session: Session = Depends(get_session)):
    return criar(session, estoque)


@app.get("/estoque")
def listar_estoque(session: Session = Depends(get_session)):
    return listar(session, Estoque)


@app.put("/estoque/{id}")
def atualizar_estoque(
    id: int,
    estoque: Estoque,
    session: Session = Depends(get_session)
):
    return atualizar(session, Estoque, id, estoque.dict(exclude_unset=True))


@app.delete("/estoque/{id}")
def deletar_estoque(id: int, session: Session = Depends(get_session)):
    return deletar(session, Estoque, id)