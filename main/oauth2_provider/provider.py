from allauth.socialaccount import providers
from allauth.socialaccount.providers.base import ProviderAccount
from allauth.socialaccount.providers.oauth2.provider import OAuth2Provider


class OAuth2Account(ProviderAccount):
    pass


class OAuth2Provider(OAuth2Provider):

    id = 'oauth2provider'
    name = 'My Custom OAuth2 Provider'
    account_class = OAuth2Account

    def extract_uid(self, data):
        return str(data['id'])

    def extract_common_fields(self, data):
        return dict(username=data['username'],
                    email=data['email'],
                    first_name=data['first_name'],
                    last_name=data['last_name'],)

    def get_default_scope(self):
        scope = ['read']
        return scope


providers.registry.register(OAuth2Provider)
