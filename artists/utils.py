from django.contrib.contenttypes.models import ContentType

from rest_framework_serializer_extensions.utils import get_hash_ids_source


def internal_id_from_model_and_external_id_and_content_type(model, external_id, content_type):
    try:
        _, instance_id = get_hash_ids_source().decode(
            external_id
        )
    except (TypeError, ValueError):
        raise model.DoesNotExist

    if content_type.model_class() != model:
        raise model.DoesNotExist

    return instance_id


def internal_ids_from_model_and_external_ids(model, external_ids):
    """
    This optimizes the internal_id_from_model_and_external_id() util in the django_rest_serializer_extensions which
    queries the database for model content type on every external_id transformation
    The assumption here is that all external_ids belong to the same model content_type
    link: https://github.com/evenicoulddoit/django-rest-framework-serializer-extensions/blob/master/rest_framework_serializer_extensions/utils.py

    :param model: The model whose external_ids have to be transformed into internal_ids
    :param external_ids: The external_ids or HashIds
    :return: list
    """
    content_type = ContentType.objects.get_for_model(model)
    internal_ids = [
        internal_id_from_model_and_external_id_and_content_type(model, external_id, content_type)
        for external_id in external_ids
    ]
    return internal_ids
