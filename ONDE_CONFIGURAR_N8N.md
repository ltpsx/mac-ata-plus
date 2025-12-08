# 📍 ONDE CONFIGURAR CADA CAMPO NO N8N

## 🎯 Tela que você está vendo agora

Você está no nó **"Executar Atualização ATA Plus"** correto! Agora veja onde configurar cada coisa:

---

## 1️⃣ CAMPO "Command" ✅
**Onde está:** Você já vê na tela - campo grande com "python"

**O que fazer:** Deixar como está: `python`

✅ **Este campo já está correto!**

---

## 2️⃣ CAMPO "Arguments" ❌ (FALTANDO!)

**Onde está:** Logo ABAIXO do campo "Command"

**Como adicionar:**
- Se você NÃO vê um campo chamado "Arguments", procure um botão **"Add Field"** ou **"Add parameter"**
- Clique nele
- Selecione **"Arguments"** na lista
- Um novo campo vai aparecer

**O que digitar no campo Arguments:**
```
atualizar_ata_plus.py
```

---

## 3️⃣ OPÇÃO "Working Directory" ❌ (FALTANDO!)

**Onde está:** Você precisa rolar a página para baixo!

**Como adicionar:**
1. **Role a tela para BAIXO** (role bem para baixo mesmo!)
2. Procure um botão chamado **"Add Option"** (geralmente é cinza/azul)
3. Clique nele
4. Vai abrir uma lista de opções
5. Procure e selecione **"Working Directory"** ou **"CWD"**
6. Um novo campo vai aparecer

**O que digitar no campo Working Directory:**
```
C:\Users\compr\OneDrive\Estoque\precos_project\ata-plus-deploy
```

---

## 4️⃣ CONFIGURAR TIMEOUT (IMPORTANTE!)

**Onde está:** Clique na **ENGRENAGEM** ⚙️ ao lado do nome do nó (canto superior)

**Como configurar:**
1. Clique na engrenagem ⚙️ ao lado de "Executar Atualização ATA Plus"
2. Vai abrir um painel lateral com "Settings"
3. Procure o campo **"Timeout"**
4. Digite: `600` (600 segundos = 10 minutos)

---

## 📋 RESUMO - O QUE VOCÊ PRECISA VER NA TELA:

Quando estiver tudo configurado, o nó deve mostrar:

```
┌─────────────────────────────────────────────┐
│ Executar Atualização ATA Plus           ⚙️ │
├─────────────────────────────────────────────┤
│                                             │
│ Execute Once: [toggle ligado]              │
│                                             │
│ Command:                                    │
│ ┌─────────────────────────────────────────┐│
│ │ python                                  ││
│ └─────────────────────────────────────────┘│
│                                             │
│ Arguments:                                  │
│ ┌─────────────────────────────────────────┐│
│ │ atualizar_ata_plus.py                   ││
│ └─────────────────────────────────────────┘│
│                                             │
│ [+ Add Field]                               │
│                                             │
│ ─────────── OPTIONS ───────────             │
│                                             │
│ Working Directory:                          │
│ ┌─────────────────────────────────────────┐│
│ │ C:\Users\compr\OneDrive\Estoque\...     ││
│ └─────────────────────────────────────────┘│
│                                             │
│ [+ Add Option]                              │
│                                             │
└─────────────────────────────────────────────┘
```

---

## 🔍 NÃO ENCONTROU "Arguments"?

### Opção A - Versão antiga do N8N
Se o seu N8N for versão antiga, pode ser que o campo "Arguments" não exista separado.

**SOLUÇÃO:** Coloque tudo junto no campo "Command":
```
python atualizar_ata_plus.py
```

E ainda assim adicione o "Working Directory"!

---

### Opção B - Campo com outro nome
Alguns N8N chamam de:
- **"Script"** ao invés de "Arguments"
- **"Parameters"** ao invés de "Arguments"

---

## ✅ TESTE RÁPIDO

Depois de configurar tudo:

1. Clique em **"Execute step"** (botão laranja no canto superior direito)
2. **IMPORTANTE:** Antes de executar, feche TODOS os arquivos CSV/Excel abertos!
3. Aguarde 2-3 minutos
4. Deve ficar verde ✅

---

## ❌ SE DER ERRO

### Erro: "python not found"
**Solução:** No campo "Command", use o caminho completo:
```
C:\Users\compr\AppData\Local\Programs\Python\Python313\python.exe
```

### Erro: "Permission denied"
**Solução:** Feche todos os arquivos CSV/Excel e tente novamente

### Erro: "File not found"
**Solução:** Verifique se o "Working Directory" está correto

---

## 📸 DICA VISUAL

Se ainda estiver confuso, **tire um print da tela inteira** do nó e me manda!
Assim posso te dizer exatamente o que está faltando! 😊
