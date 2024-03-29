from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response


def get_post_delete_method(
        self, request, pk,
        obj_model=None,
        model=None,
        serializer=None):
    """
    Дополнительный метод для однотипных post, delete запросов.

    obj_model - Модель для получения объекта
    model - Модель через которую проходит связь
    serializer - Сериализатор для ответа пользователю после операции.
    """
    obj = get_object_or_404(obj_model, id=pk)
    validated_data = {}
    for field in model._meta.get_fields():
        if field.name != 'id' and field.name != 'user':
            validated_data[field.name] = obj
        if field.name == 'user':
            validated_data[field.name] = request.user

    if request.method == 'POST':

        if obj == request.user:
            return Response(
                {'errors': 'Ошибка при добавлении'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if model.objects.filter(**validated_data).exists():
            return Response(
                {'errors': 'Ошибка при добавлении'},
                status=status.HTTP_400_BAD_REQUEST
            )

        model.objects.create(**validated_data)
        serializer = serializer(
            obj, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    if request.method == 'DELETE':

        if model.objects.filter(**validated_data).exists():
            model.objects.get(**validated_data).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(
            {'errors': 'Ошибка при удалении'},
            status=status.HTTP_400_BAD_REQUEST
        )

    return Response(
        {'errors': 'Метод запроса не соответствует POST или DELETE'},
        status=status.HTTP_400_BAD_REQUEST
    )
