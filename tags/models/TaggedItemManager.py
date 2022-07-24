from django.contrib.contenttypes.models import ContentType

from django.db import models

from tags.models import TaggedItem


class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)

        return TaggedItem.objects \
            .select_related('tag') \
            .filter(
            content_type=content_type,
            object_id=obj_id
        )
