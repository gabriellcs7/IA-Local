# IA Local

[![Python](https://img.shields.io/badge/Python-3.10%2B-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Transformers](https://img.shields.io/badge/%F0%9F%A4%97%20Transformers-5.x-FFD21E)](https://huggingface.co/docs/transformers/)
[![Model](https://img.shields.io/badge/Modelo-Qwen2.5--1.5B--Instruct-6F42C1)](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)
[![License: MIT](https://img.shields.io/badge/Licen%C3%A7a-MIT-green.svg)](LICENSE)

Aplicação de linha de comando que executa um modelo de inteligência artificial generativa localmente. O projeto utiliza o **Qwen2.5-1.5B-Instruct** por meio da biblioteca **Transformers** para gerar respostas a partir de um prompt definido no código.

> [!NOTE]
> Na primeira execução, é necessário acesso à internet para baixar o modelo. Depois que os arquivos estiverem armazenados no cache local, o programa poderá ser executado sem conexão.

## Funcionalidades

- Geração local de texto com um modelo de linguagem;
- Personalização do prompt diretamente no código;
- Controle do tamanho e da criatividade da resposta;
- Execução simples pelo terminal.

## Tecnologias

- [Python](https://www.python.org/) — linguagem principal;
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/) — carregamento e execução do pipeline de geração;
- [PyTorch](https://pytorch.org/) — mecanismo de inferência;
- [Qwen2.5-1.5B-Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct) — modelo de linguagem utilizado.

## Pré-requisitos

- Python 3.10 ou superior;
- Git;
- Espaço em disco e memória suficientes para carregar o modelo;
- Internet durante o primeiro download do modelo.

## Instalação

Clone o repositório e entre na pasta do projeto:

```bash
git clone https://github.com/gabriellcs7/IA-Local.git
cd IA-Local
```

Crie um ambiente virtual:

```bash
python -m venv .venv
```

Ative o ambiente virtual no Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```bash
python -m pip install --upgrade pip
python -m pip install transformers torch
```

## Uso

Execute o programa com:

```bash
python main.py
```

Para fazer outra pergunta, altere a variável `prompt` em `main.py`:

```python
prompt = """
Você é um professor de programação.

Responda à pergunta: Como surgiu a linguagem Java?

Resposta:
"""
```

Também é possível ajustar os parâmetros de geração:

```python
resposta = ia(
    prompt,
    max_new_tokens=500,
    temperature=0.3,
)
```

- `max_new_tokens` define o tamanho máximo da resposta;
- `temperature` controla a variação do texto: valores menores tendem a gerar respostas mais previsíveis.

## Estrutura do projeto

```text
IA-Local/
├── main.py      # Carrega o modelo e gera a resposta
├── LICENSE      # Licença do projeto
└── README.md    # Documentação
```

## Observações

O tempo de carregamento e geração depende do hardware disponível. A primeira execução costuma ser mais demorada devido ao download dos arquivos do modelo.

## Licença

Este projeto está disponível sob a [Licença MIT](LICENSE).

---

Desenvolvido por [Gabriel Costa](https://github.com/gabriellcs7).
