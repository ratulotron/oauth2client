import logging

import requests
from allauth.socialaccount.providers.oauth2.views import (OAuth2Adapter, OAuth2LoginView, OAuth2CallbackView)
from .provider import OAuth2Provider
from django.conf import settings


class NewOAuth2Adapter(OAuth2Adapter):
    provider_id = OAuth2Provider.id

    # Fetched programmatically, must be reachable from container
    access_token_url = '{}/o/token/'.format(settings.OAUTH_SERVER_BASEURL)
    profile_url = '{}/profile/'.format(settings.OAUTH_SERVER_BASEURL)

    # Accessed by the user browser, must be reachable by the host
    authorize_url = '{}/o/authorize/'.format(settings.OAUTH_SERVER_BASEURL)

    # NOTE: trailing slashes in URLs are important, don't miss it

    def complete_login(self, request, app, token, **kwargs):
        headers = {'Authorization': 'Bearer {0}'.format(token.token)}
        resp = requests.get(self.profile_url, headers=headers)
        extra_data = resp.json()
        return self.get_provider().sociallogin_from_response(request, extra_data)

    def authentication_error(self,
                             request,
                             provider_id,
                             error=None,
                             exception=None,
                             extra_context=None):
        logging.error('Error in social authentication cycle. [Provider: {}]'.format(
            provider_id
        ))

        if exception:
            logging.exception(exception)


oauth2_login = OAuth2LoginView.adapter_view(NewOAuth2Adapter)
oauth2_callback = OAuth2CallbackView.adapter_view(NewOAuth2Adapter)
