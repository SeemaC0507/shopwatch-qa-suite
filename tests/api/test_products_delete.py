def test_delete_product(api):
    session, base_url = api

    response = session.delete(f"{base_url}/products/1")
    assert response.status_code == 200

    elapsed = response.elapsed.total_seconds() * 1000
    assert elapsed < 3000, f"Response too slow: {elapsed:.0f}ms - limit is 3000ms"


    product = response.json()
    assert product["id"] == 1
