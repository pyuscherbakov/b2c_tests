from core.utils.data_generator import *


body_create_contract = {
    "vehicle": {
        "category": "B",
        "mark": "Hyundai",
        "model": "Solaris",
        "year": 2022,
        "cost": 1100000.55,
        "power": 100,
        "mileage": 10,
        "engine_volume": 123,
        "engine_type": "petrol",
        "body_number": "asd123",
        "chassis_number": "123asd",
        "engine_number": "ewr123",
        "licence_plate": licence_plate,
        "vin": vin,
        "pts": {
            "series": "1234",
            "number": "011223",
            "issue_date": "2012-12-20"
        },
        "sts": {
            "series": "1234",
            "number": "011223",
            "issue_date": "2012-12-20"
        }
    },
    "insurer": {
        "physical": {
            "birth_date": "1986-12-12",
            "last_name": "Анисимов",
            "first_name": "Панкрат",
            "middle_name": "Христофорович",
            "sex": "male",
            "married": False,
            "children": 0,
            "passport": {
                "series": series,
                "number": number,
                "issue_date": "2012-01-01",
                "issued_by": "ОВД Московского района Московской области",
                "department_code": "440-000",
                "birth_place": "Москва"
            },
            "registration_address": {
                "country": "Россия",
                "region": "Московская обл",
                "area": "г Клин",
                "city": "г Клин",
                "city_area": "",
                "city_district": "",
                "settlement": "",
                "street": "Волоколамское шоссе",
                "house": "1",
                "block": "",
                "flat": "1",
                "fias_id": "7b9c1219-f2d2-498f-a156-ec05df85f831"
            },
            "phone": "99999999999",
            "email": "test@fast-system.ru"
        }
    },
    "owner": {
        "physical": {
            "birth_date": "1986-12-12",
            "last_name": "Анисимов",
            "first_name": "Панкрат",
            "middle_name": "Христофорович",
            "sex": "male",
            "married": False,
            "children": 0,
            "passport": {
                "series": series,
                "number": number,
                "issue_date": "2012-01-01",
                "issued_by": "ОВД Московского района Московской области",
                "department_code": "440-000",
                "birth_place": "Москва"
            },
            "registration_address": {
                "country": "Россия",
                "region": "Московская обл",
                "area": "г Клин",
                "city": "г Клин",
                "city_area": "",
                "city_district": "",
                "settlement": "",
                "street": "Волоколамское шоссе",
                "house": "1",
                "block": "",
                "flat": "1",
                "fias_id": "7b9c1219-f2d2-498f-a156-ec05df85f831"
            },
            "phone": "99999999999",
            "email": "test@fast-system.ru"
        }
    },
    "drivers_min_age": 18,
    "drivers_min_exp": 1,
    "drivers": [
        {
            "birth_date": "1986-12-12",
            "last_name": "Иванов",
            "first_name": "Иван",
            "middle_name": "Иванович",
            "sex": "male",
            "married": False,
            "children": 0,
            "driver_license": {
                "series": series,
                "number": number,
                "issue_date": "2012-12-20",
                "driving_experience_date": "2012-12-20"
            },
            "registration_address": {
                "country": "Россия",
                "region": "Московская обл",
                "area": "г Клин",
                "city": "г Клин",
                "city_area": "",
                "city_district": "",
                "settlement": "",
                "street": "Волоколамское шоссе",
                "house": "1",
                "block": "",
                "flat": "1",
                "fias_id": "7b9c1219-f2d2-498f-a156-ec05df85f831"
            }
        }
    ],
    "terms": {
        "kasko": {
            "start_date": start_date,
            "end_date": end_date,
            "start_exploitation_date": start_date,
            "purchase_date": start_date,
            "franchise": "Нет",
            "bank": ""
        }
    }
}

body_create_calculation = {"products": [{"id": ""}]}
