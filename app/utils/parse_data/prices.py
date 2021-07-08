from loguru import logger


class ParserPrice:
    path_to_prices = './app/data/cache/prices.txt'

    @staticmethod
    def get_price(good_category: str):
        with open(ParserPrice.path_to_prices, encoding='UTF-8') as file:
            categories = file.readlines()

        for category in categories:
            if good_category in category:
                price = category.split(':')[-1]
                return int(price)

    @staticmethod
    def set_price(good_category: str, price):
        with open(ParserPrice.path_to_prices, encoding='UTF-8') as file:
            categories = file.readlines()
        categories_new = []
        for category in categories:
            if good_category in category or category == '\n':
                continue
            categories_new.append(category.strip())
        categories_new.append(f'{good_category}:{price}')

        with open(ParserPrice.path_to_prices, 'w', encoding='UTF-8') as file:
            text_prices = ' '.join(categories_new)
            logger.debug(text_prices)
            categories = file.write('\n'.join(categories_new))
