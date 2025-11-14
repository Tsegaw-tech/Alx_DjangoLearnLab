from django.apps import AppConfig

class BookshelfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bookshelf'

    def ready(self):
        # Import here inside ready(), not at top-level
        from django.contrib.auth.models import Group, Permission
        from django.db.models.signals import post_migrate
        from django.dispatch import receiver

        @receiver(post_migrate)
        def create_groups(sender, **kwargs):
            # Create groups if they don't exist
            groups = {
                "Admins": ["can_view", "can_create", "can_edit", "can_delete"],
                "Editors": ["can_create", "can_edit"],
                "Viewers": ["can_view"],
            }

            for group_name, perm_codes in groups.items():
                group, created = Group.objects.get_or_create(name=group_name)
                for code in perm_codes:
                    try:
                        perm = Permission.objects.get(codename=code)
                        group.permissions.add(perm)
                    except Permission.DoesNotExist:
                        pass  # Permission not yet created
