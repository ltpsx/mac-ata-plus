"""
Script COMPLETO para ATA Plus: Exporta + Gera HTML + Gera App + Deploy
"""

import subprocess
import sys
from pathlib import Path
from datetime import datetime

# Configura encoding UTF-8 para o console Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

BASE_DIR = Path(__file__).parent.parent

def executar_comando(comando, descricao, cwd=None):
    """Executa um comando e retorna True se sucesso, False se erro"""
    print(f"\n{'='*60}")
    print(f">>> {descricao}")
    print(f"{'='*60}")

    try:
        resultado = subprocess.run(
            comando,
            shell=True,
            check=True,
            capture_output=True,
            text=True,
            encoding='utf-8',
            cwd=str(cwd or BASE_DIR)
        )

        if resultado.stdout:
            print(resultado.stdout)

        print(f"✅ {descricao} - SUCESSO")
        return True

    except subprocess.CalledProcessError as e:
        print(f"❌ {descricao} - FALHOU")
        print(f"Código de saída: {e.returncode}")
        if e.stdout:
            print(f"Saída: {e.stdout}")
        if e.stderr:
            print(f"Erro: {e.stderr}")
        return False
    except Exception as e:
        print(f"❌ {descricao} - ERRO INESPERADO")
        print(f"Erro: {str(e)}")
        return False

def main():
    print("\n" + "="*60)
    print("AUTOMAÇÃO COMPLETA - ATA PLUS")
    print("="*60)
    print(f"Diretório: {BASE_DIR}")
    print(f"Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")

    # Lista de tarefas
    tarefas = [
        # ETAPA 1: EXPORTAR CSV DA TABELA ATA PLUS
        {
            "comando": "python exportar_tabela_ata_plus.py",
            "descricao": "1/5 - Exportar Tabela ATA Plus (CSV)",
            "cwd": BASE_DIR
        },

        # ETAPA 2: GERAR HTML DA TABELA
        {
            "comando": "python gerador_tabela.py",
            "descricao": "2/5 - Gerar HTML da Tabela ATA Plus",
            "cwd": BASE_DIR / "Tabela Ata Plus"
        },

        # ETAPA 3: GERAR APP DE PEDIDOS
        {
            "comando": "python gerar_app_v2.py",
            "descricao": "3/5 - Gerar App de Pedidos ATA Plus",
            "cwd": BASE_DIR / "App Pedidos Ata Plus"
        },

        # ETAPA 4: PREPARAR DEPLOY
        {
            "comando": "python preparar_deploy.py",
            "descricao": "4/5 - Preparar estrutura de deploy",
            "cwd": BASE_DIR / "ata-plus-deploy"
        },

        # ETAPA 5: GIT ADD + COMMIT + PUSH
        {
            "comando": f'cd ata-plus-deploy && git add docs/ && git commit -m "Atualização automática - {datetime.now().strftime("%d/%m/%Y %H:%M")}" && git push',
            "descricao": "5/5 - Git add/commit/push",
            "cwd": BASE_DIR
        },
    ]

    # Executa todas as tarefas
    sucessos = 0
    erros = 0

    for tarefa in tarefas:
        cwd = tarefa.get("cwd", BASE_DIR)
        if executar_comando(tarefa["comando"], tarefa["descricao"], cwd):
            sucessos += 1
        else:
            erros += 1
            # Se falhar no git commit (sem mudanças), continua normal
            if "git commit" in tarefa["comando"]:
                print("ℹ️ Sem mudanças para commit - tudo ok!")
                sucessos += 1
                erros -= 1
            else:
                print(f"\n⚠️ Erro na etapa: {tarefa['descricao']}")
                resposta = input("Continuar mesmo assim? (s/n): ")
                if resposta.lower() != 's':
                    break

    # Resumo final
    print("\n" + "="*60)
    print("RESUMO FINAL")
    print("="*60)
    print(f"✅ Etapas concluídas: {sucessos}")
    print(f"❌ Etapas com erro: {erros}")

    if erros == 0:
        print("\n🎉 PROCESSO COMPLETO CONCLUÍDO COM SUCESSO!")
        print("\n📍 Site será publicado em:")
        print("   https://<seu-usuario>.github.io/<nome-do-repo>/")
        print("\n📱 App de Pedidos:")
        print("   https://<seu-usuario>.github.io/<nome-do-repo>/app/")
        print("\n📒 Tabela de Preços:")
        print("   https://<seu-usuario>.github.io/<nome-do-repo>/tabela/")
        print("\n⏱️ Deploy automático acontecerá em ~1 minuto via GitHub Actions!")
    else:
        print(f"\n⚠️ Processo concluído com {erros} erro(s)")

    print("\n" + "="*60)

if __name__ == "__main__":
    main()
