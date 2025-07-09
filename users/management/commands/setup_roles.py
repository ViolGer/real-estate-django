from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from course.models import Lesson, Achievement
from leads.models import Lead

class Command(BaseCommand):
    help = "Setup initial user groups and permissions"

    def handle(self, *args, **kwargs):
        roles = {
            "Агент": {
                "course": ["view_lesson", "view_achievement"],
                "leads": ["add_lead", "view_lead"],
            },
            "Администратор": "all",
            "РОП": {
                "leads": ["view_lead"],
            },
            "Методолог": {
                "course": ["add_lesson", "change_lesson", "delete_lesson", "view_lesson", "add_achievement", "view_achievement"],
            },
            "Техподдержка": {
                "leads": [],
            },
        }

        for role_name, permissions in roles.items():
            group, created = Group.objects.get_or_create(name=role_name)
            if permissions == "all":
                all_perms = Permission.objects.all()
                group.permissions.set(all_perms)
                self.stdout.write(self.style.SUCCESS(f"{role_name}: назначены все разрешения"))
            else:
                perms_to_set = []
                for app_label, codename_list in permissions.items():
                    for codename in codename_list:
                        try:
                            perm = Permission.objects.get(codename=codename, content_type__app_label=app_label)
                            perms_to_set.append(perm)
                        except Permission.DoesNotExist:
                            self.stdout.write(self.style.WARNING(f"⚠️ Разрешение не найдено: {codename} в {app_label}"))
                group.permissions.set(perms_to_set)
                self.stdout.write(self.style.SUCCESS(f"{role_name}: назначено {len(perms_to_set)} разрешений"))

        self.stdout.write(self.style.SUCCESS("✅ Роли и права успешно настроены."))
