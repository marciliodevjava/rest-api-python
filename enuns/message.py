from enuns import Enum


class MessagensEnumUsuario(Enum):
    ERRO_DELECAO_USUARIO = "Ocorreu um erro ao deletar o usuário {}."
    ERRO_USUARIO_NOT_FOUND = 'Usuario não existe.'
    USUARIO_DELETADO_COM_SUCESSO = 'Usuário {} deletado com sucesso!'
    OCORREU_UM_ERRO_AO_SALVAR_USUARIO = 'Ocorreu um erro para salvar o usuário'
    USUARIO_CRIADO_COM_SUCESSO = 'Ocorreu um erro para salvar o usuário'
    USUARIO_COM_LOGIN_JA_EXISTE = 'Usuário com o login {} já existe'
    USUARIO_LOGADO_COM_SUCESSO = 'Usuario Logado com SUCESSO!'
    SENHA_INCORRETA = 'Senha INCORRETA, tente novamente'
    USUARIO_E_SENHA_INCORRETO = 'Usuario e senha incoretos!'
    HOTEL_NOT_FOUND = 'Hotel not found.'


class MessagensEnumHotel(Enum):
    HOTEL_NOT_FOUND = 'Hotel not found.'
    HOTEL_COM_NAO_PODE_NULO = 'O campo hotel_id não pode ser nulo.'
    HOTEL_EXISTE_NA_BASE_DE_DADO = 'Hotel já existe na base de dados.'
    HOTEL_OCOREU_ERRO_GRAVAR_INFORMACAO = 'Ocoreu um erro ao gravar informação.'
    HOTEL_ADICIONADO_COM_SUCESSO = 'Hotel adicionado com sucesso.'
    HOTEL_ERRO_DELETAR_INFORMACAO = 'Occoreu um erro ao deletar a informação.'
    HOTEL_REMOVIDO_COM_SUCESSO = 'Hotel removido com sucesso.'
    HOTEL_SOLICITACAO_SEM_CONTEUDO ='Solicitação não retornou conteúdo.'

class MessagensSites(Enum):
    SITES_NAO_ENCONTRATOS = 'Não existe nenhum site na base de dados'
