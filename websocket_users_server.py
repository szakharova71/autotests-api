import asyncio

import websockets
from websockets import ServerConnection


# Обработчик входящих сообщений
async def echo(websocket: ServerConnection):
    async for message in websocket:
        print(f"Получено сообщение от пользователя: {message}")

        for i in range(5): # Отправляем ответ 5 раз
            response = f"{i+1} Сообщение пользователя: {message}"
            await websocket.send(response)



# Запуск WebSocket-сервера на порту 8765
async def main():
    server = await websockets.serve(echo, "localhost", 8765)
    print("WebSocket сервер запущен на ws://localhost:8765")
    await server.wait_closed()


asyncio.run(main())