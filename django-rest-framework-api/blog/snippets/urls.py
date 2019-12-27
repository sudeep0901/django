from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>', views.snippet_detail)
    # path('', views.api_root),
    # path('snippets/', views.SnippetList.as_view()),
    # path('snippets/<int:pk>', views.SnippetDetail.as_view()),
    # path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view()),
    # path('users/', views.UserList.as_view(), name="users"),
    # path('users/<int:pk>', views.UserDetail.as_view(), name='user')

    path('', views.api_root),
    path('snippets/', views.SnippetList.as_view(),name='snippet-list'),
    path('snippets/<int:pk>', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight', views.SnippetHighlight.as_view(), name='snippet_highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user-detail')
]

format_suffix_patterns(urlpatterns)
