from django.core.files.base import ContentFile
from django.core.files.storage import FileSystemStorage
import csv
import os

fs = FileSystemStorage(location="temp")


from django.db import transaction
from apps.clients.models import Order, OrderStatusUpdate


class UploadOrdersMixin(object):
    def __init__(self, file, client):
        self.file = file
        self.client = client

    def run(self):
        self.__trigger_upload()

    def __trigger_upload(self):
        # if self.file.extension in ["csv", "CSV"]:
        self.__upload_csv_orders()
        # elif self.file.extension in ["xls", "xlsx", "XLS", "XLSX"]:
        #    self.__upload_xls_orders()

    @transaction.atomic
    def __upload_csv_orders(self):
        source_file_content = self.file.read()
        source_file_content = ContentFile(source_file_content)
        source_file_name = fs.save("temp_source_file.csv", source_file_content)
        temp_source_file = fs.path(source_file_name)

        orders_list = []
        with open(temp_source_file, "r") as file:
            data = list(csv.DictReader(file))
            for row in data:
                print(row)

                orders_list.append(
                    Order(
                        client=self.client,
                        tenant=self.client.tenant,
                        order_number=row["order_number"],
                        customer_name=row["customer_name"],
                        customer_phone=row["customer_phone"],
                        customer_address=row["customer_address"],
                        delivery_cost=row["delivery_cost"],
                    )
                )

        orders = Order.objects.bulk_create(orders_list)
        orders_updates_list = [
            OrderStatusUpdate(
                order=order, previous_status="Created", next_status="Pending Dispatch"
            )
            for order in orders
        ]
        OrderStatusUpdate.objects.bulk_create(orders_updates_list)

        # self.__clear_files(self.file)

    def __upload_xls_orders(self):
        pass

    def __clear_files(self, file_path):
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except OSError as e:
                print(f"Error: {file_path} : {e.strerror}")
        else:
            print(f"File does not exist: {file_path}")
