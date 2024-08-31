#Tabela só terá os paramentros, e variáveis locais

class SymbolTableEntry:
    def __init__(self, name, data_type, param_pos, is_call, num_args, args):
        self.name = name
        self.data_type = data_type
        self.param_pos = param_pos
        self.is_call = is_call
        self.num_args = num_args
        self.args = args

class SymbolTable:
    def __init__(self):
        self.table = {}

    def insert(self, entry):
        if entry.name in self.table:
            raise Exception()
        self.table[entry.name] = entry

    def lookup(self, name):
        return self.table.get(name)
    
    def delete(self, name):
        if name in self.table:
            del self.table[name]

    def __str__(self):
        return '\n'.join(f"{name.ljust(15)}| {name.ljust(15)}| {str(entry.data_type).ljust(15)}| {str(entry.param_pos).ljust(15)}| {str(entry.is_call).ljust(15)}| {str(entry.num_args).ljust(15)}| {entry.args}"
                         for name, entry in self.table.items())