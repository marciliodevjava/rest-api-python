class FiltroHotel:
    @staticmethod
    def normalize_path_params(cidade=None, **dados):
        if cidade:
            return {
                'cidade': cidade
            }
