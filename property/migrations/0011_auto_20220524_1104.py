# Generated by Django 2.2.24 on 2022-05-24 08:04

from django.db import migrations


def fill_owners_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        flat_owners = Owner.objects.filter(
            name=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
        )
        if flat_owners:
            flat.owners.set(flat_owners)
        else:
            flat_owner = Owner.objects.create(
                name=flat.owner,
                owners_phonenumber=flat.owners_phonenumber,
                owner_pure_phone=flat.owner_pure_phone
            )
            flat.owners.clear()
            flat.owners.add(flat_owner)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_auto_20220524_1036'),
    ]

    operations = [
        migrations.RunPython(fill_owners_flats)
    ]
