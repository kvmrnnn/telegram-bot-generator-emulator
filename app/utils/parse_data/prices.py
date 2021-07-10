from loguru import logger


class ParserPrice:
    path_to_prices = './app/data/cache/prices.txt'

    @staticmethod
    def get_price(goods_category: str, default_price: float = 99):
        with open(ParserPrice.path_to_prices, encoding='UTF-8') as file:
            categories = file.readlines()

        for category in categories:
            if goods_category in category:
                price = category.split(':')[-1]
                return float(price)

        ParserPrice.set_price(goods_category, default_price)

        return default_price

    @staticmethod
    def set_price(goods_category: str, price: float):
        with open(ParserPrice.path_to_prices, encoding='UTF-8') as file:
            categories = file.readlines()
        categories_new = []
        for category in categories:
            if goods_category in category or category == '\n':
                continue
            categories_new.append(category.strip())
        categories_new.append(f'{goods_category}:{float(price)}')

        with open(ParserPrice.path_to_prices, 'w', encoding='UTF-8') as file:
            file.write('\n'.join(categories_new))
