
# ETAPA 1 - EXTRAÇÃO
# A extração foi simulada através de uma lista de dados fictícios criada diretamente em Python.
usuarios = [
    {"nome": "Ana Silva", "conta": "12345", "cartao": "**** 1234"},
    {"nome": "Bruno Costa", "conta": "67890", "cartao": "**** 5678"},
    {"nome": "Carla Souza", "conta": "24680", "cartao": "**** 9012"}
]


# ETAPA 2 - TRANSFORMAÇÃO
# Agora vamos gerar mensagens personalizadas, simulando o uso de IA.
def gerar_mensagem(usuario):
    return (
        f"Olá {usuario['nome']}! 😊 "
        f"Sua conta {usuario['conta']} com o cartão {usuario['cartao']} "
        "possui novas ofertas disponíveis."
    )

# ETAPA 3 - CARREGAMENTO
# Na alternativa simples, o carregamento será exibir o resultado no terminal.
for usuario in usuarios:
    print(gerar_mensagem(usuario))
