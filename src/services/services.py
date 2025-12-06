"""
Qualquer inteligência do domínio

Funções que analisam conteúdo

Regras que NÃO são da LLM

Políticas de filtragem

Ações baseadas no que o usuário pediu

Chamada para outras APIs internas

Workflow que não depende só da LLM

Exemplos futuros:

Classificar intenções

Validar informações do usuário

Salvar histórico em banco

Analisar pedidos ("marcar consulta", "buscar produto")

Enriquecer dados enviados à LLM

O importante:

Tudo que é “regra real do sistema” fica em services,
e não no processor.
"""