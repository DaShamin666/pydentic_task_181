import requests
from faker import Faker
from Models import UserRequest
from Models import ResponseModel
from Models import UserResponse
from Models import UpdateUserRequest
from Models import UpdateUserResponse


fake = Faker()

def test_post_user():

    data = {
        "name": fake.name(),
        "job": fake.job(),
    }
    user = UserRequest(**data)
    response = requests.post('https://reqres.in/api/users', json=user.dict())
    assert response.status_code == 201
    user_id = response.json()['id']
    response_data = UserResponse(**response.json())
    assert response_data.id is not None
    assert response_data.name == user.name
    assert response_data.job == user.job
    assert response_data.createdAt is not None
    print(f"Creat User ID: {user_id}")

def test_user():
    response = requests.get(f'https://reqres.in/api/users/2')
    assert response.status_code == 200
    assert isinstance(response.json()['data']['email'], str)
    assert isinstance(response.json()['data']['first_name'], str)
    assert isinstance(response.json()['data']['last_name'], str)
    assert isinstance(response.json()['data']['avatar'], str)
    assert response.json()["data"]['id'] == 2
    print(ResponseModel(**response.json()))


def test_update_user():

    new_user_update = UpdateUserRequest(
        name=fake.name(),
        job=fake.job()
    )
    response = requests.patch(url=f'https://reqres.in/api/users/2', json=new_user_update.dict())
    assert response.status_code == 200
    response_data = UpdateUserResponse(**response.json())
    assert response_data.name == new_user_update.name
    assert response_data.job == new_user_update.job
    print(response_data)

def test_delete_user():
    response = requests.delete(f'https://reqres.in/api/users/2')
    assert response.status_code == 204
    response_2 =requests.get(f'https://reqres.in/api/users/2')
    assert response_2.status_code == 404 # тестовая апи мы не можем удалить юзера этого , своего
    # пользователя создать тоже не можем чтобы удалить его по айди,поэтому тест фейлится