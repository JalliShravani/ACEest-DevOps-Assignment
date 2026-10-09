from app import app


# Create a test client
def get_test_client():
    return app.test_client()


# Test the home endpoint
def test_home():
    client = get_test_client()

    response = client.get("/")

    assert response.status_code == 200

    data = response.get_json()

    assert data["application"] == "ACEest Fitness & Gym"
    assert data["status"] == "running"


# Test the health endpoint
def test_health():
    client = get_test_client()

    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "healthy"


# Test getting clients
def test_get_clients():
    client = get_test_client()

    response = client.get("/clients")

    assert response.status_code == 200

    assert response.get_json() == []


# Test adding a client
def test_add_client():
    client = get_test_client()

    client_data = {
        "name": "Test User",
        "age": 25,
        "weight": 60
    }

    response = client.post("/clients", json=client_data)

    assert response.status_code == 201

    data = response.get_json()

    assert data["name"] == "Test User"
    assert data["age"] == 25
    assert data["weight"] == 60


# Test missing required field
def test_add_client_missing_field():
    client = get_test_client()

    client_data = {
        "name": "Test User",
        "age": 25
    }

    response = client.post("/clients", json=client_data)

    assert response.status_code == 400

    data = response.get_json()

    assert "error" in data
