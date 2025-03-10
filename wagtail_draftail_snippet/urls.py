from django.urls import path
from django.conf.urls import url

from wagtail.snippets.views import chooser

from .views import choose_snippet_link_model, choose_snippet_embed_model


app_name = "wagtaildraftailsnippet"

urlpatterns = [
    url(
        r"^choose-link-model/$",
        choose_snippet_link_model,
        name="choose-snippet-link-model",
    ),
    url(
        r"^choose-embed-model/$",
        choose_snippet_embed_model,
        name="choose-snippet-embed-model",
    ),
    path(
        "choose/", chooser.ChooseView.as_view(), name="choose_generic"
    ),  # This exists only to get the additional URL params added via JS in wagtail-draftail-snippet.js line 50
]
