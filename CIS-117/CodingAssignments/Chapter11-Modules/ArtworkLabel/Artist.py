class Artist:
    # TODO: Define constructor with parameters to initialize instance attributes
    #       (name, birth_year, death_year)
    def __init__(self, name = 'unknown', birth=-1, death=-1):
        self.name = name
        self.birth_year = birth
        self.death_year = death

    def print_info(self):
        if self.birth_year >= 0 and self.death_year >= 0:
            print(f'Artist: {self.name} ({self.birth_year} to {self.death_year})')
        elif self.birth_year >= 0: 
            print(f'Artist: {self.name} ({self.birth_year} to present)')
        else:
            print(f'Artist: {self.name} (unknown)')
            