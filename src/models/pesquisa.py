class Pesquisa:
  def __init__(self, tipo_busca: str, quant_paginas: int, uf: str, orcamento_max: float, quant_vagas: int, quant_quartos: int, quant_banheiros: int):
    self.tipo_busca = tipo_busca
    self.quant_paginas = quant_paginas
    self.uf = uf
    self.orcamento_max = orcamento_max
    self.quant_vagas = quant_vagas
    self.quant_quartos = quant_quartos
    self.quant_banheiros = quant_banheiros