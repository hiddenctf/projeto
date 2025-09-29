# README - Aplicativo de Automação de Emails HTML

## 📧 Sobre o Projeto

Este é um aplicativo desktop desenvolvido em Python para automação de envio de emails em massa com suporte completo para HTML. Ideal para newsletters, campanhas de marketing e comunicação corporativa.

Autor:Jean Carlos Ventura Motta

## ✨ Funcionalidades

- ✅ **Envio em massa** para múltiplos destinatários
- ✅ **Suporte a HTML** completo com templates pré-prontos
- ✅ **Interface gráfica** intuitiva e amigável
- ✅ **Templates incluídos**: Básico, Marketing e Newsletter
- ✅ **Envio assíncrono** sem travar a interface
- ✅ **Validação automática** de emails
- ✅ **Suporte a Gmail** (SMTP)

## 🚀 Como Usar

### Pré-requisitos

- Python 3.6 ou superior
- Conta do Gmail com acesso a "Apps menos seguros" habilitado

### Configuração do Gmail

1. Acesse: https://myaccount.google.com/security
2. Ative a opção **"Acesso a app menos seguro"**
3. Ou use **Senha de App** (recomendado):
   - Ative verificação em 2 etapas
   - Gere uma senha de app específica

### Executando o Aplicativo

1. **Salve o código** em um arquivo `email_sender.py`

2. **Execute o script**:
```bash
python email_sender.py
```

## 📋 Passo a Passo

### 1. Configuração Inicial
- Insira seu email do Gmail
- Digite sua senha (ou senha de app)
- Clique em "Salvar Credenciais"

### 2. Preparação do Email
- **Nome do Remetente**: Como você quer aparecer nos emails
- **Assunto**: Título do email
- **Conteúdo**: Use os botões de exemplo ou crie seu próprio HTML
- **Formato**: Marque "Usar formatação HTML" para emails estilizados

### 3. Lista de Destinatários
- Prepare um arquivo `.txt` com um email por linha:
```
cliente1@email.com
cliente2@email.com
cliente3@email.com
```

### 4. Envio
- Clique em "Carregar Lista de Emails"
- Selecione seu arquivo `.txt`
- Clique em "Enviar Emails"

## 🎨 Templates Incluídos

### 📄 Template Básico
- Layout profissional simples
- Cabeçalho colorido
- Botão de call-to-action
- Rodapé institucional

### 🎯 Template Marketing
- Design moderno com gradiente
- Lista de vantagens
- Botão promocional destacado
- Ideal para campanhas

### 📰 Template Newsletter
- Layout de notícias
- Múltiplas seções de conteúdo
- Links "Ler mais"
- Profissional para comunicações regulares

## ⚙️ Estrutura do Arquivo de Emails

Crie um arquivo `emails.txt` com o formato:
```txt
destinatario1@provedor.com
destinatario2@empresa.com
destinatario3@servico.com
```

## 🛠️ Tecnologias Utilizadas

- **Python 3** - Linguagem principal
- **Tkinter** - Interface gráfica
- **smtplib** - Protocolo de envio de emails
- **email** - Construção de mensagens
- **threading** - Processamento assíncrono

## 🔒 Segurança

- As credenciais são armazenadas apenas em memória durante a execução
- Conexão SMTP com criptografia TLS
- Recomendado usar **Senha de App** do Gmail
- Nenhum dado é armazenado permanentemente

## ❗ Solução de Problemas

### Erro de Autenticação
- Verifique se "Acesso a app menos seguro" está ativado
- Use senha de app se tiver verificação em 2 etapas
- Confirme se o email e senha estão corretos

### Emails Não Chegam
- Verifique a pasta de spam
- Confirme se o conteúdo HTML é válido
- Teste com menos destinatários inicialmente

### Arquivo Não Carrega
- Certifique-se que é um arquivo `.txt`
- Verifique se cada linha contém um email válido
- Formato: um email por linha

## 📝 Exemplo de Uso

1. **Comercial**: Campanhas de lançamento de produtos
2. **Educacional**: Comunicados para alunos
3. **Corporativo**: Newsletters internas
4. **Marketing**: Promoções e ofertas

