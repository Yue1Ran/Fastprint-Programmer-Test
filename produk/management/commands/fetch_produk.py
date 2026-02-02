from django.core.management.base import BaseCommand
import requests, hashlib
from email.utils import parsedate_to_datetime
from produk.models import Produk, Kategori, Status

class Command(BaseCommand):
    help = 'Fetch produk Fastprint'

    def handle(self, *args, **kwargs):
        url = "https://recruitment.fastprint.co.id/tes/api_tes_programmer"
        session = requests.Session()
        r = session.post(url)

        # pull username dari header 
        username = r.headers["X-Credentials-Username"].split(" ")[0]

        # pull  tgl dari header date
        server_date = parsedate_to_datetime(r.headers["Date"])
        raw = f"bisacoding-{str(server_date.day).zfill(2)}-{str(server_date.month).zfill(2)}-{str(server_date.year)[-2:]}"
        password = hashlib.md5(raw.encode()).hexdigest()

        payload = {
            "username": username,
            "password": password
        }

        # print("USERNAME:", username)
        # print("RAW:", raw)
        # print("PASSWORD(MD5):", password)
        
        # REQUEST LOGIN + DATA
        r2 = session.post(url, data=payload)

        print("STATUS:", r2.status_code)
        print("JSON:", r2.json())

        if r2.status_code != 200 or r2.json().get("error") != 0:

            #dummy fallback data
            # kategori, _ = Kategori.objects.get_or_create(
            #     nama_kategori="Fallback"
            # )
            # status, _ = Status.objects.get_or_create(
            #     nama_status="bisa dijual"
            # )

            # Produk.objects.get_or_create(
            #     nama_produk="Produk Dummy Fastprint",
            #     defaults={
            #         "harga": 10000,
            #         "kategori": kategori,
            #         "status": status
            #     }
            # )

            print("API gagal → fallback data dibuat")
            return


        data = r2.json()["data"]

        for item in data:
            kategori, _ = Kategori.objects.get_or_create(
                nama_kategori=item["kategori"]
            )
            status, _ = Status.objects.get_or_create(
                nama_status=item["status"]
            )

            Produk.objects.update_or_create(
                nama_produk=item["nama_produk"],
                defaults={
                    "harga": item["harga"],
                    "kategori": kategori,
                    "status": status
                }
            )

        print("SUCCESS")
