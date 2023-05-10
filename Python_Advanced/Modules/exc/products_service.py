from  json import loads

def get_all_products():
    with open('.\\products.txt', 'r') as products_file:
        result = []
        for line in products_file:
            product = loads(line.strip())
            result.append(product)
        return result