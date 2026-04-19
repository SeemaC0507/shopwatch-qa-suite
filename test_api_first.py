import requests

# def test_get_product_returns_200():
#     response = requests.get("https://fakestoreapi.com/products/1")
#     assert response.status_code == 200
#     product = response.json()
#     assert product["id"] == 1
#     assert isinstance(product["title"], str)

# def test_get_invalid_product_returns_404():
#     response = requests.get("https://fakestoreapi.com/products/99999")
#     assert response.status_code != 500

def test_get_product_returns_200(api):
    session, base_url = api
    response = session.get(f"{base_url}/products/1")
    assert response.status_code == 200
    product = response.json()
    assert product["id"] == 1
    assert isinstance(product["title"],str)

def test_get_invalid_product_returns_404(api):
    session, base_url = api
    response = session.get(f"{base_url}/products/99999")
    assert response.status_code != 500    

def test_get_all_products_returns_list(api):
    session, base_url = api
    response = session.get(f"{base_url}/products")
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)
    assert len(products) > 0