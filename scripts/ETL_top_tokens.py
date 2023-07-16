from utils.extract_CoinGecko import get_criptos_top
from utils.transform_df import transformation_top
from utils.load_redshift import load_to_redshift
from utils.pyspark import PySparkSession
class ETLTopTokens(PySparkSession):
    """
    Proceso ETL del top 100 de criptomonedas con mayor capitalizacion de mercado.
    """

    def __init__(self):
        super().__init__()
        self.table = "criptos_market_cap"
        self.URL_BASE = "https://api.coingecko.com/api/v3/"

    def extract(self):
        json = get_criptos_top(self.URL_BASE)
        return json
    
    def transform(self, json):
        df = transformation_top(json, self.spark)
        return df
     
    def load(self, df):
        load_to_redshift(df, self.table, self.REDSHIFT_URL, self.REDSHIFT_USER, self.REDSHIFT_PASSWORD)



if __name__ == "__main__":
    etl = ETLTopTokens()
    json = etl.extract()
    
    if isinstance(json, str):
        print('Error:', json)
    
    else:
        df = etl.transform(json)
        etl.load(df)