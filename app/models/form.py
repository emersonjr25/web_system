from flask_wtf import FlaskForm
from wtforms import FloatField
from wtforms.validators import DataRequired

class MachineTwo(FlaskForm):
    Lot_size = FloatField('Lot_size', validators=[DataRequired()])
    Year_built = FloatField('Year_built', validators=[DataRequired()])
    Overall_material = FloatField('Overall_material', validators=[DataRequired()])
    Overall_condition = FloatField('Overall_condition', validators=[DataRequired()])
    Remodel_date = FloatField('Remodel_date', validators=[DataRequired()])
    Masonry_veneer = FloatField('Masonry_veneer', validators=[DataRequired()])
    First_Floor_square = FloatField('First_Floor_square', validators=[DataRequired()])
    Second_Floor_square = FloatField('Second_Floor_square', validators=[DataRequired()])
    Above_grade_Area = FloatField('Above_grade_Area', validators=[DataRequired()])
    Full_bathrooms = FloatField('Full_bathrooms', validators=[DataRequired()])
    Number_Bedrooms_above_base = FloatField('Number_Bedrooms_above_base', validators=[DataRequired()])
    Number_Kitchens = FloatField('Number_Kitchens', validators=[DataRequired()])
    Total_rooms_above_base = FloatField('Total_rooms_above_base', validators=[DataRequired()])
    Size_garage = FloatField('Size_garage', validators=[DataRequired()])
    Pool_area = FloatField('Pool_area', validators=[DataRequired()])