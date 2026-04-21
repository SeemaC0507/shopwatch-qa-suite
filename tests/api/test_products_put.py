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

    elapsed = response.elapsed.total_seconds() * 1000
    assert elapsed < 3000, f"Response too slow: {elapsed:.0f}ms - limit is 3000ms"


    product = response.json()
    assert product["title"] == "Updated Wireless Headphone"
    assert product["id"] == 1
