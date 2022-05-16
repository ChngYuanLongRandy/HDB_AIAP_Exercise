from sklearn.preprocessing import StandardScaler, OrdinalEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

class DataPipeline():

    def __init__(self, model_type, model_params: dict):
        self.model_type = model_type
        self.model_params = model_params


    def 