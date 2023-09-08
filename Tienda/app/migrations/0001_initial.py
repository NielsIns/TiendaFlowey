# Generated by Django 4.0.4 on 2022-06-28 22:53

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('cod_carr', models.AutoField(primary_key=True, serialize=False)),
                ('comprado', models.BooleanField()),
                ('total', models.IntegerField(null=True)),
                ('descuento', models.IntegerField(null=True)),
                ('subtotal', models.IntegerField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'db_carrito',
            },
        ),
        migrations.CreateModel(
            name='TipoCliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_tipo_cliente',
            },
        ),
        migrations.CreateModel(
            name='TipoPago',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_tipo_pago',
            },
        ),
        migrations.CreateModel(
            name='TipoProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'db_tipo_producto',
            },
        ),
        migrations.CreateModel(
            name='TipoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20, null=True)),
            ],
            options={
                'db_table': 'db_tipo_user',
            },
        ),
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suscrito', models.BooleanField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'db_suscripcion',
            },
        ),
        migrations.CreateModel(
            name='Seguimiento',
            fields=[
                ('cod_seguimiento', models.AutoField(primary_key=True, serialize=False)),
                ('estado', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carrito')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'db_seguimiento',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('codigo', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('marca', models.CharField(max_length=20)),
                ('precio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=100)),
                ('stock', models.IntegerField()),
                ('imagen', models.ImageField(null=True, upload_to='productos')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipoproducto')),
            ],
            options={
                'db_table': 'db_producto',
            },
        ),
        migrations.CreateModel(
            name='Historial',
            fields=[
                ('num_hist', models.AutoField(primary_key=True, serialize=False)),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carrito')),
                ('seguimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.seguimiento')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'db_historial',
            },
        ),
        migrations.CreateModel(
            name='ElementCarrito',
            fields=[
                ('cod_element_carrito', models.AutoField(primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField()),
                ('comprado', models.BooleanField()),
                ('carrito', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.carrito')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.producto')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'db_element_carrito',
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('run', models.CharField(max_length=13, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=20)),
                ('clave', models.CharField(max_length=20)),
                ('correo', models.CharField(max_length=25)),
                ('region', models.CharField(max_length=25)),
                ('comuna', models.CharField(max_length=25)),
                ('direccion', models.CharField(max_length=150)),
                ('imagen', models.ImageField(null=True, upload_to='usuarios')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('tipo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.tipocliente')),
            ],
            options={
                'db_table': 'db_cliente',
            },
        ),
        migrations.AddField(
            model_name='mainuser',
            name='tipo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.tipouser'),
        ),
        migrations.AddField(
            model_name='mainuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
    ]