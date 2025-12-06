"""
Prepara a estrutura de deploy para ATA Plus no GitHub Pages
Copia os arquivos gerados para a pasta docs/
"""

import shutil
import sys
from pathlib import Path
from datetime import datetime

# Configura encoding UTF-8 para o console Windows
if sys.platform == 'win32':
    import codecs
    sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
    sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')

# Diretórios
BASE_DIR = Path(__file__).parent.parent
DEPLOY_DIR = Path(__file__).parent / "docs"

# Pastas de origem
TABELA_ORIGEM = BASE_DIR / "Tabela Ata Plus" / "tabela_preco.html"
APP_WEB_ORIGEM = BASE_DIR / "App Pedidos Ata Plus" / "app_pedidos_web.html"
APP_JSON_ORIGEM = BASE_DIR / "App Pedidos Ata Plus" / "dados.json"

# Pastas de destino
TABELA_DESTINO = DEPLOY_DIR / "tabela" / "index.html"
APP_DESTINO = DEPLOY_DIR / "app" / "index.html"
APP_JSON_DESTINO = DEPLOY_DIR / "app" / "dados.json"

print("="*60)
print("PREPARANDO DEPLOY - ATA PLUS")
print("="*60)
print(f"Hora: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
print()

# Função auxiliar para copiar arquivo
def copiar_arquivo(origem, destino, descricao):
    """Copia um arquivo e exibe resultado"""
    if not origem.exists():
        print(f"❌ {descricao}")
        print(f"   Arquivo não encontrado: {origem}")
        return False

    # Cria diretório de destino se não existir
    destino.parent.mkdir(parents=True, exist_ok=True)

    # Copia o arquivo
    shutil.copy2(origem, destino)

    tamanho_kb = destino.stat().st_size / 1024
    if tamanho_kb > 1024:
        tamanho_str = f"{tamanho_kb/1024:.2f} MB"
    else:
        tamanho_str = f"{tamanho_kb:.1f} KB"

    print(f"✅ {descricao}")
    print(f"   Origem: {origem.name}")
    print(f"   Destino: {destino.relative_to(DEPLOY_DIR.parent)}")
    print(f"   Tamanho: {tamanho_str}")
    print()
    return True

# Copia os arquivos
sucessos = 0

if copiar_arquivo(TABELA_ORIGEM, TABELA_DESTINO, "Tabela de Preços ATA Plus"):
    sucessos += 1

if copiar_arquivo(APP_WEB_ORIGEM, APP_DESTINO, "App de Pedidos (HTML)"):
    sucessos += 1

if copiar_arquivo(APP_JSON_ORIGEM, APP_JSON_DESTINO, "App de Pedidos (JSON)"):
    sucessos += 1

# Resumo
print("="*60)
print("RESUMO")
print("="*60)
print(f"Arquivos copiados: {sucessos}/3")

if sucessos == 3:
    print("\n✅ Deploy preparado com sucesso!")
    print("\nEstrutura criada em docs/:")
    print("  docs/")
    print("  ├── index.html        (landing page)")
    print("  ├── app/")
    print("  │   ├── index.html    (app de pedidos)")
    print("  │   └── dados.json    (dados dos produtos)")
    print("  └── tabela/")
    print("      └── index.html    (tabela de preços)")
    print("\nPróximos passos:")
    print("  1. cd ata-plus-deploy")
    print("  2. git init (se ainda não inicializou)")
    print("  3. git add .")
    print("  4. git commit -m 'Deploy inicial ATA Plus'")
    print("  5. git remote add origin <URL-DO-REPO>")
    print("  6. git push -u origin main")
else:
    print(f"\n⚠️ Alguns arquivos não foram encontrados ({3-sucessos} faltando)")
    print("Execute primeiro:")
    print("  1. python exportar_tabela_ata_plus.py")
    print("  2. cd 'Tabela Ata Plus' && python gerador_tabela.py")
    print("  3. cd 'App Pedidos Ata Plus' && python gerar_app_v2.py")

print("="*60)
