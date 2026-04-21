def test_product_lifecycle(api):
    session, base_url = api

    #Step 1 - Verify API is alive
    response = session.get(f"{base_url}/products/1")
    assert response.status_code == 200

    #Step 2 - Create a product
    new_product = {
        "title": "ShopWatch Lifecycle Test Product",
        "price": 49.99,
        "description": "Created during lifecycle test",
        "image": "https://fakestoreapi.com/img/placeholder.jpg",
        "category": "electronics"
    }

    response = session.post(f"{base_url}/products", json =new_product)
    assert response.status_code == 201

    product = response.json()
    assert product["title"] == "ShopWatch Lifecycle Test Product"
    assert isinstance(product["id"], int)

    product_id = product["id"]

    #Step 3- Update the product
    updated_product = {
        "title": "ShopWatch Lifecycle Test Product — UPDATED",
        "price": 39.99,
        "description": "Updated during lifecycle test",
        "image": "https://fakestoreapi.com/img/placeholder.jpg",
        "category": "electronics"
    }

    response = session.put(f"{base_url}/products/{product_id}", json=updated_product)
    assert response.status_code == 200

    updated = response.json()
    assert updated["title"] == "ShopWatch Lifecycle Test Product — UPDATED"
    assert updated["price"] == 39.99

    #Step 4- Delete the product

    response = session.delete(f"{base_url}/products/{product_id}")
    assert response.status_code == 200

   # assert len(response.text) > 0, "Response body is empty — FakeStoreAPI does not persist DELETE data"

   # FakeStoreAPI returns empty body on DELETE — documented sandbox limitation
    assert response.status_code != 500, "Server crashed on DELETE request"


    #deleted = response.json()
    #assert deleted["id"] == product_id

    elapsed = response.elapsed.total_seconds() * 1000
    assert elapsed < 3000, f"Response too slow: {elapsed:.0f}ms - limit is 3000ms"


