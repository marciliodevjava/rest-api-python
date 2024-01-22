class HotelModel:
    def __init__(self, hotel_id, nome, estrelas, diaria, cidade):
        self.__hotel_id = hotel_id
        self.__nome = nome
        self.__estrelas = estrelas
        self.__diaria = diaria
        self.__cidade = cidade

    def json(self):
        return {
            'hotel_id': self.__hotel_id,
            'nome': self.__nome,
            'estrelas': self.__estrelas,
            'diaria': self.__diaria,
            'cidade': self.__cidade
        }