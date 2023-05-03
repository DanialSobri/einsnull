from fastapi.testclient import TestClient
from config import settings
from student.endpoints import router

client = TestClient(router)

def test_get_students():
    response = client.get("{}/student/all".format(settings.API_V1_STR), headers={"X-Token": "coneofsilence"})
    print(response)
    assert response.status_code == 200
    # assert response.json() == {
    #     "id": "foo",
    #     "title": "Foo",
    # }