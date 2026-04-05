import datetime

class AIPrediction:
    def __init__(self, stock_level, sales_rate, buffer_stock):
        self.stock_level = stock_level
        self.sales_rate = sales_rate
        self.buffer_stock = buffer_stock

    def calculate_refill_date(self):
        days_to_refill = (self.stock_level - self.buffer_stock) / self.sales_rate
        refill_date = datetime.datetime.utcnow() + datetime.timedelta(days=days_to_refill)
        return refill_date.strftime('%Y-%m-%d %H:%M:%S')

    def stock_status(self):
        if self.stock_level <= self.buffer_stock:
            return 'Reorder Needed'
        elif self.stock_level < self.buffer_stock * 2:
            return 'Low Stock'
        else:
            return 'In Stock'


# Example usage:
# prediction = AIPrediction(stock_level=100, sales_rate=10, buffer_stock=20)
# print(prediction.calculate_refill_date())
# print(prediction.stock_status())