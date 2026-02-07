from httpx import Response
import allure  # Импортируем allure
from clients.api_client import APIClient
from clients.api_coverage import tracker  # Импортируем трекер из api_coverage.py
from clients.exercises.exercises_schema import GetExercisesQuerySchema, CreateExerciseRequestSchema, \
    UpdateExerciseRequestSchema, GetExercisesResponseSchema, CreateExerciseResponseSchema, UpdateExerciseResponseSchema
# Вместо AuthenticationUserDict импортируем AuthenticationUserSchema
from clients.private_http_builder import get_private_http_client, AuthenticationUserSchema
from tools.routes import APIRoutes  # Импортируем enum APIRoutes


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    @allure.step("Get exercises")  # Добавили allure шаг
    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def get_exercises_api(self, query: GetExercisesQuerySchema) -> Response:
        """
        Метод получения списка заданий.

        :param query: Словарь с courseId.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        # Вместо /api/v1/exercises используем APIRoutes.EXERCISES
        return self.get(APIRoutes.EXERCISES, params=query.model_dump(by_alias=True))

    @allure.step("Get exercise by id {exercise_id}")  # Добавили allure шаг
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        # Вместо /api/v1/exercises используем APIRoutes.EXERCISES
        return self.get(f"{APIRoutes.EXERCISES}/{exercise_id}")


    @allure.step("Create exercise")  # Добавили allure шаг
    @tracker.track_coverage_httpx(APIRoutes.EXERCISES)
    def create_exercise_api(self, request: CreateExerciseRequestSchema) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с title, courseId, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        # Вместо /api/v1/exercises используем APIRoutes.EXERCISES
        return self.post(APIRoutes.EXERCISES, json=request.model_dump(by_alias=True))

    @allure.step("Update exercise by id {exercise_id}")  # Добавили allure шаг
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def update_exercise_api(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> Response:
        """
        Метод обновления задания.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с title, maxScore, minScore, orderIndex, description, estimatedTime.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        # Вместо /api/v1/exercises используем APIRoutes.EXERCISES
        return self.patch(f"{APIRoutes.EXERCISES}/{exercise_id}", json=request.model_dump(by_alias=True))

    @allure.step("Delete exercise by id {exercise_id}")  # Добавили allure шаг
    @tracker.track_coverage_httpx(f"{APIRoutes.EXERCISES}/{{exercise_id}}")
    def delete_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        # Вместо /api/v1/exercises используем APIRoutes.EXERCISES
        return self.delete(f"{APIRoutes.EXERCISES}/{exercise_id}")

    # Добавили 4 новых метода get_exercise, get_exercises, create_exercise, update_exercise
    def get_exercises(self, query: GetExercisesQuerySchema) -> GetExercisesResponseSchema:
        response = self.get_exercises_api(query)
        return GetExercisesResponseSchema.model_validate_json(response.text)


    def get_exercise (self, exercise_id: str) -> GetExercisesResponseSchema:
        response = self.get_exercise_api(exercise_id)
        return GetExercisesResponseSchema.model_validate_json(response.text)

    def create_exercise(self, request: CreateExerciseRequestSchema) -> CreateExerciseResponseSchema:
        response = self.create_exercise_api(request)
        return CreateExerciseResponseSchema.model_validate_json(response.text)

    def update_exercise(self, exercise_id: str, request: UpdateExerciseRequestSchema) -> UpdateExerciseResponseSchema:
        response = self.update_exercise_api(exercise_id, request)
        return UpdateExerciseResponseSchema.model_validate_json(response.text)


# Добавляем builder для ExercisesClient
# Вместо AuthenticationUserDict используем AuthenticationUserSchema
def get_exercises_client(user: AuthenticationUserSchema) -> ExercisesClient:
    """
    Функция создаёт экземпляр ExercisesClient с уже настроенным HTTP-клиентом.

    :return: Готовый к использованию ExercisesClient.
    """
    return ExercisesClient(client=get_private_http_client(user))