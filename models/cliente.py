class Cliente:
  def __init__(self, nome: str, email: str, telefone: str, tipo_imovel: str, tipo_aquisicao: str, cidade_desejada: str, uf_desejado: str, orcamento: float, pendente: bool = False, id_cliente: int = None, ):
    self.id_cliente = id_cliente
    self.nome = nome
    self.email = email
    self.telefone = telefone
    self.tipo_imovel = tipo_imovel
    self.tipo_aquisicao = tipo_aquisicao
    self.cidade_desejada = cidade_desejada
    self.uf_desejado = uf_desejado
    self.orcamento = orcamento
    self.pendente = pendente
  
  def to_dict(self):
    return {
      "id_cliente": self.id_cliente,
      "nome": self.nome,
      "email": self.email,
      "telefone": self.telefone,
      "tipo_imovel": self.tipo_imovel,
      "tipo_aquisicao": self.tipo_aquisicao,
      "cidade_desejada": self.cidade_desejada,
      "uf_desejado": self.uf_desejado,
      "orcamento": self.orcamento,
      "pendente": self.pendente
    }
  
  def __str__(self):
    return f"Cliente(id_cliente={self.id_cliente}, nome={self.nome}, email={self.email}, telefone={self.telefone}, tipo_imovel={self.tipo_imovel}, tipo_aquisicao={self.tipo_aquisicao}, cidade_desejada={self.cidade_desejada}, uf_desejado={self.uf_desejado}, orcamento={self.orcamento}, pendente={self.pendente})"