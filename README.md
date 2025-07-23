# Contador de Carboidratos

Este é um sistema em Python para registrar, consultar e gerar relatórios do consumo de carboidratos em refeições diárias.

## Funcionalidades

- **Registrar Refeição:** Adicione alimentos consumidos, informando o nome e a quantidade de carboidratos (em gramas).
- **Visualizar Consumo Diário:** Veja todas as refeições de um dia específico e o total de carboidratos consumidos.
- **Gerar Relatório Mensal:** Exporte um relatório Excel com todas as refeições de um mês, incluindo o total de carboidratos.

## Estrutura do Projeto

```
contador_carboidratos/
│
├── controller/              # Lógica principal do sistema
│   ├── database.py          # Funções de acesso ao banco de dados
│   ├── reports.py           # Geração de relatórios mensais
│   ├── ui.py                # Funções de interface com o usuário (inputs)
│   ├── menu.py              # Menu principal do sistema
│   └── models.py            # Modelos de dados (ex: Meal)
│
├── data/                    # Arquivos do banco de dados (ignorado no git)
├── reports/                 # Relatórios gerados (ignorado no git)
├── database_setup.py        # Script para criar o banco de dados
├── main.py                  # Ponto de entrada do sistema
├── requirements.txt         # Dependências do projeto
└── README.md                # Este arquivo
```

## Como usar

1. **Clone o repositório e instale as dependências:**

   ```sh
   git clone <url-do-repositorio>
   cd contador_carboidratos
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```

2. **Crie o banco de dados:**

   Execute o script de setup:
   ```sh
   python database_setup.py
   ```

3. **Execute o sistema:**

   ```sh
   python main.py
   ```

4. **Siga o menu interativo no terminal.**

## Observações

- O banco de dados é salvo na pasta `data/` e os relatórios em `reports/`.
- Para inserir valores decimais de carboidratos, use ponto ou vírgula (ex: `12.5` ou `12,5`).

## Requisitos

- Python 3.11+
- Veja as dependências em `requirements.txt`.

## Licença

Este projeto é livre para uso acadêmico e pessoal.

---

Se tiver dúvidas ou sugestões, abra uma issue ou envie um
