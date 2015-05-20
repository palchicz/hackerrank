class Node:

    def __init__(self, index, key,
                candidate, ciper_words, encoding_table):
        self.index = index
        self.key = key
        self.candidate = candidate
        self.ciper_words = ciper_words
        self.encoding_table = encoding_table

    @property
    def neighbors(self):
        return []

def get_root_node(cipher_words, encoding_table):
    return Node(-1, {}, '', cipher_words, encoding_table)

def filter_candidates(candidates, table, cipher):
    filtered = []
    for candidate in candidates:
        if _is_encryptable(candidate, table, cipher):
            filtered.append(candidate)

    return filtered

def _is_encryptable(plaintext, table, cipher):
    for pos, letter in enumerate(plaintext):
        if letter in table:
            if table[letter] != cipher[pos]:
                return False
        else:
            if cipher[pos] in table.values():
                return False
    return True

