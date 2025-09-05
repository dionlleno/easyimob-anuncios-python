import json
import os

from models.localidade import Localidade

class FiltrosJson:
  def __init__(self):
    self.path_filtro_estado_cidade = os.path.join("data", "estados_cidades.json")
  
  def carregar_json(self, path) -> dict:
    if not os.path.exists(path):
      return {}
    try:
      with open(path, 'r', encoding='utf-8') as arquivo:
        return json.load(arquivo)
    except FileNotFoundError as erro:
      print(f"Arquivo nao encontrado -> {path}")
      print(f"Erro: {erro}")
    
  def salvar_json(self, path, dados) -> None:
    try:
      with open(path, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, ensure_ascii=False, indent=2)
    except Exception as erro:
      print(dados)
      print(f"Erro ao salvar o arquivo -> {path}")
      print(f"Erro: {erro}")

  def adicionar_cidade(self, localidade: Localidade) -> None:
    dados = self.carregar_json(self.path_filtro_estado_cidade)
    for dado in dados:
      if dado.get("uf") == localidade.uf and dado.get("estado") == localidade.estado:
        novas_cidades: list[str] = dado.get("cidades", [])
        for cidade in localidade.cidades:
          if cidade not in novas_cidades:
            novas_cidades.append(cidade)
        novas_cidades.sort()
        dado["cidades"] = novas_cidades
        break
      self.salvar_json(path=self.path_filtro_estado_cidade, dados=dados)
    else:
      self.adicionar_estado(localidade)

  def adicionar_estado(self, localidade: Localidade) -> None:
    dados = self.carregar_json(path=self.path_filtro_estado_cidade)
    dados.append({
        "estado": localidade.estado,
        "uf": localidade.uf,
        "cidades": [localidade.cidades]
      })
    dados.sort(key=lambda x: x["estado"])
    self.salvar_json(path=self.path_filtro_estado_cidade, dados=dados)

  def listar_estados(self) -> list[str]:
    localidades = self.listar_localidades()
    estados = []
    for localidade in localidades:
      estados.append(localidade.uf)
    return estados

  def listar_cidades(self, uf: str) -> list[str]:
    localidades = self.listar_localidades()
    for localidade in localidades:
      if localidade.uf == uf:
        return localidade.cidades
    return []

  def listar_localidades(self) -> list[Localidade]:
    dados = self.carregar_json(self.path_filtro_estado_cidade)
    localidades: list[Localidade] = []
    for dado in dados:
      localidade = Localidade(
        estado=dado.get("estado"),
        uf=dado.get("uf"),
        cidades=dado.get("cidades", []))
      localidades.append(localidade)
    return localidades

if __name__ == "__main__":
  pass