from app import db

class Machine():
    __tablename__ = 'machine_learning'

    id = db.Column(db.Integer)
    Lot_size = db.Column(db.Float)
    Year_built = db.Column(db.Float)
    Overall_material = db.Column(db.Float)
    Overall_condition = db.Column(db.Float)
    Remodel_date = db.Column(db.Float)
    Masonry_veneer = db.Column(db.Float)
    First_Floor_square = db.Column(db.Float)
    Second_Floor_square = db.Column(db.Float)
    Above_grade_Area = db.Column(db.Float)
    Full_bathrooms = db.Column(db.Float)
    Number_Bedrooms_above_base = db.Column(db.Float)
    Number_Kitchens = db.Column(db.Float)
    Total_rooms_above_base = db.Column(db.Float)
    Size_garage = db.Column(db.Float)
    Pool_area = db.Column(db.Float)

    def _init__(self, Lot_size, Year_built, Overall_material, Overall_condition, Remodel_date, Masonry_veneer, First_Floor_square, Second_Floor_square, Above_grade_Area, Full_bathrooms, Number_Bedrooms_above_base, Number_Kitchens, Total_rooms_above_base, Size_garage, Pool_area):
        self.Lot_size = Lot_size
        self.Year_built = Year_built
        self.Overall_material = Overall_material
        self.Overall_condition = Overall_condition
        self.Remodel_date = Remodel_date
        self.Masonry_veneer = Masonry_veneer
        self.First_Floor_square = First_Floor_square
        self.Second_Floor_square = Second_Floor_square
        self.Above_grade_Area = Above_grade_Area
        self.Full_bathrooms = Full_bathrooms
        self.Number_Bedrooms_above_base = Number_Bedrooms_above_base
        self.Number_Kitchens = Number_Kitchens
        self.Total_rooms_above_base = Total_rooms_above_base
        self.Size_garage = Size_garage
        self.Pool_area = Pool_area
    
    def __repr__(self):
        return '<ID %r>' % self.id