from django.urls import path
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # path('snippets/', views.snippet_list),
    # path('snippets/<int:pk>', views.snippet_detail)
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view(), name="users"),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user')

]

format_suffix_patterns(urlpatterns)
