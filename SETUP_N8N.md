# 🚀 SETUP N8N - Passo a Passo Completo

## ✅ NOVO WORKFLOW CORRIGIDO

Criamos um novo arquivo corrigido:
```
workflow_n8n_completo.json
```

---

## 📥 PASSO 1: Importar Workflow

### **Opção A - Via Interface (Recomendado)**

1. Abra seu N8N (http://localhost:5678)
2. Clique em **"Workflows"** no menu lateral
3. Clique em **"+ Add workflow"**
4. Clique em **"Import from file"**
5. Selecione: **`workflow_n8n_completo.json`**
6. Clique em **"Import"**

### **Opção B - Copiar e Colar JSON**

1. Abra o arquivo `workflow_n8n_completo.json` no Notepad
2. Copie TODO o conteúdo (Ctrl+A, Ctrl+C)
3. No N8N, clique em **"+ Add workflow"**
4. Clique nos 3 pontinhos (...) no canto superior direito
5. Selecione **"Import from URL or text"**
6. Cole o JSON copiado
7. Clique em **"Import"**

---

## ⚙️ PASSO 2: Configurar Nós

### **Nó 1: "A cada hora" (Schedule Trigger)**

Este nó já está configurado! ✅
- **Tipo:** Schedule Trigger
- **Execução:** A cada hora (minuto 0)
- **Cron:** `0 * * * *`

**Se quiser alterar a frequência:**
1. Clique no nó "A cada hora"
2. Altere a **Cron Expression**
3. Exemplos:
   - A cada 2 horas: `0 */2 * * *`
   - 3x ao dia (9h, 14h, 18h): `0 9,14,18 * * *`

### **Nó 2: "Executar Atualização ATA Plus" (Execute Command)**

**IMPORTANTE - Verificar configurações:**

1. Clique no nó "Executar Atualização ATA Plus"
2. Verifique se está assim:

```
Command: python
Arguments: atualizar_ata_plus.py
```

3. Clique em **"Add Option"** → **"Working Directory"**
4. Cole o caminho:
```
C:\Users\compr\OneDrive\Estoque\precos_project\ata-plus-deploy
```

5. Clique em **"Settings"** (engrenagem ao lado do nome do nó)
6. Configure:
   - **Timeout:** `600` (10 minutos)
   - **Continue On Fail:** `false`

---

## 🧪 PASSO 3: Testar o Workflow

### **Teste Manual (Antes de Ativar)**

1. Com o workflow aberto, clique em **"Test workflow"** (canto superior direito)
2. Clique no nó **"A cada hora"**
3. Clique em **"Execute Node"**
4. Aguarde a execução (~3-5 minutos)

### **Verificar Resultado do Teste**

Após executar:

**✅ Sucesso (nó verde):**
- Exit code: `0`
- Veja os logs no output
- Última linha deve ser algo como: "EXECUÇÃO COMPLETA - SUCESSO TOTAL!"

**❌ Erro (nó vermelho):**
- Veja a mensagem de erro
- Confira a seção **"Troubleshooting"** abaixo

---

## ✅ PASSO 4: Ativar Workflow

**SOMENTE após o teste funcionar:**

1. No canto superior direito, encontre o switch **"Inactive"**
2. Clique para mudar para **"Active"** (fica verde)
3. Pronto! Workflow rodando automaticamente

---

## 🔍 PASSO 5: Monitorar

### **Ver Execuções**

1. Menu lateral → **"Executions"**
2. Veja todas as execuções automáticas
3. Clique em uma para ver detalhes

### **Ver Log da Última Atualização**

Arquivo automático criado pelo script:
```
C:\Users\compr\OneDrive\Estoque\precos_project\ata-plus-deploy\ultimo_log.json
```

Abra no Notepad para ver:
```json
{
  "inicio": "2025-12-08T18:00:00",
  "fim": "2025-12-08T18:03:25",
  "duracao_segundos": 205,
  "etapas_sucesso": 5,
  "etapas_erro": 0
}
```

---

## ❌ TROUBLESHOOTING

### **Erro: "python não é reconhecido"**

**Solução 1 - Usar caminho completo:**
1. Clique no nó "Executar Atualização ATA Plus"
2. Em **"Command"**, mude de `python` para:
```
C:\Users\compr\AppData\Local\Programs\Python\Python313\python.exe
```

**Solução 2 - Adicionar Python ao PATH:**
1. Pesquise "Variáveis de Ambiente" no Windows
2. Edite a variável PATH
3. Adicione: `C:\Users\compr\AppData\Local\Programs\Python\Python313`
4. Reinicie o N8N

### **Erro: "Arquivo não encontrado"**

Verifique se o caminho está correto:
```
C:\Users\compr\OneDrive\Estoque\precos_project\ata-plus-deploy
```

Para confirmar, rode no CMD:
```bash
cd C:\Users\compr\OneDrive\Estoque\precos_project\ata-plus-deploy
dir atualizar_ata_plus.py
```

Se aparecer o arquivo, o caminho está correto!

### **Erro: "Timeout"**

Se a execução demorar mais de 10 minutos:

1. Clique no nó → **Settings**
2. Aumente **Timeout** para `900` (15 minutos)

### **Workflow não dispara automaticamente**

Verifique:
- [ ] Switch está **"Active"** (verde)?
- [ ] N8N está rodando?
- [ ] Teste manual funcionou?

---

## 📊 ESTRUTURA DO WORKFLOW

```
┌─────────────────┐
│  A cada hora    │  ← Trigger automático
│  (Cron: 0 * *)  │     Executa no minuto 0
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Executar        │  ← Roda Python script
│ atualizar_ata   │     5 etapas automaticas
│ _plus.py        │
└─────────────────┘
```

### **O que o script faz (5 etapas):**

1. ✅ **Exportar CSV** - Puxa dados do ERP (TAB00005)
2. ✅ **Gerar Tabela** - Cria HTML da tabela de preços
3. ✅ **Gerar App** - Cria app de pedidos (HTML + JSON)
4. ✅ **Preparar Deploy** - Organiza arquivos na pasta `docs/`
5. ✅ **Git Push** - Faz commit e push para GitHub

**Resultado:** Site atualizado automaticamente! 🎉

---

## 🎯 CHECKLIST FINAL

Antes de considerar concluído:

- [ ] Workflow importado com sucesso
- [ ] Nó "A cada hora" configurado
- [ ] Nó "Executar Atualização" com caminho correto
- [ ] Working Directory configurado
- [ ] Timeout configurado (600 segundos)
- [ ] Teste manual executado - ✅ SUCESSO
- [ ] Workflow ativado (switch verde)
- [ ] Primeira execução automática confirmada
- [ ] Site atualizado: https://ltpsx.github.io/mac-ata-plus/

---

## 📧 OPCIONAL: Adicionar Notificações

### **Adicionar Email quando atualizar:**

1. Após o nó "Executar Atualização", clique em **"+"**
2. Adicione nó **"Send Email"**
3. Configure SMTP
4. Mensagem exemplo:
```
Assunto: ✅ ATA Plus Atualizado

ATA Plus foi atualizado com sucesso!
Horário: {{ $now }}
Site: https://ltpsx.github.io/mac-ata-plus/
```

---

## 🚀 RESULTADO FINAL

Com tudo configurado:
- ✅ Atualização **automática** a cada hora
- ✅ Dados do ERP **sempre atualizados** no site
- ✅ **Zero** intervenção manual
- ✅ Log de cada execução salvo
- ✅ App funcionando 24/7

**Pronto para produção!** 💪🎉
