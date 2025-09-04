import json
import os
from controllers.logs import LogGerador
from models.cliente import Cliente

class ClienteJson:
  def __init__(self):
    self.path_clientes = os.path.join("data", "clientes.json")
    self.log = LogGerador()

  def carregar_json(self, path) -> dict:
    if not os.path.exists(path):
      return []
    try:
      with open(path, '+r', encoding='utf-8') as arquivo:
        return json.load(arquivo)
    except FileNotFoundError as erro:
      self.log.salvar_log(titulo="Arquivo", conteudo="Arquivo de 'Cliente' nao foi encontrado", erro=erro)
    except Exception as erro:
      self.log.salvar_log(titulo="Geral", conteudo="Erro durante a leitura do arquivo de 'Clientes'", erro=erro)
    
  def salvar_json(self, path, dados: dict) -> None:
    try:
      with open(path, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)
    except Exception as erro:
      self.log.salvar_log(titulo="Geral", conteudo="Erro durante a escrita do arquivo de 'Clientes'", erro=erro)
  
  def gerar_id(self, dados: dict):
    if not dados:
      return 1
    ultimo_id = max(dado.get("id_cliente") for dado in dados)
    return ultimo_id + 1
  
  def cliente_existe(self, cliente: Cliente, dados: dict) -> bool:
    clientes: list[Cliente] = self.listar_clientes()
    for c in clientes:
      if cliente.nome == c.nome and cliente.email == c.email and cliente.telefone == c.telefone:
        return True
    return False
  
  def buscar_cliente_id(self, id_cliente: int) -> Cliente:
    clientes: list[Cliente]= self.listar_clientes()
    for c in clientes:
      if c.id_cliente == id_cliente:
        return c
    return None

  def listar_clientes(self) -> list[Cliente]:
    dados = self.carregar_json(self.path_clientes)
    clientes: list[Cliente] = []
    for dado in dados:
      cliente = Cliente(
        id_cliente=dado.get("id_cliente"),
        nome=dado.get("nome"),
        email=dado.get("email"),
        telefone=dado.get("telefone"),
        tipo_imovel=dado.get("tipo_imovel"),
        tipo_aquisicao=dado.get("tipo_aquisicao"),
        cidade_desejada=dado.get("cidade_desejada"),
        uf_desejado=dado.get("uf_desejado"),
        orcamento=dado.get("orcamento"),
        pendente=dado.get("pendente")
      )
      clientes.append(cliente)
    return clientes

  def adicionar_cliente(self, cliente: Cliente) -> None:
    dados = self.carregar_json(self.path_clientes)
    if not self.cliente_existe(cliente=cliente, dados=dados):
      dados.append(
        {
          "id_cliente": self.gerar_id(dados=dados),
          "nome": cliente.nome.upper(),
          "email": cliente.email.upper(),
          "telefone": cliente.telefone.upper(),
          "tipo_imovel": cliente.tipo_imovel.upper(),
          "tipo_aquisicao": cliente.tipo_aquisicao.upper(),
          "cidade_desejado": cliente.cidade_desejada.upper(),
          "uf_desejado": cliente.uf_desejado.upper(),
          "orcamento": cliente.orcamento,
          "pendente": cliente.pendente,
        }
      )
      self.salvar_json(path=self.path_clientes,dados=dados)
    else:
      pass
  
  def excluir_cliente(self, id_cliente: int) -> bool:
    clientes: list[Cliente] = self.listar_clientes()
    novos_dados = []
    for cliente in clientes:
      if cliente.id_cliente != id_cliente:
        novos_dados.append({
          "id_cliente": cliente.id_cliente,
          "nome": cliente.nome.upper(),
          "email": cliente.email.upper(),
          "telefone": cliente.telefone.upper(),
          "tipo_imovel": cliente.tipo_imovel.upper(),
          "tipo_aquisicao": cliente.tipo_aquisicao.upper(),
          "cidade_desejado": cliente.cidade_desejada.upper(),
          "uf_desejado": cliente.uf_desejado.upper(),
          "orcamento": cliente.orcamento,
          "pendente": cliente.pendente,
        }
      )
      print("ENCONTRADO E PULANDO")
    self.salvar_json(path=self.path_clientes, dados=novos_dados)

if __name__ == "__main__":
  clienteJson = ClienteJson()
  cliente = Cliente(
    id_cliente=None,
    nome="teste",
    email="email",
    telefone="1212121212",
    tipo_imovel="APARTAMENTO",
    tipo_aquisicao="ALUGUEL",
    cidade_desejada=None,
    uf_desejado="SP",
    orcamento=900,
    pendente=False
    )
  clienteJson.adicionar_cliente(cliente=cliente)
  pass