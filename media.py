def calcular_media(nota1, nota2, nota3):
    for nota in (nota1, nota2, nota3):
        if not isinstance(nota, (int, float)):
            raise ValueError("Todas as notas devem ser numéricas.")
        if nota < 0:
            raise ValueError("As notas não podem ser negativas.")
    return (nota1 + nota2 + nota3) / 3
