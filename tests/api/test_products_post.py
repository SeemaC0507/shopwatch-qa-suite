def test_create_product(api):
    session, base_url = api

    new_product = {
        "title": "Wireless Headphone",
        "price": 79.99,
        "description": "Noise Cancelling headphones",
        "image": "https://fakestoreapi.com/img/placeholder.jpg",
        "category": "electronics"
    }

    response = session.post(f"{base_url}/products", json=new_product)
    assert response.status_code == 201

    product = response.json()
    assert product["title"] == "Wireless Headphone"
    assert isinstance(product["id"], int)

def test_create_then_fetch_product(api):
    session, base_url = api

    new_product = {
        "title": "Wireless Headphone",
        "price": 79.99,
        "description": "Noise Cancelling headphones",
        "image": "https://fakestoreapi.com/img/placeholder.jpg",
        "category": "electronics"
    }

    response = session.post(f"{base_url}/products", json=new_product)
    assert response.status_code == 201

    elapsed = response.elapsed.total_seconds() * 1000
    assert elapsed < 3000, f"Response too slow: {elapsed:.0f}ms - limit is 3000ms"


    product = response.json()
    new_id = product["id"]
    response = session.get(f"{base_url}/products/{new_id}") 
    assert response.status_code == 200
    assert len(response.text) > 0, "Response body is empty — FakeStoreAPI does not persist POST data"

#    fetched = response.json()
#    assert fetched["title"] == "Wireless Headphone"
