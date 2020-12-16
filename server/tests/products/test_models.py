import pytest
from products.models import Product

@pytest.mark.django_db
def test_products_model():
    product = Product(naziv="Test Product", kategorija="test", godina=1987)
    product.save()

    assert product.naziv == "Test Product"
    assert product.kategorija == "test"
    assert product.godina == 1987
    assert product.created_at
    assert product.updated_at
    assert str(product) == product.naziv