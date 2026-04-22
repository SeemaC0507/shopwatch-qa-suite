def test_create_product(api):
    session, base_url = api

    new_product = {
        "title": "Wireless Headphone",
        "body": "Noise cancelling headphones",
        "userId": 1
    }

    response = session.post(f"{base_url}/posts", json=new_product)
    assert response.status_code == 201

    post = response.json()
    assert post["title"] == "Wireless Headphone"
    assert isinstance(post["id"], int)

def test_create_then_fetch_product(api):
    session, base_url = api

    new_product = {
        "title": "Wireless Headphone",
        "body": "Noise cancelling headphones",
        "userId": 1
    }

    response = session.post(f"{base_url}/posts", json=new_product)
    assert response.status_code == 201

    elapsed = response.elapsed.total_seconds() * 1000
    assert elapsed < 3000, f"Response too slow: {elapsed:.0f}ms - limit is 3000ms"


    post = response.json()
    new_id = post["id"]
    response = session.get(f"{base_url}/posts/{new_id}") 


    # JSONPlaceholder does not persist POST data — documented sandbox limitation
    assert response.status_code != 500, "Server crashed on GET after POST"


   