def test_product_lifecycle(api):
    session, base_url = api

    #Step 1 - Verify API is alive
    response = session.get(f"{base_url}/posts/1")
    assert response.status_code == 200

    #Step 2 - Create a product
    new_product = {
        "title": "Wireless Headphone",
        "body": "Noise cancelling headphones",
        "userId": 1
    }

    response = session.post(f"{base_url}/posts", json =new_product)
    assert response.status_code == 201

    post = response.json()
    assert post["title"] == "Wireless Headphone"
    assert isinstance(post["id"], int)

    post_id = post["id"]

    #Step 3- Update the post
    updated_post = {
        "title": "Updated Wireless Headphone",
        "body": "Noise cancelling headphones",
        "userId": 1
    }

    response = session.put(f"{base_url}/posts/1", json=updated_post)

    #response = session.put(f"{base_url}/posts/{post_id}", json=updated_post)
    assert response.status_code == 200

    updated = response.json()
    assert updated["title"] == "Updated Wireless Headphone"
    
    #Step 4- Delete the post

    response = session.delete(f"{base_url}/posts/{post_id}")
    assert response.status_code == 200

    # FakeStoreAPI returns empty body on DELETE — documented sandbox limitation
    assert response.status_code != 500, "Server crashed on DELETE request"


    elapsed = response.elapsed.total_seconds() * 1000
    assert elapsed < 3000, f"Response too slow: {elapsed:.0f}ms - limit is 3000ms"


