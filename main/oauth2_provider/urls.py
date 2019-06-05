from allauth.socialaccount.providers.oauth2.urls import default_urlpatterns
from main.oauth2_provider.provider import OAuth2Provider


urlpatterns = default_urlpatterns(OAuth2Provider)
