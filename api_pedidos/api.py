from typing import List
from fastapi import FastAPI, Depends
from uuid import UUID
from api_pedidos.esquema import Item
from api_pedidos.excecao import PedidoNaoEncontradoError, FalhaDeComunicacaoError
from fastapi import FastAPI, Depends, Request
from fastapi.responses import JSONResponse
from http import HTTPStatus


app = FastAPI()


def recuperar_itens_por_pedido(identificacao_do_pedido: UUID) -> List[Item]:
    pass


@app.exception_handler(FalhaDeComunicacaoError)
def tratar_erro_falha_de_comunicacao(request: Request, exc: FalhaDeComunicacaoError):
    return JSONResponse(status_code=HTTPStatus.BAD_GATEWAY, content={"message": "Falha de comunicação com o servidor remoto"})


@app.exception_handler(PedidoNaoEncontradoError)
def tratar_erro_pedido_nao_encontrado(request: Request, exc: PedidoNaoEncontradoError):
    return JSONResponse(status_code=HTTPStatus.NOT_FOUND, content={"message": "Pedido não encontrado"})


@app.get("/healthcheck")
async def healthcheck():
    return {"status": "ok"}


@app.get("/orders/{identificacao_do_pedido}/items")
def listar_itens(itens: List[Item] = Depends(recuperar_itens_por_pedido)):
    return itens
