from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


# Create your models here.
class BaseModel(models.Model):
    objects = models.Manager
    description = models.TextField(blank=True, null=True, default='')
    activated = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s (#%s)" % (self.__class__.__name__, self.pk)

    @property
    def desc(self):
        if len(self.description) > 20:
            return self.description[:17] + '...'
        else:
            return self.description

    class Meta:
        abstract = True

    pass


class Organization(BaseModel):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('organization')
        verbose_name_plural = _('organizations')

    pass


class User(AbstractUser):
    """
    Default custom user model for MOS Web Server.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    organization = models.ForeignKey(Organization, null=True, blank=True, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
