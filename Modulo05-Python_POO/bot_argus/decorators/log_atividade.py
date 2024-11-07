import functools
import datetime

def log_atividade(func):
    """Decorator para registrar atividades de métodos da classe GestorDePedidos."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        resultado = func(*args, **kwargs)
        with open("logs/log_atividades.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - Executou {func.__name__} com args={args} kwargs={kwargs}. Retorno: {resultado}\n")
        return resultado
    return wrapper
