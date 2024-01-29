class FiltroHotel:
    @staticmethod
    def normalize_path_params(cidade=None, **dados):
        if cidade:
            return {
                'cidade': cidade
            }

    @staticmethod
    def normalize_filter_offset(offset=None, **dados):
        if offset:
            return offset
        return 0

    @staticmethod
    def normalize_filter_limit(limit=None, **dado):
        if limit:
            return limit
        return 10
