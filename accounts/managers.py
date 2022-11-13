from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):

    def _create_user(self, username, password, **extra_fields):
        user = self.model(
            username=username,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields['is_staff'] = False
        extra_fields['is_superuser'] = False
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if (extra_fields.get("is_staff") is not True) and (extra_fields.get("is_superuser") is not True):
            raise ValueError("Superuser must have both is_staff and is_superuser attributes set to True")
        return self._create_user(username, password, **extra_fields)
