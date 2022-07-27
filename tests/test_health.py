def test_health_check(client, database):
    """
    Ensure that the health check returns a successful status code
    """
    response = client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.get_data(as_text=True) == "Ok"