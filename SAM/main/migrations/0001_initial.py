# Generated by Django 4.1.6 on 2023-02-13 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Business_User_Accounts",
            fields=[
                ("user_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=100)),
                ("business_name", models.CharField(max_length=50)),
                ("contact_no", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="User_Accounts",
            fields=[
                ("user_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("address", models.CharField(max_length=100)),
                ("contact_no", models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name="User_Address",
            fields=[
                ("address_id", models.IntegerField(primary_key=True, serialize=False)),
                ("address", models.CharField(max_length=100)),
                ("current", models.BooleanField()),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.user_accounts",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Services",
            fields=[
                ("service_id", models.IntegerField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=50)),
                ("category", models.CharField(max_length=50)),
                ("description", models.CharField(max_length=200)),
                ("image", models.ImageField(upload_to="")),
                ("price", models.IntegerField()),
                (
                    "b_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.business_user_accounts",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Membership",
            fields=[
                (
                    "membership_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("membership_type", models.CharField(max_length=50)),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.user_accounts",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Feedback",
            fields=[
                ("feedback_id", models.IntegerField(primary_key=True, serialize=False)),
                ("rating", models.IntegerField()),
                ("review", models.CharField(max_length=150)),
                (
                    "b_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.business_user_accounts",
                    ),
                ),
                (
                    "service_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.services"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="main.user_accounts",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Business_User_Address",
            fields=[
                ("address_id", models.IntegerField(primary_key=True, serialize=False)),
                ("address", models.CharField(max_length=100)),
                ("current", models.BooleanField()),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.business_user_accounts",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Appointments",
            fields=[
                (
                    "appointment_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("date_time", models.DateTimeField()),
                (
                    "b_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.business_user_accounts",
                    ),
                ),
                (
                    "service_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="main.services"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.user_accounts",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Appointment_History",
            fields=[
                (
                    "appointment_id",
                    models.IntegerField(primary_key=True, serialize=False),
                ),
                ("date_time", models.DateTimeField()),
                (
                    "b_user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.business_user_accounts",
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="main.user_accounts",
                    ),
                ),
            ],
        ),
    ]
