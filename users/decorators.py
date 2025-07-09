from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied

def group_required(group_name):
    """
    Декоратор, который пускает только пользователей из нужной группы.
    Если пользователь не в группе — выдаёт 403 (Permission Denied).
    """
    def in_group(u):
        if u.is_authenticated:
            if u.groups.filter(name=group_name).exists() or u.is_superuser:
                return True
        raise PermissionDenied
    return user_passes_test(in_group)


# Удобные алиасы-декораторы:
agent_required = group_required('Агент')
admin_required = group_required('Администратор')
manager_required = group_required('РОП')
methodologist_required = group_required('Методолог')
support_required = group_required('Техподдержка')