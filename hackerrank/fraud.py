STATE_MAPPINGS = {
    'california': 'ca',
    'illinois': 'il',
    'new york': 'ny'
}

class Order:

    def __init__(self, csv_record):
        csv_values = csv_record.split(',')
        self._order_id = int(csv_values[0])
        self._deal_id = int(csv_values[1])
        self._email = csv_values[2]
        self._street_address = csv_values[3]
        self._city = csv_values[4]
        self._state = csv_values[5]
        self._zipcode = csv_values[6]

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
        username = username.replace('.', '')
        return '{}@{}'.format(username, domain)

    @property
    def canonical_address(self):
        if self._state.lower() in STATE_MAPPINGS:
            state = STATE_MAPPINGS[self._state.lower()]
        else:
            state = self._state
        zipcode = self._zipcode.replace('-','')
        canonical_address = '{},{},{},{}'.format(
            self._street_address,
            self._city,
            state,
            zipcode
        )
        return canonical_address.lower()
