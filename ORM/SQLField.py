class SQLField:
    def __init(self, columnNum, name, field_type, is_primary_key=False, length=0):
        self.columnNum = columnNum
        self.name = name
        self.field_type = field_type
        self.isPrimaryKey = is_primary_key
        self.length = length