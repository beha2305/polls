from django.urls import path

from .views import response, ans

urlpatterns = [
    path("", response),
    path("ans/<int:question_id>",ans),
    # path("<int:question_id>/results/",results),
    # path("<int:question_id>/vote/",vote),
]