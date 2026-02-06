class userData:
    def __init__(self, Name, Age):
        self.user_name = Name
        self.age = Age

    def print_info(self):
        print(f"User:{self.user_name},Age:{self.age}")
    
    def process_data(DataList):
        result = []
        for d in DataList:
            if d.age > 18:
                result.append(d.user_name.upper())
        return result
