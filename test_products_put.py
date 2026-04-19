def test_update_product(api):
    session, base_url = api
    
    updated_product = {
        "title": "Updated Wireless Headphone",
        "price": 59.99,
        "description": "Now with better battery life",
        "image": "https://fakestoreapi.com/img/placeholder.jpg",
        "category": "electronics"
    }

    response = session.put(f"{base_url}/products/1", json=updated_product)
    assert response.status_code == 200

    product = response.json()
    assert product["title"] == "Updated Wireless Headphone"
    assert product["id"] == 1
