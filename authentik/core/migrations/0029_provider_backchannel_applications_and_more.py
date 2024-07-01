# Generated by Django 4.1.7 on 2023-04-30 17:56

import django.db.models.deletion
from django.apps.registry import Apps
from django.db import DatabaseError, InternalError, ProgrammingError, migrations, models
from django.db.backends.base.schema import BaseDatabaseSchemaEditor


def backport_is_backchannel(apps: Apps, schema_editor: BaseDatabaseSchemaEditor):
    from authentik.providers.ldap.models import LDAPProvider
    from authentik.providers.scim.models import SCIMProvider

    for model in [LDAPProvider, SCIMProvider]:
        try:
            for obj in model.objects.only("is_backchannel"):
                obj.is_backchannel = True
                obj.save()
        except (DatabaseError, InternalError, ProgrammingError):
            # The model might not have been migrated yet/doesn't exist yet
            # so we don't need to worry about backporting the data
            pass


class Migration(migrations.Migration):
    dependencies = [
        ("authentik_core", "0028_provider_authentication_flow"),
        ("authentik_providers_ldap", "0002_ldapprovider_bind_mode"),
        ("authentik_providers_scim", "0006_rename_parent_group_scimprovider_filter_group"),
    ]

    operations = [
        migrations.AddField(
            model_name="provider",
            name="backchannel_application",
            field=models.ForeignKey(
                default=None,
                help_text="Accessed from applications; optional backchannel providers for protocols like LDAP and SCIM.",
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="backchannel_providers",
                to="authentik_core.application",
            ),
        ),
        migrations.AddField(
            model_name="provider",
            name="is_backchannel",
            field=models.BooleanField(default=False),
        ),
        migrations.RunPython(backport_is_backchannel),
        migrations.AlterField(
            model_name="propertymapping",
            name="managed",
            field=models.TextField(
                default=None,
                help_text="Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.",
                null=True,
                unique=True,
                verbose_name="Managed by authentik",
            ),
        ),
        migrations.AlterField(
            model_name="source",
            name="managed",
            field=models.TextField(
                default=None,
                help_text="Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.",
                null=True,
                unique=True,
                verbose_name="Managed by authentik",
            ),
        ),
        migrations.AlterField(
            model_name="token",
            name="managed",
            field=models.TextField(
                default=None,
                help_text="Objects that are managed by authentik. These objects are created and updated automatically. This flag only indicates that an object can be overwritten by migrations. You can still modify the objects via the API, but expect changes to be overwritten in a later update.",
                null=True,
                unique=True,
                verbose_name="Managed by authentik",
            ),
        ),
    ]
