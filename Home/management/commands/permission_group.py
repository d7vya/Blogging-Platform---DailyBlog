from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = "Create default groups and assign permissions"

    def handle(self, *args, **kwargs):
        groupnper = {
            'user_group': {
                'Blog': ['add_blog', 'view_blog'],
                'Comment': ['add_comment', 'view_comment'],
            },
            'ban_user': {
                'Blog': ['view_blog'],
                'Comment': ['view_comment'],
            },
            'staff_group': {
                'Blog': ['add_blog', 'view_blog', 'delete_blog'],
                'Comment': ['add_comment', 'view_comment', 'delete_comment'],
                'User': ['ban_user'],  # Custom permission for banning users
            },
        }

        for group_name, model_perms in groupnper.items():
            # Create or get the group
            group, created = Group.objects.get_or_create(name=group_name)
            self.stdout.write(f"{'Created' if created else 'Exists'}: Group '{group_name}'")

            for model_name, perms in model_perms.items():
                try:
                    # Get ContentType for the model
                    if model_name == 'User':
                        content_type = ContentType.objects.get(app_label='auth', model='user')
                    else:
                        content_type = ContentType.objects.get(app_label='Home', model=model_name.lower())
                    
                    # Assign permissions
                    for perm_codename in perms:
                        permission, perm_created = Permission.objects.get_or_create(
                            codename=perm_codename,
                            content_type=content_type,
                            defaults={'name': f"Can {perm_codename.replace('_', ' ')} {model_name}"}
                        )
                        group.permissions.add(permission)
                        self.stdout.write(
                            f"{'Created' if perm_created else 'Exists'}: Permission '{permission.codename}' "
                            f"added to group '{group_name}'"
                        )
                except ContentType.DoesNotExist:
                    self.stderr.write(f"Error: ContentType for model '{model_name}' not found.")
                except Exception as e:
                    self.stderr.write(f"Unexpected error: {e}")

        self.stdout.write("Default groups and permissions created successfully.")
#divya has ban_user permission assigned to it through shell