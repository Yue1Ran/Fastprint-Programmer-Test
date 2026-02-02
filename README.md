Fastprint Programmer Test – Django
Nama: Dwi Rangga Kusuma

==================================================

DESKRIPSI APLIKASI

Aplikasi Memiliki Fitur:
- Autentikasi ke API Fastprint
- Mengambil data produk dari API
- Menyimpan data produk ke database MySQL
- Menampilkan daftar produk melalui web
- Hanya menampilkan produk dengan status "bisa dijual"
- Mendukung operasi CRUD (Create, Read, Update, Delete)

==================================================

TEKNOLOGI YANG DIGUNAKAN

- Python 3.11
- Django 4.2
- MySQL (XAMPP / phpMyAdmin)
- PyMySQL
- Requests

==================================================

STRUKTUR PROJECT

fastprint_test/
│
├── fastprint_test/
│   └── settings.py
│
├── produk/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── management/
│       └── commands/
│           └── fetch_produk.py
│
├── templates/
│   └── produk/
│       └── produk_list.html
│
├── manage.py
└── README.md

==================================================

KONFIGURASI DATABASE (MySQL)

Database menggunakan MySQL melalui XAMPP (phpMyAdmin).

1. Buat database baru dengan nama:
   fastprint_db

2. Konfigurasi database pada settings.py:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'fastprint_db',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

==================================================

INSTALASI DAN SETUP

1. Aktifkan virtual environment (Windows - PowerShell):
   venv\Scripts\activate

2. Install dependency:
   pip install django pymysql requests

==================================================

MIGRASI DATABASE

Jalankan perintah berikut:

python manage.py makemigrations
python manage.py migrate

==================================================

PENGAMBILAN DATA DARI API FASTPRINT

Pengambilan data dilakukan menggunakan custom Django management command.

Perintah:
python manage.py fetch_produk

Jika autentikasi API berhasil, data produk akan otomatis tersimpan
ke dalam database MySQL.

==================================================

MODEL DATABASE

Model utama adalah Produk dengan field:
- id_produk (Primary Key)
- nama_produk
- harga
- kategori (Foreign Key)
- status (Foreign Key)

==================================================

FILTER DATA PRODUK

Pada halaman web, hanya produk dengan status:
"bisa dijual"

yang akan ditampilkan.
Produk dengan status "tidak bisa dijual" tidak ditampilkan di halaman list.

==================================================

MENJALANKAN APLIKASI

Jalankan server Django dengan perintah:
python manage.py runserver

Dapat di akses aplikasi melalui browser:
http://127.0.0.1:8000/
