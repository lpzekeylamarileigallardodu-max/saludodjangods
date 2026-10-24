from saludos.domain.saludo import construir_saludo


class SaludarUseCase:
    def execute(self, nombre: str) -> str:
        return construir_saludo(nombre)