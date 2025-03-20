from django.urls import path

from . import views

app_name = "polls" # adds a namespace to the app for better url routing when multiple apps are involved
urlpatterns = [
	path("", views.index, name="index"),
	path("<int:question_id>/", views.detail, name="detail"),
	path("<int:question_id>/results/", views.results, name="results"),
	path("<int:question_id>/vote/", views.vote, name="vote"),
]