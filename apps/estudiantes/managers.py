from django.db import models


class ApiModelQuerySet(models.QuerySet):
    def all(self):
        return self.filter(archived=False)

    def removed(self):
        return self.filter(archived=True)

    def update(self, **kwargs):
        super().update(**kwargs)


class ApiModelManager(models.Manager):
    def get_queryset(self):
        return ApiModelQuerySet(self.model, using=self._db)

    def all(self):
        return self.get_queryset().all().order_by('-id')

    def removed(self):
        return self.get_queryset().removed().order_by('-id')
