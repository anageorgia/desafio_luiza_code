from .views import CadastrarProduto
from django.urls import path
from.import views


urlpatterns = [

    path('', views.index, name='luMarketplace-index'),

    path('cadastrar-prod/', CadastrarProduto.as_view(),
         name='luMarketplace-cadastro'),

    path('atualizar-prod/<int:id>', views.luMarketplace_atualizar,
         name='luMarketplace-atualizar'),


    path('luMarketplace_inativar/<id_prod>',
         views.luMarketplace_inativar, name='luMarketplace-inativar'),

    path('luMarketplace_ativar/<id_prod>',
         views.luMarketplace_ativar, name='luMarketplace-ativar'),

    path('luMarketplace_deletar/<id_prod>', views.luMarketplace_deletar, name='luMarketplace-deletar'),

    path('login/', views.login_user),

    path('login/submit', views.submit_login),

    path('logout/', views.logout_user),

    path('area_do_vendedor/', views.index_logado),

]
