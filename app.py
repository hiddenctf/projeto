

import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import threading

class EmailSenderApp:
    """
    Classe principal da aplicação de automação de emails
    Responsável pela interface gráfica e lógica de envio
    """
    
    def __init__(self, root):
        """
        Inicializa a aplicação
        
        Args:
            root: Janela principal do Tkinter
        """
        self.root = root
        # Configuração da janela principal
        self.root.title("Envio de Emails Automático - HTML")
        self.root.geometry("600x800")
        
        # Variáveis de instância para armazenar dados
        self.email_remetente = ""      # Email do remetente
        self.senha = ""                # Senha do email
        self.nome_remetente = ""       # Nome que aparecerá no remetente
        self.emails_carregados = []    # Lista de destinatários
        self.conteudo_email = ""       # Corpo do email
        self.usar_html = tk.BooleanVar(value=True)  # Controle HTML vs texto puro
        
        # Inicializa a interface do usuário
        self.setup_ui()

    def setup_ui(self):
        """
        Configura toda a interface gráfica do usuário
        Divide em duas telas: credenciais e envio
        """
        # ========== PRIMEIRA TELA - CREDENCIAIS ==========
        self.credentials_frame = tk.Frame(self.root)
        self.credentials_frame.pack(pady=10)
        
        # Campo para email do remetente
        tk.Label(self.credentials_frame, text="Email Remetente:").pack()
        self.email_entry = tk.Entry(self.credentials_frame, width=40)
        self.email_entry.pack(pady=5)
        
        # Campo para senha (com mascara de segurança)
        tk.Label(self.credentials_frame, text="Senha:").pack()
        self.password_entry = tk.Entry(self.credentials_frame, width=40, show="*")
        self.password_entry.pack(pady=5)
        
        # Botão para salvar credenciais e avançar
        save_btn = tk.Button(self.credentials_frame, text="Salvar Credenciais", 
                           command=self.save_credentials)
        save_btn.pack(pady=10)
        
        # ========== SEGUNDA TELA - ENVIO DE EMAILS ==========
        self.main_frame = tk.Frame(self.root)
        
        # Campo para nome do remetente (como aparecerá nos emails)
        tk.Label(self.main_frame, text="Nome do Remetente:").pack()
        self.nome_remetente_entry = tk.Entry(self.main_frame, width=40)
        self.nome_remetente_entry.pack(pady=5)
        
        # Campo para assunto do email
        tk.Label(self.main_frame, text="Assunto do Email:").pack()
        self.assunto_entry = tk.Entry(self.main_frame, width=40)
        self.assunto_entry.pack(pady=5)
        
        # Checkbox para escolher entre HTML e texto puro
        html_check = tk.Checkbutton(self.main_frame, text="Usar formatação HTML", 
                                  variable=self.usar_html)
        html_check.pack(pady=5)
        
        # Área de texto para conteúdo do email (com scroll)
        tk.Label(self.main_frame, text="Conteúdo do Email:").pack()
        
        # Frame para botões de exemplo HTML
        exemplo_frame = tk.Frame(self.main_frame)
        exemplo_frame.pack(pady=5)
        
        tk.Button(exemplo_frame, text="Exemplo Básico HTML", 
                 command=self.inserir_exemplo_basico).pack(side=tk.LEFT, padx=2)
        tk.Button(exemplo_frame, text="Exemplo Marketing", 
                 command=self.inserir_exemplo_marketing).pack(side=tk.LEFT, padx=2)
        tk.Button(exemplo_frame, text="Exemplo Newsletter", 
                 command=self.inserir_exemplo_newsletter).pack(side=tk.LEFT, padx=2)
        
        self.conteudo_text = scrolledtext.ScrolledText(self.main_frame, width=70, height=20)
        self.conteudo_text.pack(pady=5, fill=tk.BOTH, expand=True)
        
        # Botão para carregar lista de emails de arquivo .txt
        self.btn_carregar = tk.Button(self.main_frame, text="Carregar Lista de Emails", 
                                    command=self.carregar_arquivo)
        self.btn_carregar.pack(pady=10)
        
        # Botão para iniciar envio (inicialmente desabilitado)
        self.btn_enviar = tk.Button(self.main_frame, text="Enviar Emails", 
                                  command=self.iniciar_envio, state=tk.DISABLED)
        self.btn_enviar.pack(pady=10)
        
        # Label para mostrar status das operações
        self.status_label = tk.Label(self.main_frame, text="Aguardando ação...")
        self.status_label.pack(pady=10)
        
        # Rodapé da aplicação
        footer = tk.Label(self.main_frame, text="Powered by Python - Suporte HTML", fg="gray", 
                         font=("Arial", 8))
        footer.pack(side=tk.BOTTOM, pady=5)

    def inserir_exemplo_basico(self):
        """Insere um exemplo básico de email HTML"""
        exemplo_html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; color: #333; }
        .container { max-width: 600px; margin: 0 auto; padding: 20px; }
        .header { background: #007bff; color: white; padding: 20px; text-align: center; }
        .content { padding: 20px; background: #f8f9fa; }
        .button { background: #28a745; color: white; padding: 12px 24px; 
                 text-decoration: none; border-radius: 5px; display: inline-block; }
        .footer { text-align: center; padding: 20px; color: #666; font-size: 12px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Título do Email</h1>
        </div>
        <div class="content">
            <h2>Olá, [Nome]!</h2>
            <p>Este é um exemplo de email em HTML.</p>
            <p>Você pode usar <strong>negrito</strong>, <em>itálico</em> e outros estilos.</p>
            <a href="#" class="button">Clique Aqui</a>
        </div>
        <div class="footer">
            <p>&copy; 2024 Sua Empresa. Todos os direitos reservados.</p>
        </div>
    </div>
</body>
</html>"""
        
        self.conteudo_text.delete("1.0", tk.END)
        self.conteudo_text.insert("1.0", exemplo_html)

    def inserir_exemplo_marketing(self):
        """Insere um exemplo de email de marketing"""
        exemplo_html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin: 0; padding: 0; }
        .container { max-width: 600px; margin: 0 auto; background: #ffffff; }
        .promo-header { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                       color: white; padding: 30px; text-align: center; }
        .content { padding: 30px; }
        .promo-button { background: #ff6b6b; color: white; padding: 15px 30px; 
                       text-decoration: none; border-radius: 25px; font-weight: bold; }
        .feature { margin: 20px 0; padding: 15px; background: #f8f9fa; border-radius: 8px; }
        .social-links { text-align: center; padding: 20px; }
    </style>
</head>
<body>
    <div class="container">
        <div class="promo-header">
            <h1>🎉 Oferta Especial!</h1>
            <p>Desconto de 30% em todos os produtos</p>
        </div>
        <div class="content">
            <h2>Não perca esta oportunidade!</h2>
            <p>Aproveite nossa promoção por tempo limitado.</p>
            
            <div class="feature">
                <h3>⭐ Vantagens:</h3>
                <ul>
                    <li>Produtos de alta qualidade</li>
                    <li>Entrega rápida</li>
                    <li>Suporte 24/7</li>
                </ul>
            </div>
            
            <div style="text-align: center; margin: 30px 0;">
                <a href="#" class="promo-button">Quero o Desconto!</a>
            </div>
        </div>
    </div>
</body>
</html>"""
        
        self.conteudo_text.delete("1.0", tk.END)
        self.conteudo_text.insert("1.0", exemplo_html)

    def inserir_exemplo_newsletter(self):
        """Insere um exemplo de newsletter"""
        exemplo_html = """<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <style>
        body { font-family: Arial, sans-serif; line-height: 1.6; margin: 0; padding: 0; }
        .newsletter { max-width: 600px; margin: 0 auto; border: 1px solid #ddd; }
        .header { background: #343a40; color: white; padding: 20px; text-align: center; }
        .article { padding: 20px; border-bottom: 1px solid #eee; }
        .read-more { color: #007bff; text-decoration: none; font-weight: bold; }
    </style>
</head>
<body>
    <div class="newsletter">
        <div class="header">
            <h1>📰 Nossa Newsletter</h1>
            <p>Edição de Dezembro 2024</p>
        </div>
        
        <div class="article">
            <h2>Novidades da Empresa</h2>
            <p>Confira as últimas atualizações e melhorias...</p>
            <a href="#" class="read-more">Ler mais →</a>
        </div>
        
        <div class="article">
            <h2>Dicas e Tutoriais</h2>
            <p>Aprenda a aproveitar ao máximo nossos produtos...</p>
            <a href="#" class="read-more">Ler mais →</a>
        </div>
        
        <div class="article">
            <h2>Eventos Próximos</h2>
            <p>Participe dos nossos próximos webinars e treinamentos...</p>
            <a href="#" class="read-more">Ler mais →</a>
        </div>
    </div>
</body>
</html>"""
        
        self.conteudo_text.delete("1.0", tk.END)
        self.conteudo_text.insert("1.0", exemplo_html)

    def save_credentials(self):
        """
        Valida e salva as credenciais de email fornecidas
        Avança para a tela principal se as credenciais forem válidas
        """
        self.email_remetente = self.email_entry.get()
        self.senha = self.password_entry.get()
        
        # Valida se todos os campos foram preenchidos
        if not all([self.email_remetente, self.senha]):
            messagebox.showerror("Erro", "Por favor, preencha todos os campos!")
            return
        
        # Validação básica de formato de email
        if "@" not in self.email_remetente or "." not in self.email_remetente:
            messagebox.showerror("Erro", "Por favor, insira um email válido!")
            return
        
        # Transição para a tela principal
        self.credentials_frame.pack_forget()
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        messagebox.showinfo("Sucesso", "Credenciais salvas com sucesso!")

    def enviar_email(self, destinatarios):
        """
        Envia email para múltiplos destinatários usando SMTP
        
        Args:
            destinatarios: Lista de emails dos destinatários
            
        Returns:
            bool: True se o envio foi bem-sucedido, False caso contrário
        """
        try:
            # Coleta dados dos campos da interface
            self.nome_remetente = self.nome_remetente_entry.get()
            self.conteudo_email = self.conteudo_text.get("1.0", tk.END).strip()
            assunto = self.assunto_entry.get()
            
            # Validações dos campos obrigatórios
            if not self.nome_remetente:
                messagebox.showerror("Erro", "Por favor, insira o nome do remetente!")
                return False
                
            if not assunto:
                messagebox.showerror("Erro", "Por favor, insira o assunto do email!")
                return False
                
            if not self.conteudo_email:
                messagebox.showerror("Erro", "Por favor, insira o conteúdo do email!")
                return False
            
            # Configuração da mensagem de email
            msg = MIMEMultipart()
            msg["From"] = f"{self.nome_remetente} <{self.email_remetente}>"
            msg["To"] = self.email_remetente  # Remetente como destinatário visível
            msg["Subject"] = assunto
            
            # Decide se usa HTML ou texto puro
            if self.usar_html.get():
                # Envia como HTML
                msg.attach(MIMEText(self.conteudo_email, "html"))
            else:
                # Envia como texto puro
                msg.attach(MIMEText(self.conteudo_email, "plain"))
            
            # Conexão e envio via servidor SMTP do Gmail
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Habilita criptografia
                server.login(self.email_remetente, self.senha)
                
                # Envia para todos os destinatários (incluindo remetente como BCC)
                server.sendmail(
                    self.email_remetente,
                    [self.email_remetente] + destinatarios,
                    msg.as_string()
                )
            
            return True
            
        except smtplib.SMTPAuthenticationError:
            # Erro de autenticação - credenciais inválidas
            messagebox.showerror("Erro", "Falha na autenticação. Verifique seu email e senha.")
            self.root.destroy()
            return False
        except Exception as e:
            # Erro genérico no envio
            messagebox.showerror("Erro", f"Falha ao enviar emails:\n{str(e)}")
            return False

    def iniciar_envio(self):
        """
        Inicia o processo de envio em uma thread separada
        para não travar a interface gráfica
        """
        if not self.emails_carregados:
            messagebox.showwarning("Aviso", "Nenhum email carregado.")
            return
            
        # Cria e inicia thread para envio assíncrono
        threading.Thread(target=self.processar_emails, daemon=True).start()

    def processar_emails(self):
        """
        Processa o envio dos emails e atualiza o status
        Executado em thread separada
        """
        # Atualiza interface para mostrar progresso
        self.status_label.config(text="Enviando emails...")
        self.root.update_idletasks()
        
        # Executa envio e mostra resultado
        if self.enviar_email(self.emails_carregados):
            messagebox.showinfo("Sucesso", 
                              f"Emails enviados para {len(self.emails_carregados)} destinatários!")
        
        # Atualiza status final
        self.status_label.config(text="Envio concluído!")

    def carregar_arquivo(self):
        """
        Carrega lista de emails a partir de arquivo .txt
        Valida e filtra emails no formato correto
        """
        arquivo_path = filedialog.askopenfilename(
            filetypes=[("Arquivos de Texto", "*.txt")]
        )
        
        if arquivo_path:
            try:
                # Lê e processa o arquivo
                with open(arquivo_path, "r", encoding="utf-8") as file:
                    # Filtra linhas válidas (não vazias e com @)
                    self.emails_carregados = [
                        linha.strip() for linha in file 
                        if linha.strip() and "@" in linha
                    ]
                
                # Verifica se encontrou emails válidos
                if not self.emails_carregados:
                    messagebox.showwarning("Aviso", "Nenhum email válido encontrado no arquivo.")
                    return
                
                # Feedback de sucesso e habilita botão de envio
                messagebox.showinfo("Sucesso", 
                                  f"{len(self.emails_carregados)} emails válidos carregados!")
                self.status_label.config(text=f"{len(self.emails_carregados)} emails prontos para envio.")
                self.btn_enviar.config(state=tk.NORMAL)
            
            except Exception as e:
                # Erro ao ler arquivo
                messagebox.showerror("Erro", f"Não foi possível abrir o arquivo:\n{str(e)}")

# Ponto de entrada da aplicação
if __name__ == "__main__":
    """
    Inicializa e executa a aplicação
    """
    root = tk.Tk()
    app = EmailSenderApp(root)
    root.mainloop()
