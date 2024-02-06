from enuns import Enum


class MessagensEnumUsuario(Enum):
    ERRO_DELECAO_USUARIO = "Ocorreu um erro ao deletar o usuário {}."
    ERRO_USUARIO_NOT_FOUND = 'Usuario não existe.'
    USUARIO_DELETADO_COM_SUCESSO = 'Usuário {} deletado com sucesso!'
    OCORREU_UM_ERRO_AO_SALVAR_USUARIO = 'Ocorreu um erro para salvar o usuário'
    USUARIO_CRIADO_COM_SUCESSO = 'Usuário {} criado com sucesso!'
    USUARIO_COM_LOGIN_JA_EXISTE = 'Usuário com o login {} já existe'
    USUARIO_LOGADO_COM_SUCESSO = 'Usuario Logado com SUCESSO!'
    SENHA_INCORRETA = 'Senha INCORRETA, tente novamente'
    USUARIO_E_SENHA_INCORRETO = 'Usuario e senha incoretos!'
    HOTEL_NOT_FOUND = 'Hotel not found.'
    MENSAGEM_PARANS_LOGIN = 'O campo login tem que ser passado.'
    MENSAGEM_PARANS_SENHA = 'O campo senha tem que ser passado.'
    TOKEN_REVOGADO = "Token has been revoked"


class MessagensEnumHotel(Enum):
    HOTEL_TOKEN_EXPIRADO = 'Token Expirado.'
    MENSAGEM_PARANS_SITE = 'Site não enviado'
    HOTEL_NOT_FOUND = 'Hotel not found.'
    HOTEL_COM_NAO_PODE_NULO = 'O campo hotel_id não pode ser nulo.'
    HOTEL_EXISTE_NA_BASE_DE_DADO = 'Hotel já existe na base de dados.'
    HOTEL_OCOREU_ERRO_GRAVAR_INFORMACAO = 'Ocoreu um erro ao gravar informação.'
    HOTEL_ADICIONADO_COM_SUCESSO = 'Hotel adicionado com sucesso.'
    HOTEL_ERRO_DELETAR_INFORMACAO = 'Occoreu um erro ao deletar a informação.'
    HOTEL_REMOVIDO_COM_SUCESSO = 'Hotel removido com sucesso.'
    HOTEL_SOLICITACAO_SEM_CONTEUDO = 'Solicitação não retornou conteúdo.'
    MENSAGEM_PARANS_NOME = "O campo 'nome' tem que ser enviado"
    MENSAGEM_PARANS_ESTRELAS = "O campo 'estrelas' tem que ser enviado"
    MENSAGEM_PARANS_DIARIA = "O campo 'diaria' tem que ser enviado"
    MENSAGEM_PARANS_CIDADE = "O campo 'cidade' tem que ser enviado"


class MessagensEnumSites(Enum):
    MENSAGEM_PARANS_HOTEL = "O campo 'hotel' tem que ser enviado"
    ERRO_AO_CONSULTAR_NO_BANCO = "Erro ao consultar as informações no banco de dados."
    SITE_ERRO_ENVIAR_PARAMETROS = "Dados não foi enviado para salvar o site."
    SITES_NAO_ENCONTRATOS = 'Não existe nenhum site na base de dados.'
    MENSAGEM_PARANS_URL = "O Campo 'url' tem que ser enviado."
    MENSAGEM_PARANS_NOME = "O Campo 'nome tem que ser enviado."
    SITE_ERRO_AO_SALVAR_SITE = "Erro ao salvar site."
    SITE_DELETADO_COM_SUCESSO = 'Site deletado com sucesso.'
    SITE_OCORREU_UM_ERRO_DELETAR = 'Ocorreu um erro ao deletar site.'
    SITE_NAO_ENCONTRATO_PARA_DELETAR = 'Site não foi encontrato para ser deletado.'
    SITE_JA_EXISTE_NA_BASE_DE_DADOS = 'O site já existe na base de dados.'
