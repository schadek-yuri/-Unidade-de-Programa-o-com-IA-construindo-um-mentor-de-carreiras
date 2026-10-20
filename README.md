
# Mentor de Carreiras com IA — Análise de Tokens

## Sobre o projeto

Este projeto foi desenvolvido como atividade prática da
unidade de Programação com IA: construindo um mentor de
carreiras.

O objetivo é comparar o consumo de tokens de dois prompts
enviados a um modelo de inteligência artificial:

- Prompt curto: solicita uma sugestão de carreira em tecnologia.
- Prompt detalhado: solicita uma orientação profissional
  estruturada, com opções de carreira e plano de estudos.

## Objetivos

- Executar dois testes com prompts de tamanhos diferentes.
- Identificar os tokens de entrada e de saída.
- Calcular o total de tokens consumidos.
- Comparar os resultados e analisar as diferenças.

## Tecnologias utilizadas

- Python
- API da OpenAI
- Biblioteca openai
- Biblioteca python-dotenv

## Como executar

### 1. Instale o Python

Utilize uma versão compatível com as bibliotecas instaladas.

### 2. Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/mentor-carreiras-consumo-tokens.git
cd mentor-carreiras-consumo-tokens
```

### 3. Crie um ambiente virtual

```bash
python -m venv .venv
```

Ative o ambiente virtual:

Windows:

```bash
.venv\Scripts\activate
```

Linux ou macOS:

```bash
source .venv/bin/activate
```

### 4. Instale as dependências

```bash
pip install -r requirements.txt
```

### 5. Configure a chave da API

Crie um arquivo `.env` na raiz do projeto e adicione:

```dotenv
OPENAI_API_KEY=sua_chave_api_aqui
```

É necessário ter uma chave válida e acesso à API.
O uso da API pode gerar cobranças conforme o modelo
e as tarifas vigentes.

### 6. Execute o programa

```bash
python main.py
```

## Resultados

O programa apresenta, para cada teste:

- Tokens de entrada.
- Tokens de saída.
- Total de tokens consumidos.

Os números devem ser preenchidos com os valores reais
obtidos durante a execução.

| Teste | Tokens de entrada | Tokens de saída | Total |
|---|---:|---:|---:|
| Prompt curto | Preencher | Preencher | Preencher |
| Prompt detalhado | Preencher | Preencher | Preencher |

## Análise e conclusão

Espera-se que o prompt detalhado utilize mais tokens de
entrada, pois contém mais instruções e contexto.

O total de tokens também depende da resposta produzida
pelo modelo. Uma solicitação detalhada pode gerar uma
resposta maior e, consequentemente, aumentar o consumo
de tokens de saída.

Após executar o programa, compare os valores apresentados
e registre qual teste consumiu mais tokens.

## Aprendizado

O experimento demonstra que a construção de prompts
influencia o uso de recursos de modelos de IA. Prompts
mais detalhados podem melhorar a especificidade das
respostas, mas também podem aumentar o consumo de tokens.

## Autor

Desenvolvido como projeto educacional de Programação com IA.
