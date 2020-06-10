from django.urls import path

from . import views

app_name = 'ecommerce'

urlpatterns = [
    path("", views.InicioView.as_view(), name="index"),
    path("producto/<slug>/", views.ItemDetailView.as_view(), name="producto"),
    path("checkout/", views.checkout, name="checkout"),
    path("resumen-compra/", views.OrderSummaryView.as_view(), name="resumen-compra"),
    path("add-to-cart/<slug>/", views.add_to_cart, name="add-to-cart"),
    path("remove-from-cart/<slug>/", views.remove_from_cart, name="remove-from-cart"),
    path("remove-item-from-cart/<slug>/", views.remove_single_item_from_cart, name="remove-single-item-from-cart")
]
