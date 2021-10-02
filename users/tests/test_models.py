import pytest

from ..models import User
pytestmark = pytest.mark.django_db

def test_create_user():
    user = User.objects.create_user(
        username ='usuario_teste',
        email ='usuario@teste.com',
        password='123456'
    )

    assert user.username == "usuario_teste"
    assert user.email =="usuario@teste.com"
    assert user.is_active
    assert not user.is_staff
    assert not user.is_superuser

def test_create_superuser():
    user = User.objects.create_superuser(
        username ="admin_teste",
        email ="admin@teste.com",
        password="321"
    )

    assert user.username == "admin_teste"
    assert user.email == "admin@teste.com"
    assert user.is_active
    assert user.is_staff
    assert user.is_superuser