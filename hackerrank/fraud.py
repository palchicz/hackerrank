import re

STATE_MAPPINGS = {
    'california': 'ca',
    'illinois': 'il',
    'new york': 'ny'
}
STREET_MAPPINGS = {
    'st.': 'street',
    'rd.': 'road'
}
STREET_SUFFIX_RE = re.compile(r'\b([\w.]+)$')

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
        street_address = self._get_canonical_street_address()
        state = self._get_canonical_state()
        zipcode = self._zipcode.replace('-','')
        canonical_address = '{},{},{},{}'.format(
            street_address,
            self._city,
            state,
            zipcode
        )
        return canonical_address.lower()

    def _get_canonical_state(self):
        if self._state.lower() in STATE_MAPPINGS:
            state = STATE_MAPPINGS[self._state.lower()]
        else:
            state = self._state
        return state

    def _get_canonical_street_address(self):
        street_suffix = re.search(
            STREET_SUFFIX_RE,
            self._street_address
        ).group(0).lower()
        if street_suffix in STREET_MAPPINGS:
            street_address = re.sub(
                STREET_SUFFIX_RE,
                STREET_MAPPINGS[street_suffix],
                self._street_address,
            )
        else:
            street_address = self._street_address
        return street_address
