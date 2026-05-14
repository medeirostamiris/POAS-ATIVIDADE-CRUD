from sqlmodel import Session, select

# CRUD GENÉRICO

def criar(session: Session, objeto):
    session.add(objeto)
    session.commit()
    session.refresh(objeto)
    return objeto


def listar(session: Session, model):
    return session.exec(select(model)).all()


def buscar_por_id(session: Session, model, id: int):
    return session.get(model, id)


def atualizar(session: Session, model, id: int, dados: dict):
    objeto = session.get(model, id)

    if not objeto:
        return None

    for chave, valor in dados.items():
        setattr(objeto, chave, valor)

    session.add(objeto)
    session.commit()
    session.refresh(objeto)

    return objeto


def deletar(session: Session, model, id: int):
    objeto = session.get(model, id)

    if not objeto:
        return None

    session.delete(objeto)
    session.commit()

    return {"mensagem": "Deletado com sucesso"}