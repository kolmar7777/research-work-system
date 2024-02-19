import yfinance as yf
import pandas as pd
import os

class DataLoader:
    def init(self, path: str = "./data",
             # load_from_file: bool = False,
             # load_simfin: bool = False,
             # load_yfinance: bool = True
            ):
        self.path = path
        # self.load_from_file: bool = False,
        # self.load_simfin: bool = False,
        # self.load_yfinance: bool = True
    def load_data(self, load_source: str = "yfinance") -> pd.DataFrame:
        if load_source == "yfinance":
            data = self.load_yfinance()
        elif load_source == "simfin":
            data = self.load_simfin()
        elif load_source == "file":
            data = self.load_file()
        else:
            raise ValueError("load_source not in list ['yfinance', 'simfin', 'file']\n")
        return data
        
    def load_yfinance(self, companies: str = "",
                      start_time: str = '2020-01-01',
                      end_time: str = '2023-12-31',
                      period: str = "1d",
                      save_data: bool = True
                     ) -> pd.DataFrame:
        if not companies:
            companies = 'VZ UNH JNJ PG MRK RTX KO WBA MMM WMT MSFT IBM INTC AAPL CSCO '
            companies += 'NKE CAT PFE XOM MCD JPM HD V GS DIS AXP CVX TRV BA' # DOW
        data = yf.download(companies, start_time, end_time, group_by="column", period=period)
        if save_data:
            data.to_csv(os.path.join("./", "data", "data.csv"))
        return data
    
    def load_simfin(self) -> pd.DataFrame:
        return pd.DataFrame()
    
    def load_file(self, path: str = os.path.join("./", "data"),
                  filename: str = "") -> pd.DataFrame:
        if filename:
            return pd.read_csv(path + filename)
        else:
            return pd.read_csv(path + "data.csv")
    