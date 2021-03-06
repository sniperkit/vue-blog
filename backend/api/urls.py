from django.conf.urls import url
from .views import article, article_detail, comment, tag, UserLoginAPIView,\
    manage, request_user, tag_detail, article_admin, article_detail_admin, tag_admin, change_img,\
    archive_article, view_info, random_article


urlpatterns = [
    url(r'^api/articles/$', article),
    url(r'^api/random_articles/$', random_article),
    url(r'^api/articles_admin/$', article_admin),
    url(r'^api/article/(?P<article_id>\d+)/$', article_detail),
    url(r'^api/article_admin/(?P<article_id>\d+)/$', article_detail_admin),
    url(r'^api/comments/$', comment),
    url(r'^api/tags/$', tag),
    url(r'^api/tags_admin/$', tag_admin),
    url(r'^api/tag/(?P<tag_id>\d+)/$', tag_detail),
    url(r'^api/login/$', UserLoginAPIView.as_view()),
    url(r'^api/manage/$', manage),
    url(r'^api/request_user/$', request_user),
    url(r'^api/change_img/$', change_img),
    url(r'^api/archive_articles/$', archive_article),
    url(r'^api/view_num/$', view_info),
]
