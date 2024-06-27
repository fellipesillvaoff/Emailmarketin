import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def enviar_email(nota, rastreio, situacao):
    email_de = 'site@clubedoeletronico.com'  # E-mail remetente
    senha = 'Mestrado2020*'  # Senha do e-mail remetente
    email_para = input('Digite o e-mail completo: ')
    assunto = f'Atualização pedido {nota}'  # Assunto do e-mail
    corpo = f'Temos boas noticias! O pedido da Nota Fiscal {nota} teve o rastreio {rastreio} atualizado para {situacao}. Consulte detalhes em nosso site O Clube entregas. https://cluberastreio.up.railway.app'

    # Criação do corpo do e-mail
    mensagem = MIMEMultipart()
    mensagem['From'] = email_de
    mensagem['To'] = email_para+",atendimentoclubedoeletronico@gmail.com"
    mensagem['Subject'] = assunto

    # Adiciona o conteúdo do e-mail com a data e hora atual
    texto = corpo
    conteudo = MIMEText(texto, 'plain')
    mensagem.attach(conteudo)

    # Envio do e-mail
    servidor_smtp = None
    try:
        # Configuração do servidor SMTP
        servidor_smtp = smtplib.SMTP('smtp.hostinger.com', 587)  # Altere para as configurações do seu servidor SMTP
        servidor_smtp.starttls()
        servidor_smtp.login(email_de, senha)

        # Envio do e-mail
        servidor_smtp.send_message(mensagem)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('Ocorreu um erro ao enviar o e-mail:', str(e))
    finally:
        # Encerra a conexão com o servidor SMTP
        if servidor_smtp:
            servidor_smtp.quit()

    return