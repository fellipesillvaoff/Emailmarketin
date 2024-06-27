import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from jinja2 import Environment, FileSystemLoader
import os

def enviar_email(nome, oferta,email_para,assunto):
    email_de = 'site@clubedoeletronico.com'  # Seu endereço de e-mail
    senha = 'Mestrado2020/'  # Sua senha de e-mail
    #email_para = input('Digite o e-mail completo: ')  # E-mail do destinatário
    #assunto = f'Atualização pedido {nota}'  # Assunto do e-mail

    # Carregar o modelo HTML
    file_loader = FileSystemLoader(os.path.join(os.path.dirname(__file__), 'template'))
    env = Environment(loader=file_loader)
    template = env.get_template('padraohtml.html')

    # Criação do corpo do e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = email_de
    mensagem['To'] = email_para
    mensagem['Subject'] = assunto

    # Renderizar o modelo
    template_vars = {"name": nome, 'code': oferta}  # Variáveis para o modelo
    html_message = template.render(template_vars)

    # Anexar a mensagem HTML ao corpo do e-mail
    mensagem.attach(MIMEText(html_message, 'html'))

    # Enviar o e-mail
    servidor_smtp = None
    try:
        # Configuração do servidor SMTP
        servidor_smtp = smtplib.SMTP('smtp.hostinger.com', 587)  # Altere para as configurações do seu servidor SMTP
        servidor_smtp.starttls()
        servidor_smtp.login(email_de, senha)

        # Enviar o e-mail
        servidor_smtp.send_message(mensagem)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('Ocorreu um erro ao enviar o e-mail:', str(e))
    finally:
        # Encerrar a conexão com o servidor SMTP
        if servidor_smtp:
            servidor_smtp.quit()

    return

dados = {
    "contatos": ['felipe', 'kat'],
    "ofertas": ['code101', 'code102'],
    "emails": ['fellipesillvaoff@gmail.com', 'contatos']
}

for i in range(len(dados["contatos"])):
    nome = dados["contatos"][i]
    oferta = dados["ofertas"][i]
    email = dados["emails"][i]
    assunto = f'{nome} você recebeu um pix'

    enviar_email(nome, oferta, email, assunto)