def calcular_ir(renda_mensal):
    faixa = None
    desconto = 0
    aliquota = 0
    ir = 0
    status = "Válido"

    if renda_mensal < 0:
        status = "Inválido"
        return {
            "renda_mensal": renda_mensal,
            "faixa": faixa,
            "desconto": desconto,
            "aliquota": aliquota,
            "ir_mensal": ir,
            "status": status
        }

    elif renda_mensal <= 5000:
        faixa = "Até R$ 5.000"
        desconto = 100
        aliquota = 0.275
        ir = 0

    elif renda_mensal <= 5500:
        faixa = "Até R$ 5.500"
        desconto = 75
        aliquota = 0.275
        ir_bruto = renda_mensal * aliquota
        ir = ir_bruto * (1 - desconto / 100)

    elif renda_mensal <= 6000:
        faixa = "Até R$ 6.000"
        desconto = 50
        aliquota = 0.275
        ir_bruto = renda_mensal * aliquota
        ir = ir_bruto * (1 - desconto / 100)

    elif renda_mensal <= 6500:
        faixa = "Até R$ 6.500"
        desconto = 25
        aliquota = 0.275
        ir_bruto = renda_mensal * aliquota
        ir = ir_bruto * (1 - desconto / 100)

    elif renda_mensal <= 7350:
        faixa = "Até R$ 7.350"
        desconto = 10
        aliquota = 0.275
        ir_bruto = renda_mensal * aliquota
        ir = ir_bruto * (1 - desconto / 100)

    else:
        faixa = "Acima de R$ 7.350"
        aliquota = 0.275
        ir = renda_mensal * aliquota

    return {
        "renda_mensal": renda_mensal,
        "faixa": faixa,
        "desconto": desconto,
        "aliquota": aliquota,
        "ir_mensal": ir,
        "status": status
    }

if __name__ == "__main__":
    print(calcular_ir(float(input("Digite a renda mensal: "))))
