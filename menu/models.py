from django.db import models
from django.utils.translation import gettext_lazy as _


class Statuses(models.TextChoices):
    """Statuses for menu and items."""

    AVAILABLE = "available", "Доступно"
    UNAVAILABLE = "unavailable", "Недоступно"


class Menu(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name=_("Название"),
    )
    status = models.CharField(
        max_length=50,
        verbose_name=_("Cтатус"),
        choices=Statuses.choices,
        default=Statuses.AVAILABLE,
    )

    class Meta:
        verbose_name = _("Меню")
        verbose_name_plural = _("Меню")

    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    menu = models.ForeignKey(
        Menu,
        on_delete=models.CASCADE,
        verbose_name=_("Меню"),
    )
    parent = models.ForeignKey(
        "self",
        on_delete=models.CASCADE,
        verbose_name=_("Родитель"),
        related_name="child",
        blank=True,
        null=True,
    )
    name = models.CharField(
        max_length=100,
        verbose_name=_("Название"),
    )
    status = models.CharField(
        max_length=50,
        verbose_name=_("Cтатус"),
        choices=Statuses.choices,
        default=Statuses.AVAILABLE,
    )
    url = models.CharField(
        max_length=250,
        verbose_name=_("URL"),
        help_text="Может быть задан как явным образом, так и через named url",
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = _("Элемент меню")
        verbose_name_plural = _("Элементы меню")

    @property
    def get_absolute_url(self) -> str:
        return "/%s" % self.url

    def __str__(self) -> str:
        return self.name
