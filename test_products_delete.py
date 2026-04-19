def test_delete_product(api):
    session, base_url = api

    response = session.delete(f"{base_url}/products/1")
    assert response.status_code == 200

    product = response.json()
    assert product["id"] == 1
