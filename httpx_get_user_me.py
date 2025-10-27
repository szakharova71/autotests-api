import httpx  # Импортируем библиотеку HTTPX

# Данные для входа в систему
login_payload = {
    "email": "user1026@example.com",
    "password": "string"
}

# Выполняем запрос на аутентификацию
login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

# Выводим полученные токены
print("Login response:", login_response_data)
print("Status Code:", login_response.status_code)



# Формируем payload для получения данных пользователя
access_token = login_response_data["token"]["accessToken"]


# Выполняем запрос на получение данных пользователя
user_response = httpx.get("http://localhost:8000/api/v1/users/me", headers={"Authorization": f"Bearer {access_token}"})
user_response_data = user_response.json()

# Выводим обновленные токены
print("Get user response:", user_response_data)
print("Status Code:",user_response.status_code)