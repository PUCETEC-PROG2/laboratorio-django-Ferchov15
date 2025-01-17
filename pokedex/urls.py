from django.urls import path

from . import views

app_name = 'pokedex'

urlpatterns = [
    path("", views.index, name="index"),
    path("trainers/", views.trainers, name="trainers"),
    path("pokemon/<int:pokemon_id>/", views.pokemon, name="pokemon"),
    path("trainers/trainer/<int:trainer_id>/", views.trainer, name="trainer"),
    path("add_pokemon/", views.add_pokemon, name="add_pokemon"),
    path("add_trainer/", views.add_trainer, name="add_trainer"),
    path("edit_pokemon/<int:pokemon_id>/", views.edit_pokemon, name="edit_pokemon"),
    path("trainers/edit_trainer/<int:trainer_id>/", views.edit_trainer, name="edit_trainer"),
    path("delet_pokemon/<int:pokemon_id>/", views.delet_pokemon, name="delet_pokemon"),
    path("trainers/delet_trainer/<int:trainer_id>/", views.delet_trainer, name="delet_trainer"),
    path("login/", views.CustomLoginView.as_view(), name="login")
]