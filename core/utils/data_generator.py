import random
import datetime

licence_plate = "А" + str(random.randint(100, 999)) + "АА47"
vin = "TEST" + str(random.randint(1000000000000, 9999999999999))
series = str(random.randint(1000, 9999))
number = str(random.randint(100000, 999999))

start_date = str(datetime.date.today() + datetime.timedelta(days=1))
end_date = str(datetime.date.today() + datetime.timedelta(days=365))
