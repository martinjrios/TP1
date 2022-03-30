class Coins:
    def __init__(self, file_name):
        self.quotes_file_path = file_name    

    def parse_data(self):
        try:
            with open(self.quotes_file_path, "r") as quotes_file:
                quotes_file.readline()
                coin_values_list = []
                for line in quotes_file:
                    coin_field_list = line.split(",")
                    coin_values_list.append({"id": coin_field_list[0], "name": coin_field_list[1], "value1": coin_field_list[2], "value2": coin_field_list[3]})
                
            return coin_values_list

        except Exception as e:
            print("Error al leer el archivo de cotizaciones: " + str(e))
            return []