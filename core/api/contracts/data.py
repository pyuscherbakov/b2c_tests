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

schema_create_contract = {
    "type": "object",
    "required": ["data"],
    "properties": {
        "data": {
            "type": "object",
            "required": ["id", "contract"],
            "properties": {
                "id": {"type": "string"},
                "contract": {
                    "type": "object",
                    "required": ["vehicle", "insurer", "owner", "drivers_min_age", "drivers_min_exp", "drivers", "terms"],
                    "properties": {
                        "vehicle": {
                            "type": "object",
                            "required": ["cost", "category", "mark", "model", "year", "power", "mileage",
                                         "engine_volume", "engine_type", "body_number", "chassis_number",
                                         "engine_number", "licence_plate", "vin", "pts", "sts"
                            ],
                            "properties": {
                                "cost": {"type": "number"},
                                "category": {"type": "string"},
                                "mark": {"type": "string"},
                                "model": {"type": "string"},
                                "year": {"type": "integer"},
                                "power": {"type": "integer"},
                                "mileage": {"type": "integer"},
                                "engine_volume": {"type": "integer"},
                                "engine_type": {"type": "string"},
                                "body_number": {"type": "string"},
                                "chassis_number": {"type": "string"},
                                "engine_number": {"type": "string"},
                                "licence_plate": {"type": "string"},
                                "vin": {"type": "string"},
                                "pts": {
                                    "type": "object",
                                    "required": ["series", "number", "issue_date"],
                                    "properties": {
                                        "series": {"type": "string"},
                                        "number": {"type": "string"},
                                        "issue_date": {"type": "string"}
                                    }
                                },
                                "sts": {
                                    "type": "object",
                                    "required": ["series", "number","issue_date"],
                                    "properties": {
                                        "series": {"type": "string"},
                                        "number": {"type": "string"},
                                        "issue_date": {"type": "string"}
                                    }
                                }
                            }
                        },
                        "insurer": {
                            "type": "object",
                            "required": ["physical"],
                            "properties": {
                                "physical": {
                                    "type": "object",
                                    "required": ["birth_date", "last_name", "first_name", "middle_name", "sex",
                                                 "married", "children", "passport", "registration_address", "phone",
                                                 "email"],
                                    "properties": {
                                        "birth_date": {"type": "string"},
                                        "last_name": {"type": "string"},
                                        "first_name": {"type": "string"},
                                        "middle_name": {"type": "string"},
                                        "sex": {"type": "string"},
                                        "married": {"type": "boolean"},
                                        "children": {"type": "integer"},
                                        "passport": {
                                            "type": "object",
                                            "required": ["series", "number", "issue_date", "issued_by",
                                                         "department_code", "birth_place"],
                                            "properties": {
                                                "series": {"type": "string"},
                                                "number": {"type": "string"},
                                                "issue_date": {"type": "string"},
                                                "issued_by": {"type": "string"},
                                                "department_code": {"type": "string"},
                                                "birth_place": {"type": "string"}
                                            }
                                        },
                                        "registration_address": {
                                            "type": "object",
                                            "required": ["country", "region", "city", "district", "street", "house",
                                                         "building", "apartment", "fias"],
                                            "properties": {
                                                "country": {"type": "string"},
                                                "region": {"type": "string"},
                                                "city": {"type": "string"},
                                                "district": {"type": "null"},
                                                "street": {"type": "string"},
                                                "house": {"type": "integer"},
                                                "building": {"type": "null"},
                                                "apartment": {"type": "null"},
                                                "fias": {"type": "null"}
                                            }
                                        },
                                        "phone": {"type": "string"},
                                        "email": {"type": "string"}
                                    }
                                }
                            }
                        },
                        "owner": {
                            "type": "object",
                            "required": ["physical"],
                            "properties": {
                                "physical": {
                                    "type": "object",
                                    "required": ["birth_date", "last_name", "first_name", "middle_name", "sex",
                                                 "married", "children", "passport", "registration_address", "phone",
                                                 "email"],
                                    "properties": {
                                        "birth_date": {"type": "string"},
                                        "last_name": {"type": "string"},
                                        "first_name": {"type": "string"},
                                        "middle_name": {"type": "string"},
                                        "sex": {"type": "string"},
                                        "married": {"type": "boolean"},
                                        "children": {"type": "integer"},
                                        "passport": {
                                            "type": "object",
                                            "required": ["series", "number", "issue_date", "issued_by",
                                                         "department_code", "birth_place"],
                                            "properties": {
                                                "series": {"type": "string"},
                                                "number": {"type": "string"},
                                                "issue_date": {"type": "string"},
                                                "issued_by": {"type": "string"},
                                                "department_code": {"type": "string"},
                                                "birth_place": {"type": "string"}
                                            }
                                        },
                                        "registration_address": {
                                            "type": "object",
                                            "required": ["country", "region", "city", "district", "street", "house",
                                                         "building", "apartment", "fias"],
                                            "properties": {
                                                "country": {"type": "string"},
                                                "region": {"type": "string"},
                                                "city": {"type": "string"},
                                                "district": {"type": "null"},
                                                "street": {"type": "string"},
                                                "house": {"type": "integer"},
                                                "building": {"type": "null"},
                                                "apartment": {"type": "null"},
                                                "fias": {"type": "null"}
                                            }
                                        },
                                        "phone": {"type": "string"},
                                        "email": {"type": "string"}
                                    }
                                }
                            }
                        },
                        "drivers_min_age": {"type": "integer"},
                        "drivers_min_exp": {"type": "integer"},
                        "drivers": {
                            "type": "array",
                            "items": {
                                "anyOf": [
                                    {
                                        "type": "object",
                                        "required": ["birth_date", "last_name", "first_name", "middle_name", "sex",
                                                     "married", "children", "driver_license", "registration_address"],
                                        "properties": {
                                            "birth_date": {"type": "string"},
                                            "last_name": {"type": "string"},
                                            "first_name": {"type": "string"},
                                            "middle_name": {"type": "string"},
                                            "sex": {"type": "string"},
                                            "married": {"type": "boolean"},
                                            "children": {"type": "integer"},
                                            "driver_license": {
                                                "type": "object",
                                                "required": ["series", "number", "issue_date", "driving_experience_date"],
                                                "properties": {
                                                    "series": {"type": "string"},
                                                    "number": {"type": "string"},
                                                    "issue_date": {"type": "string"},
                                                    "driving_experience_date": {"type": "string"}
                                                }
                                            },
                                            "registration_address": {
                                                "type": "object",
                                                "required": ["country", "region", "city", "district", "street",
                                                             "house", "building", "apartment", "fias"],
                                                "properties": {
                                                    "country": {"type": "string"},
                                                    "region": {"type": "string"},
                                                    "city": {"type": "string"},
                                                    "district": {"type": "null"},
                                                    "street": {"type": "string"},
                                                    "house": {"type": "integer"},
                                                    "building": {"type": "null"},
                                                    "apartment": {"type": "null"},
                                                    "fias": {"type": "null"}
                                                }
                                            }
                                        }
                                    }
                                ]
                            }
                        },
                        "terms": {
                            "type": "object",
                        }
                    }
                }
            }
        }
    }
}