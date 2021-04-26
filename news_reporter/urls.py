from django.urls import path
from  .views import HomeView,NewsListView, NewsDetailsView, NewsCreateView,NewsUpdateView,NewsDeleteView,CommentView

urlpatterns = [
    path('news_report/<int:pk>/comment/', CommentView.as_view(), name="news-comment"),
    path('news_report/<int:pk>/delete/', NewsDeleteView.as_view(), name='news-delete'),
    path('news_report/<int:pk>/edit/', NewsUpdateView.as_view(), name='news-update'),
    path('news_report/create/', NewsCreateView.as_view(), name='news-create'),
    path('news_report/<int:pk>/', NewsDetailsView.as_view(), name='news-detail'),
    path('news_report', NewsListView.as_view(), name='news-home'),
    path ('', HomeView.as_view(), name='home')
    ]
