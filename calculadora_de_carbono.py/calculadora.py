def calcular_emissoes(carbono_por_km, distancia):
    return carbono_por_km * distancia

def obter_dados_veiculo():
    tipo_carro = input("Digite o tipo de carro (compacto, SUV, Sedâ): ").strip().lower()
    tipo_combustivel = input("Digite o tipo de combustivel (gasolina, etanol, diesel)").strip().lower()
    distancia = float(input("Digite a distância percorrida (em km): "))

    if tipo_combustivel == "gasolina":
        carbono_por_km = 2.31  # Emissões em kg de CO2 por litro
    elif tipo_combustivel == "etanol":
        carbono_por_km = 1.60  # Emissões em kg de CO2 por litro
    elif tipo_combustivel == "diesel":
        carbono_por_km = 2.68  # Emissões em kg de CO2 por litro
    else:
        print("Tipo de combustível inválido!")
        return None, None

    return carbono_por_km, distancia

def main():
    print("Calculadora de Emissões de Carbono de Veículos")
    carbono_por_km, distancia = obter_dados_veiculo()

    if carbono_por_km is not None and distancia is not None:
        emissoes = calcular_emissoes(carbono_por_km, distancia)
        print(f"Emissões totais de CO2: {emissoes:.2f} kg")

if __name__ == "__main__":
    main()
