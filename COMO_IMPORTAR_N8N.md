# 📥 Como Importar o Workflow no N8N

## 🎯 Arquivo para Importar

```
workflow_n8n.json
```

---

## 📋 Passo a Passo

### **1. Abrir o N8N**
- Acesse seu N8N (http://localhost:5678 ou seu servidor)
- Faça login

### **2. Importar o Workflow**

**Opção A - Pelo Menu:**
1. Clique em **"Workflows"** no menu lateral
2. Clique no botão **"+ Add workflow"** → **"Import from file"**
3. Selecione o arquivo: `workflow_n8n.json`
4. Clique em **"Import"**

**Opção B - Arrastar e Soltar:**
1. Abra a aba de workflows
2. Arraste o arquivo `workflow_n8n.json` para a janela do N8N
3. Confirme a importação

### **3. Ativar o Workflow**
1. Após importar, o workflow será aberto
2. No canto superior direito, mude o switch de **"Inactive"** para **"Active"**
3. Pronto! O workflow está rodando

---

## ⚙️ O que o Workflow Faz

O workflow importado tem 2 nós:

### **Nó 1: Schedule Trigger - "A cada hora"**
- **Tipo:** Cron Trigger
- **Expressão:** `0 * * * *` (executa no minuto 0 de cada hora)
- **Exemplos:**
  - 08:00, 09:00, 10:00, 11:00... 23:00

### **Nó 2: Execute Command - "Executar Atualização ATA Plus"**
- **Comando:** `python`
- **Script:** `atualizar_ata_plus.py`
- **Caminho completo:** `C:\Users\compr\OneDrive\Estoque\precos_project\ata-plus-deploy\atualizar_ata_plus.py`

---

## 🔧 Personalizações

### **Alterar Frequência de Atualização**

1. Clique no nó **"A cada hora"**
2. Altere a **Cron Expression**:

| Frequência | Cron Expression |
|---|---|
| A cada hora | `0 * * * *` |
| A cada 2 horas | `0 */2 * * *` |
| A cada 30 minutos | `*/30 * * * *` |
| Horário comercial (8h-18h) | `0 8-18 * * *` |
| 4x ao dia (9h, 12h, 15h, 18h) | `0 9,12,15,18 * * *` |
| Apenas dias úteis | `0 * * * 1-5` |

### **Ajustar Timeout (se necessário)**

Se o script demorar mais de 2 minutos:

1. Clique no nó **"Executar Atualização ATA Plus"**
2. Clique em **"Settings"** (engrenagem)
3. Aumente o **"Timeout"** para `600000` (10 minutos em ms)

---

## 🧪 Testar o Workflow

### **Teste Manual**

1. Com o workflow aberto, clique em **"Test workflow"** (canto superior direito)
2. Clique no nó **"A cada hora"**
3. Clique em **"Execute Node"**
4. Aguarde a execução (leva ~3 minutos)
5. Verifique se o nó ficou verde ✅

### **Verificar Logs**

1. Após executar, clique no nó **"Executar Atualização ATA Plus"**
2. Veja a aba **"Output"**
3. Confira se:
   - Exit code = `0` (sucesso)
   - Há logs no output mostrando cada etapa

### **Verificar Resultado**

Após execução bem-sucedida:
1. Acesse: https://github.com/ltpsx/mac-ata-plus/actions
2. Veja se há um novo workflow executado
3. Aguarde ~1 minuto
4. Teste o site: https://ltpsx.github.io/mac-ata-plus/

---

## ❌ Troubleshooting

### **Erro: Python não encontrado**

**Solução 1 - Usar caminho completo:**
1. Clique no nó **"Executar Atualização ATA Plus"**
2. Altere o **"Command"** para o caminho completo do Python:
   ```
   C:\Users\compr\AppData\Local\Programs\Python\Python313\python.exe
   ```

**Solução 2 - Adicionar Python ao PATH:**
1. Adicione Python às variáveis de ambiente do Windows
2. Reinicie o N8N

### **Erro: Script não encontrado**

Verifique se o caminho está correto:
```
C:\Users\compr\OneDrive\Estoque\precos_project\ata-plus-deploy\atualizar_ata_plus.py
```

Se estiver diferente:
1. Clique no nó
2. Altere o **"Arguments"** com o caminho correto

### **Erro: Timeout**

Se a execução demorar muito:
1. Clique no nó → Settings
2. Aumente **Timeout** para `900000` (15 min)

### **Workflow não dispara automaticamente**

Verifique se:
1. O workflow está **"Active"** (switch verde no topo)
2. O N8N está rodando continuamente
3. Não há erros no console do N8N

---

## 📊 Monitoramento

### **Ver Execuções**
1. Menu lateral → **"Executions"**
2. Veja histórico de todas as execuções
3. Clique em uma para ver detalhes

### **Ver Última Atualização**
Verifique o arquivo de log:
```
C:\Users\compr\OneDrive\Estoque\precos_project\ata-plus-deploy\ultimo_log.json
```

Conteúdo do log:
```json
{
  "inicio": "2025-12-06T09:23:25",
  "fim": "2025-12-06T09:26:38",
  "duracao_segundos": 192.4,
  "etapas_sucesso": 5,
  "etapas_erro": 0
}
```

---

## 📧 Adicionar Notificações (Opcional)

Para receber alertas quando atualizar:

### **Adicionar nó de Email:**
1. Após o nó de execução, adicione um nó **"Email"**
2. Configure SMTP
3. Envie email com o resultado

### **Adicionar nó de Telegram:**
1. Adicione nó **"Telegram"**
2. Configure bot token
3. Envie mensagem quando concluir

### **Exemplo de mensagem:**
```
✅ ATA Plus atualizado!
Horário: {{ $now.format('DD/MM/YYYY HH:mm') }}
Produtos: 20.771
Site: https://ltpsx.github.io/mac-ata-plus/
```

---

## ✅ Checklist Final

Após importar e configurar:

- [ ] Workflow importado com sucesso
- [ ] Nó "A cada hora" configurado (cron correto)
- [ ] Nó "Executar Atualização" com caminho correto do Python
- [ ] Teste manual executado com sucesso (exit code 0)
- [ ] Workflow ativado (switch verde)
- [ ] Site atualizado: https://ltpsx.github.io/mac-ata-plus/

---

## 🎯 Resultado Final

Com o workflow ativo:
- ✅ Atualização automática a cada hora
- ✅ Dados do ERP sempre atualizados no site
- ✅ App offline atualizado automaticamente
- ✅ Sem intervenção manual necessária

**Pronto para produção!** 🚀
