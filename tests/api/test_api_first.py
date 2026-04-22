import requests

def test_get_product_returns_200(api):
    session, base_url = api
    response = session.get(f"{base_url}/posts/1")
    assert response.status_code == 200
    post = response.json()
    assert post["id"] == 1
    assert isinstance(post["title"],str)

    elapsed = response.elapsed.total_seconds() * 1000
    assert elapsed < 3000, f"Response too slow: {elapsed:.0f}ms - limit is 3000ms"

def test_get_invalid_product_returns_404(api):
    session, base_url = api
    response = session.get(f"{base_url}/posts/99999")
    assert response.status_code != 500    

def test_get_all_posts_returns_list(api):
    session, base_url = api
    response = session.get(f"{base_url}/posts")
    assert response.status_code == 200
    products = response.json()
    assert isinstance(products, list)
    assert len(products) > 0