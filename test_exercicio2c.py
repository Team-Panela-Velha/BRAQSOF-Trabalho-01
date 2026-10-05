import pytest
from exercicio2c import calcular_ir

@pytest.mark.parametrize(
    "renda, faixa_esperada, desconto_esperado, ir_esperado",
    [
        # Faixa 1 ->   R <= 5000 (ir fixo em 0)
        (3000, "Até R$ 5.000", 100, 0),
        (5000, "Até R$ 5.000", 100, 0),
        
        # Faixa 2 ->   R <= 5500
        (5200, "Até R$ 5.500", 75, (5200 * 0.275) * (1 - 75 / 100)),
        
        # Faixa 3 ->   R <= 6000
        (5800, "Até R$ 6.000", 50, (5800 * 0.275) * (1 - 50 / 100)),
        
        # Faixa 4 ->   R <= 6500
        (6200, "Até R$ 6.500", 25, (6200 * 0.275) * (1 - 25 / 100)),
        
        # Faixa 5 ->   R <= 7350
        (7000, "Até R$ 7.350", 10, (7000 * 0.275) * (1 - 10 / 100)),
        
        # Faixa 6 ->   Else (R > 7350)
        (8000, "Acima de R$ 7.350", 0, 8000 * 0.275),
    ],
)

def teste_calcular_ir_faixas(
    renda, faixa_esperada, desconto_esperado, ir_esperado
):
  
  "Testa o cálculo correto para cada faixa de renda estabelecida."
  resultado = calcular_ir(renda)

  # Verificando se os campos do dicionário retornado batem com o esperado
  assert resultado["renda_mensal"] == renda
  assert resultado["faixa"] == faixa_esperada
  assert resultado["desconto"] == desconto_esperado
  assert resultado["aliquota"] == 0.275

  # Usamos pytest.approx para lidar com pequenas imprecisões de ponto flutuante
  assert resultado["ir_mensal"] == pytest.approx(ir_esperado, rel=1e-5)
