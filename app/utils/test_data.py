from app.models.organizations import (
    Activity,
    Organization,
    OrganizationActivity,
    OrganizationPhoneNumber,
)
from app.models.buildings import Building

activities = [
    Activity(id=1, name="Еда"),
    Activity(id=2, name="Молочная продукция", parent_id=1),
    Activity(id=3, name="Мясная продукция", parent_id=1),
    Activity(id=4, name="Сыры", parent_id=2),
    Activity(id=5, name="Молоко", parent_id=2),
    Activity(id=6, name="Свинная продукция", parent_id=3),
    Activity(id=7, name="Говяжая продукция", parent_id=3),
    Activity(id=8, name="Транспорт"),
    Activity(id=9, name="Воздушный транспорт", parent_id=8),
    Activity(id=10, name="Наземный транспорт", parent_id=8),
    Activity(id=11, name="Колесный транспорт", parent_id=10),
    Activity(id=12, name="Железнодорожный транспорт", parent_id=10),
]

buildings = [
    Building(
        id=1,
        address="Страна 1, город 1, улица 1, дом 1",
        longitude=10.123456,
        latitude=10.123456,
    ),
    Building(
        id=2,
        address="Страна 1, город 1, улица 1, дом 2",
        longitude=10.123556,
        latitude=10.123556,
    ),
    Building(
        id=3,
        address="Страна 1, город 2, улица 1, дом 2",
        longitude=13.123556,
        latitude=12.123556,
    ),
]

organizations = [
    Organization(id=1, name="Молочная компания", building_id=1),
    Organization(id=2, name="Сырная компания", building_id=2),
    Organization(id=3, name="Творожная компания", building_id=3),
    Organization(id=4, name="Свинная компания", building_id=3),
    Organization(id=5, name="Фаршированная компания", building_id=2),
    Organization(id=6, name="Говяжья компания", building_id=1),
    Organization(id=7, name="Корабельная компания", building_id=2),
    Organization(id=8, name="Автобусная компания", building_id=2),
    Organization(id=9, name="Железнодорожная компания", building_id=3),
    Organization(id=10, name="Самолетная компания", building_id=1),
    Organization(id=11, name="Вертолетная компания", building_id=2),
    Organization(id=12, name="Автомобильная компания", building_id=3),
    Organization(id=13, name="Транспортная компания", building_id=1),
]

company_activities = [
    OrganizationActivity(organization_id=1, activity_id=2),
    OrganizationActivity(organization_id=1, activity_id=4),
    OrganizationActivity(organization_id=1, activity_id=5),
    OrganizationActivity(organization_id=2, activity_id=4),
    OrganizationActivity(organization_id=3, activity_id=2),
    OrganizationActivity(organization_id=4, activity_id=3),
    OrganizationActivity(organization_id=4, activity_id=6),
    OrganizationActivity(organization_id=5, activity_id=3),
    OrganizationActivity(organization_id=6, activity_id=7),
    OrganizationActivity(organization_id=8, activity_id=10),
    OrganizationActivity(organization_id=8, activity_id=11),
    OrganizationActivity(organization_id=9, activity_id=12),
    OrganizationActivity(organization_id=10, activity_id=9),
    OrganizationActivity(organization_id=11, activity_id=9),
    OrganizationActivity(organization_id=12, activity_id=8),
    OrganizationActivity(organization_id=12, activity_id=10),
    OrganizationActivity(organization_id=12, activity_id=11),
    OrganizationActivity(organization_id=13, activity_id=8),
]

company_phone_numbers = [
    OrganizationPhoneNumber(organization_id=1, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=1, phone_number="8(777)3244333"),
    OrganizationPhoneNumber(organization_id=2, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=2, phone_number="3456654323"),
    OrganizationPhoneNumber(organization_id=3, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=3, phone_number="88885695566"),
    OrganizationPhoneNumber(organization_id=4, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=4, phone_number="5526549878"),
    OrganizationPhoneNumber(organization_id=5, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=5, phone_number="99997865432"),
    OrganizationPhoneNumber(organization_id=6, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=7, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=7, phone_number="55554446598"),
    OrganizationPhoneNumber(organization_id=8, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=9, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=9, phone_number="88854568978"),
    OrganizationPhoneNumber(organization_id=10, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=10, phone_number="99089996545"),
    OrganizationPhoneNumber(organization_id=11, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=12, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=12, phone_number="8546856985"),
    OrganizationPhoneNumber(organization_id=13, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=13, phone_number="0123456789"),
    OrganizationPhoneNumber(organization_id=13, phone_number="55554445566"),
    OrganizationPhoneNumber(organization_id=13, phone_number="56664445588"),
]

test_data1 = []
test_data1.extend(activities)
test_data1.extend(buildings)
test_data1.extend(organizations)
test_data2 = []
test_data2.extend(company_activities)
test_data2.extend(company_phone_numbers)
