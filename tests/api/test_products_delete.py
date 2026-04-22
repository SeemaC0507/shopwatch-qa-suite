def test_delete_product(api):
    session, base_url = api

    response = session.delete(f"{base_url}/posts/1")
    assert response.status_code == 200

    elapsed = response.elapsed.total_seconds() * 1000
    assert elapsed < 3000, f"Response too slow: {elapsed:.0f}ms - limit is 3000ms"


    # JSONPlaceholder returns empty body on DELETE — documented sandbox limitation
    assert response.status_code != 500, "Server crashed on DELETE request"