# 🔄 Workflow N8N - Atualização Automática ATA Plus

## 📋 Visão Geral

Este workflow atualiza automaticamente a Tabela ATA Plus e o App de Pedidos a cada hora.

**O que faz:**
1. Exporta dados do ERP (TAB00005)
2. Gera HTML da tabela de preços
3. Gera App de Pedidos (offline + online)
4. Prepara estrutura de deploy
5. Faz commit e push para GitHub
6. GitHub Actions publica automaticamente

---

## 🛠️ Configuração no N8N

### **1. Criar Novo Workflow**

No n8n, crie um novo workflow com os seguintes nós:

#### **Nó 1: Schedule Trigger (Cron)**
- **Node Type:** Schedule Trigger
- **Trigger Interval:** Cron Expression
- **Cron Expression:** `0 * * * *` (a cada hora no minuto 0)
- **Alternativa:** `0 */1 * * *` (também a cada hora)

**Para testar:** Use `*/5 * * * *` (a cada 5 minutos)

---

#### **Nó 2: Execute Command**
- **Node Type:** Execute Command
- **Command:** `python`
- **Arguments (separados):**
  ```
  C:\Users\compr\OneDrive\Estoque\precos_project\ata-plus-deploy\atualizar_ata_plus.py
  ```
- **Working Directory:**
  ```
  C:\Users\compr\OneDrive\Estoque\precos_project
  ```
- **Timeout:** 600000 (10 minutos em ms)

---

#### **Nó 3: IF (Verificar Sucesso) - Opcional**
- **Node Type:** IF
- **Condition:** `{{ $json.code }}` equals `0`
- **True:** Enviar notificação de sucesso
- **False:** Enviar alerta de erro

---

#### **Nó 4a: Webhook/Notificação (Sucesso)**
- **Node Type:** HTTP Request ou Email ou Telegram
- **Message:**
  ```
  ✅ ATA Plus atualizado com sucesso!
  Horário: {{ $now.format('DD/MM/YYYY HH:mm') }}
  Site: https://ltpsx.github.io/mac-ata-plus/
  ```

---

#### **Nó 4b: Webhook/Notificação (Erro)**
- **Node Type:** HTTP Request ou Email ou Telegram
- **Message:**
  ```
  ❌ Erro na atualização ATA Plus
  Horário: {{ $now.format('DD/MM/YYYY HH:mm') }}
  Verifique os logs
  ```

---

## 📄 Estrutura Completa do Workflow (JSON)

Você pode importar este workflow no n8n:

```json
{
  "name": "ATA Plus - Atualização Automática",
  "nodes": [
    {
      "parameters": {
        "rule": {
          "interval": [
            {
              "field": "cronExpression",
              "expression": "0 * * * *"
            }
          ]
        }
      },
      "name": "A cada hora",
      "type": "n8n-nodes-base.scheduleTrigger",
      "position": [250, 300]
    },
    {
      "parameters": {
        "command": "python",
        "arguments": "C:\\Users\\compr\\OneDrive\\Estoque\\precos_project\\ata-plus-deploy\\atualizar_ata_plus.py",
        "workingDirectory": "C:\\Users\\compr\\OneDrive\\Estoque\\precos_project"
      },
      "name": "Executar Atualização",
      "type": "n8n-nodes-base.executeCommand",
      "position": [450, 300]
    }
  ],
  "connections": {
    "A cada hora": {
      "main": [
        [
          {
            "node": "Executar Atualização",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  }
}
```

---

## 🧪 Como Testar

### **Teste Manual (via Command Line)**
```bash
python C:\Users\compr\OneDrive\Estoque\precos_project\ata-plus-deploy\atualizar_ata_plus.py
```

### **Verificar Logs**
O script salva um log JSON em:
```
ata-plus-deploy/ultimo_log.json
```

Conteúdo do log:
```json
{
  "inicio": "2025-12-06T09:00:00",
  "fim": "2025-12-06T09:02:30",
  "duracao_segundos": 150.5,
  "etapas_sucesso": 5,
  "etapas_erro": 0,
  "etapas": [...]
}
```

---

## ⚙️ Configurações Recomendadas

### **Horários Sugeridos:**

1. **A cada hora:**
   ```
   0 * * * *
   ```

2. **Horário comercial (8h-18h):**
   ```
   0 8-18 * * *
   ```

3. **A cada 2 horas:**
   ```
   0 */2 * * *
   ```

4. **Horários específicos (9h, 12h, 15h, 18h):**
   ```
   0 9,12,15,18 * * *
   ```

---

## 📊 Monitoramento

### **Verificar se funcionou:**
1. Acesse: https://github.com/ltpsx/mac-ata-plus/actions
2. Veja se há um novo workflow executado
3. Verifique o horário do último commit

### **Logs do N8N:**
- Acesse as execuções do workflow no n8n
- Verifique o output do nó "Execute Command"
- Código de saída:
  - `0` = Sucesso
  - `1` = Erro

---

## 🔧 Troubleshooting

### **Erro: Python não encontrado**
Certifique-se que o Python está no PATH ou use o caminho completo:
```
C:\Users\compr\AppData\Local\Programs\Python\Python313\python.exe
```

### **Erro: Módulos não encontrados**
Instale as dependências:
```bash
pip install pyodbc
```

### **Erro: Git não encontrado**
Instale o Git e adicione ao PATH ou use caminho completo no script.

### **Timeout no N8N**
Aumente o timeout no nó Execute Command:
- Padrão: 600000 ms (10 minutos)
- Se necessário: 900000 ms (15 minutos)

---

## 📝 Notas Importantes

- ✅ O script tem **timeout de 5 minutos por etapa**
- ✅ Logs são salvos em `ultimo_log.json`
- ✅ Git commit sem mudanças **não é erro**
- ✅ Exit code 0 = sucesso, 1 = erro
- ✅ Script é **idempotente** (pode rodar múltiplas vezes)

---

## 🎯 Resultado Final

Após configurar, você terá:
- 🔄 Atualização automática a cada hora
- 📊 Dados sempre atualizados no site
- 📱 App offline atualizado
- 🌐 GitHub Pages com versão mais recente
- 📝 Logs de cada execução

**Site publicado:** https://ltpsx.github.io/mac-ata-plus/
