
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError(
        "Configure a variável OPENAI_API_KEY no arquivo .env."
    )

client = OpenAI(api_key=api_key)

MODELO = "gpt-4.1-mini"

prompts = {
    "Teste 1 - Prompt curto": (
        "Sugira uma carreira na área de tecnologia."
    ),
    "Teste 2 - Prompt detalhado": (
        "Atue como um mentor de carreiras especializado "
        "em tecnologia. Considere uma pessoa iniciante, "
        "sem experiência profissional e interessada em "
        "programação e inteligência artificial. Analise "
        "seus possíveis caminhos profissionais, apresente "
        "três opções de carreira, as habilidades necessárias, "
        "as linguagens de programação recomendadas, cursos "
        "e projetos práticos para desenvolver o portfólio. "
        "Monte um plano de estudos de seis meses, dividido "
        "por etapas, e sugira como conseguir a primeira "
        "oportunidade profissional. Organize a resposta "
        "em tópicos, com orientações claras e realistas."
    ),
}

resultados = []

for nome, prompt in prompts.items():
    print("\n" + "=" * 55)
    print(nome)
    print("=" * 55)

    resposta = client.responses.create(
        model=MODELO,
        input=prompt,
    )

    uso = resposta.usage

    entrada = uso.input_tokens
    saida = uso.output_tokens
    total = uso.total_tokens

    print("\nResposta do mentor:")
    print(resposta.output_text)

    print("\nConsumo de tokens:")
    print(f"Tokens de entrada: {entrada}")
    print(f"Tokens de saída:   {saida}")
    print(f"Total de tokens:   {total}")

    resultados.append({
        "teste": nome,
        "entrada": entrada,
        "saida": saida,
        "total": total,
    })

print("\n" + "=" * 55)
print("COMPARAÇÃO DOS TESTES")
print("=" * 55)

for resultado in resultados:
    print(f"\n{resultado['teste']}")
    print(f"Entrada: {resultado['entrada']}")
    print(f"Saída:   {resultado['saida']}")
    print(f"Total:   {resultado['total']}")

curto, detalhado = resultados

print("\nAnálise comparativa:")

if detalhado["total"] > curto["total"]:
    diferenca = detalhado["total"] - curto["total"]
    print(
        f"O prompt detalhado consumiu {diferenca} tokens "
        "a mais no total."
    )
elif curto["total"] > detalhado["total"]:
    diferenca = curto["total"] - detalhado["total"]
    print(
        f"O prompt curto consumiu {diferenca} tokens "
        "a mais no total."
    )
else:
    print("Os dois testes consumiram o mesmo total de tokens.")

print(
    "\nObservação: o consumo de saída também depende "
    "do tamanho das respostas geradas pela IA."
)
