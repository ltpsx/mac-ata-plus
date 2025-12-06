# 🛒 Sistema ATA Plus - MAC Atacado

Sistema automatizado para exportação e publicação da **Tabela de Preços ATA Plus** e **App de Pedidos**.

## 📱 Links Ativos

Após configurar o repositório GitHub:

- **App de Pedidos:** `https://<seu-usuario>.github.io/<nome-repo>/app/`
- **Tabela de Preços:** `https://<seu-usuario>.github.io/<nome-repo>/tabela/`
- **Landing Page:** `https://<seu-usuario>.github.io/<nome-repo>/`

## 🚀 Automação

Este repositório usa GitHub Actions para deploy automático. Os arquivos são atualizados automaticamente quando há push na branch `main`.

## 📂 Estrutura

```
ata-plus-deploy/
├── docs/                    # Pasta publicada no GitHub Pages
│   ├── index.html          # Página principal
│   ├── app/                # App de Pedidos ATA Plus
│   │   ├── index.html      # Interface do app
│   │   └── dados.json      # Dados dos produtos
│   └── tabela/             # Tabela de Preços ATA Plus
│       └── index.html
│
├── .github/
│   └── workflows/
│       └── deploy.yml      # GitHub Actions workflow
│
├── executar_tudo.py        # Script completo de automação
├── preparar_deploy.py      # Prepara estrutura docs/
└── README.md               # Este arquivo
```

## 🔄 Como Usar

### **Configuração Inicial (uma vez)**

1. Crie um novo repositório no GitHub (ex: `mac-ata-plus`)

2. Inicialize o Git e conecte ao repositório:
```bash
cd ata-plus-deploy
git init
git add .
git commit -m "Setup inicial ATA Plus"
git branch -M main
git remote add origin https://github.com/<seu-usuario>/<nome-repo>.git
git push -u origin main
```

3. Configure GitHub Pages:
   - Acesse: Settings → Pages
   - Source: **GitHub Actions**

### **Atualização Diária**

Execute o script completo que faz tudo automaticamente:

```bash
# Opção 1: Da raiz do projeto
python ata-plus-deploy/executar_tudo.py

# Opção 2: De dentro da pasta
cd ata-plus-deploy
python executar_tudo.py
```

O script executa automaticamente:
1. ✅ Exporta dados do ERP (TAB00005)
2. ✅ Gera HTML da Tabela de Preços
3. ✅ Gera App de Pedidos (HTML + JSON)
4. ✅ Prepara estrutura em `docs/`
5. ✅ Git add + commit + push

### **Atualização Manual (passo a passo)**

```bash
# 1. Exportar tabela do ERP
python exportar_tabela_ata_plus.py

# 2. Gerar HTML da tabela
cd "Tabela Ata Plus"
python gerador_tabela.py
cd ..

# 3. Gerar app de pedidos
cd "App Pedidos Ata Plus"
python gerar_app_v2.py
cd ..

# 4. Preparar deploy
cd ata-plus-deploy
python preparar_deploy.py

# 5. Publicar
git add docs/
git commit -m "Atualização manual"
git push
```

## 📊 Origem dos Dados

- **Tabela:** TAB00005 do ERP
- **Campos:** Código, Fabricante, Marca, Descrição, Estoque, Preço
- **Atualização:** Manual (execute os scripts)

## 🎯 Diferenças vs Sistema Principal

| Item | Sistema Principal | ATA Plus |
|---|---|---|
| Repositório | mac-tabelas-precos | mac-ata-plus |
| Tabela ERP | TAB00001 | TAB00005 |
| Tabelas | ATA, BIRIGUI, PRUDENTE | ATA Plus |
| Apps | App Pedidos (ATA) | App Pedidos (ATA Plus) |

## ⚙️ Tecnologias

- **Backend:** Python 3
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Exportação:** SheetJS (XLSX)
- **Deploy:** GitHub Pages
- **CI/CD:** GitHub Actions

## 📝 Observações

- Credenciais do banco ficam em `conexao.py` (não incluído no Git)
- O arquivo `.gitignore` já está configurado para ignorar dados sensíveis
- Deploy acontece automaticamente ~1 minuto após o push

---

**MAC Atacado** - Sistema de Gestão ATA Plus
# ATA Plus Deploy
