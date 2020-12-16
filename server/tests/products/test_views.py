import pytest
from products.models import Product
@pytest.mark.django_db
def test_add_product(client):
    products = Product.objects.all()
    assert len(products) == 0

    resp = client.post(
        "/api/products/",
        {
            "naziv": "Product 1",
            "kategorija": "test",
            "godina": 1998,
        },
        content_type="application/json"
    )
    assert resp.status_code == 201
    assert resp.data["naziv"] == "Product 1"

    products = Product.objects.all()
    assert len(products) == 1

@pytest.mark.django_db
def test_add_product_invalid_json(client):
    products = Product.objects.all()
    assert len(products) == 0

    resp = client.post(
        "/api/products/",
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

    products = Product.objects.all()
    assert len(products) == 0

@pytest.mark.django_db
def test_edit_product_success(client):
    p = Product(naziv="Product 2", kategorija="test", godina=2000)
    p.save()
    assert p is not None
    resp = client.put(
        f'/api/products/{p.id}/',
        {
            "naziv": "Changed Title",
            "kategorija": p.kategorija,
            "godina": p.godina
        },
        content_type="application/json"
    )

    print(p.id)
    assert resp.status_code == 200
    assert resp.data['naziv'] == 'Changed Title'

@pytest.mark.django_db
def test_edit_product_fail(client):
    p = Product(naziv="Product 2", kategorija="test", godina=2000)
    p.save()
    resp = client.put(
        f'/api/products/{p.id}/',
        {},
        content_type="application/json"
    )
    assert resp.status_code == 400

@pytest.mark.django_db
def test_delete_product_fail(client):
    p = Product(naziv="Product 2", kategorija="test", godina=2000)
    p.save()

    resp = client.delete(
        f'/api/products/{p.id}/'
    )
    assert resp.status_code == 204