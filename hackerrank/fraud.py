class Order:
    def __init__(self, csv_record):
        csv_values = csv_record.split(',')
        self._order_id = int(csv_values[0])
        self._deal_id = int(csv_values[1])
        self._email = csv_values[2]

    @property
    def order_id(self):
        return self._order_id

    @property
    def deal_id(self):
        return self._deal_id

    @property
    def canonical_email(self):
        canonical_email = self._email.lower()
        username, domain = canonical_email.split('@')
        username, _, _ = username.partition('+')
        return '{}@{}'.format(username, domain)
