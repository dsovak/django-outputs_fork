
# Generated by Django 2.2.9 on 2020-08-21 11:21

from django.conf import settings
import django.contrib.postgres.fields
from django.db import migrations, models
import gm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('outputs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='export',
            name='emails',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=33), blank=True, default=list, size=None),
        ),
        migrations.AddField(
            model_name='scheduler',
            name='emails',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=33), blank=True, default=list, size=None),
        ),
        migrations.AlterField(
            model_name='export',
            name='items',
            field=gm2m.fields.GM2MField('invoicing.Invoice', 'accounts.Team', 'board.Task', 'board.Inquiry', 'board.Announcement', 'chronicle.Event', 'directory.Company', 'directory.Carrier', 'directory.Activity', 'helpdesk.Article', 'logistics.Offer', 'logistics.Order', 'logistics.Option', 'logistics.ShippingOrder', related_name='exports_where_item', through_fields=('gm2m_src', 'gm2m_tgt', 'gm2m_ct', 'gm2m_pk')),
        ),
        migrations.AlterField(
            model_name='export',
            name='recipients',
            field=models.ManyToManyField(blank=True, related_name='export_where_recipient', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='scheduler',
            name='recipients',
            field=models.ManyToManyField(blank=True, related_name='scheduler_where_recipient', to=settings.AUTH_USER_MODEL),
        ),
    ]
