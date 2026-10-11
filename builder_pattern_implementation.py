class House:
    def __init__(
        self,
        bedrooms,
        bathrooms,
        kitchen,
        garden,
        garage,
        pool,
        solar_panels,
        smart_home,
    ):
        self.bedrooms = bedrooms
        self.bathrooms = bathrooms
        self.kitchen = kitchen
        self.garden = garden
        self.garage = garage
        self.pool = pool
        self.solar_panels = solar_panels
        self.smart_home = smart_home

    def __str__(self):
        features = [
            f"Bedroom: {self.bedrooms}",
            f"Bathroom: {self.bathrooms}",
            f"Kitchen: {'Yes' if self.kitchen else 'No'}",
            f"Garden: {'Yes' if self.garden else 'No'}",
            f"Garage: {'Yes' if self.garage else 'No'}",
            f"Pool: {'Yes' if self.pool else 'No'}",
            f"Solar Panels: {'Yes' if self.pool else 'No'}",
            f"Smart Home: {'Yes' if self.smart_home else 'No'}",
        ]
        return " | ".join(features)


class HouseBuilder:
    def __init__(self):
        self.bedroom = 1
        self.bathroom = 1
        self.kitchen = True
        self.garden = True
        self.garage = True
        self.pool = False
        self.solar_panels = False
        self.smart_home = False

    def set_bedrooms(self, bedrooms):
        self.bedroom = bedrooms
        return self

    def set_bathrooms(self, bathrooms):
        self.bathroom = bathrooms
        return self

    def set_kitchen(self, kitchens):
        self.kitchen = kitchens
        return self

    def add_garden(self):
        self.garden = True
        return self

    def add_garage(self):
        self.garage = True
        return self

    def add_pool(self):
        self.pool = True
        return self

    def add_solar_panels(self):
        self.solar_panels = True
        return self

    def add_smart_home(self):
        self.smart_home = True
        return self

    def build(self):
        return House(
            self.bedroom,
            self.bathroom,
            self.kitchen,
            self.garden,
            self.garage,
            self.pool,
            self.solar_panels,
            self.smart_home,
        )
