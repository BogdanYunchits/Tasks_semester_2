import xml.etree.ElementTree as ET

def generate_xml_data():
    data = ET.Element("store")
    item1 = ET.SubElement(data, "item")
    item1.set("category", "electronics")
    ET.SubElement(item1, "name").text = "Laptop"
    ET.SubElement(item1, "price").text = "1000"

    item2 = ET.SubElement(data, "item")
    item2.set("category", "books")
    ET.SubElement(item2, "name").text = "Python Programming"
    ET.SubElement(item2, "price").text = "40"

    tree = ET.ElementTree(data)
    tree.write("products.xml")

generate_xml_data()

import xml.etree.ElementTree as ET

def process_xml_and_calculate_total(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    items = []
    for item in root.findall("item"):
        name = item.find("name").text
        price = float(item.find("price").text)
        category = item.get("category")
        items.append({"name": name, "price": price, "category": category})

    items.sort(key=lambda x: x["price"])
    total_price = sum(item["price"] for item in items)

    print("Items sorted by price:")
    for item in items:
        print(f"{item['name']} ({item['category']}): {item['price']}")

    print(f"\nTotal price of all items: {total_price}")

process_xml_and_calculate_total("products.xml")
