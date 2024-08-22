class SymbolTableEntry:
    def __init__(self, name, data_type, param_pos, is_call, num_args):
        self.name = name
        self.data_type = data_type
        self.param_pos = param_pos
        self.is_call = is_call
        self.num_args = num_args

class SymbbolTable:
    def __init__(self):
        self.table = {}

    def insert(self, entry):
        if entry.name in self.table:
            raise Exception(f"Duplicate identifier: {entry.name}")
        self.table[entry.name] = entry

    def lookup(self, name):
        return self.table.get(name)
    
    def delete(self, name):
        if name in self.table:
            del self.table[name]
