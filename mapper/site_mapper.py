class SiteMapper:
    @classmethod
    def mapear_site(cls, url, nome, **dados):
        site = {'nome': nome,
                'url': url}
        return site
