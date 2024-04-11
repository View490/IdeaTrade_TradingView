from tvDatafeed import TvDatafeed, Interval
import csv
import pandas as pd
from tqdm import tqdm
import os

import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

TimeFrames = [
    "Interval.in_1_minute"
    ,"Interval.in_3_minute"
    ,"Interval.in_5_minute"
    ,"Interval.in_15_minute"
    ,"Interval.in_30_minute"
    ,"Interval.in_45_minute"
    ,"Interval.in_1_hour"
    ,"Interval.in_2_hour"
    ,"Interval.in_3_hour"
    ,"Interval.in_4_hour"
    ,"Interval.in_daily"
    ,"Interval.in_weekly"
    ,"Interval.in_monthly"
]
df = pd.DataFrame(columns=['datetime', 'symbol','open','high','low','close','volume', 'TimeFrame'])

done_timeframe = []
done_symbol = [0] * len(TimeFrames)

def login_tv(user='', password=''):
    if (user != '' & password != ''):
        tv = TvDatafeed(user, password)
    else:
        tv = TvDatafeed()
    return tv


def get_daily_stock(symbol='PTT', exchange='SET', interval="Interval.in_daily", tv=TvDatafeed()):
    data_daily = tv.get_hist(
        symbol=symbol, 
        exchange=exchange, 
        interval=eval(interval),
        n_bars=5442
        )
    return data_daily

def get_df_daily_stock(TimeFrame=Interval.in_daily, csv_path='./symbols_and_exchanges.csv', df=df, tv=TvDatafeed()):
    current_idx_path = 'current_idx.csv'
    if not os.path.exists(current_idx_path):
        with open(current_idx_path, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['TimeFrame', 'current_idx'])
            # csv_writer.writerow(["Symbol"] + ['TimeFrame'])
    
    with open(csv_path, 'r') as csvfile:
        row_count = sum(1 for row in csv.reader(csvfile))
    
    # Read the CSV file into a pandas DataFrame
    tmp = pd.read_csv(csv_path)
    symbol_index = tmp.columns.get_loc('Symbol')
    exchange_index = tmp.columns.get_loc('Exchange')
    
    current_pd = pd.read_csv(current_idx_path)
    print('pd current', current_pd)
    if str(TimeFrame) in current_pd['TimeFrame'].values:
        matching_row = current_pd[current_pd['TimeFrame'] == str(TimeFrame)]
        if matching_row['current_idx'].values == row_count-1:
            start_scrapping = False
        else:
            start_scrapping = True
    else:
        current_pd = current_pd.append({'TimeFrame': str(TimeFrame), 'current_idx': 0}, ignore_index=True)
        start_scrapping = True
    
    start_iteration = False
    if start_scrapping:
        print('[INITIAL] DF length = ', len(df), 'TimeFrame = ',TimeFrame)
        done_timeframe.append(TimeFrame)
        with open(csv_path, 'r') as csvfile:
            print('TOTAL = ',row_count)
            datareader = csv.reader(csvfile)
            for idx, row in enumerate(tqdm(datareader)):
                if idx == current_pd.at[current_pd.index[current_pd['TimeFrame'] == str(TimeFrame)][0], 'current_idx']:
                    start_iteration = True
                    print('start at current_idx = ',idx)
                if not start_iteration:
                    continue
                if idx >0:
                    data = get_daily_stock(symbol=row[symbol_index], exchange=row[exchange_index], tv=tv, interval=TimeFrame)
                    if data is None:
                        print('*** [ERROR] ',row)
                        continue
                    # print('[TimeFrame]{} [SYMBOL]{} \t[LEN]{}'.format(TimeFrame,row,len(data)))
                    data['TimeFrame']=str(Interval.in_1_minute).split('.in_')[-1]
                    data.reset_index(inplace=True)
                    df = df.append(data, ignore_index=True)
                    if idx % 5 == 0:
                        df.to_csv(r'df_all_timeframe.csv', index=False)
                        row_index = current_pd.index[current_pd['TimeFrame'] == str(TimeFrame)][0]
                        current_pd.at[row_index, 'current_idx'] = idx
                        current_pd.to_csv(current_idx_path, index=False)
                        done_symbol[len(done_timeframe)-1] = idx
                        for idx_tf, element_timeframe in enumerate(done_timeframe):
                            element_symbol = done_symbol[idx_tf]
                            print(f'>>> [status] TimeFrame={element_timeframe}, #symbol = {element_symbol}/{row_count}')
        df.dropna()
        return df

def main():
    TimeFrames = [
        "Interval.in_1_minute"
        ,"Interval.in_3_minute"
        ,"Interval.in_5_minute"
        ,"Interval.in_15_minute"
        ,"Interval.in_30_minute"
        ,"Interval.in_45_minute"
        ,"Interval.in_1_hour"
        ,"Interval.in_2_hour"
        ,"Interval.in_3_hour"
        ,"Interval.in_4_hour"
        ,"Interval.in_daily"
        ,"Interval.in_weekly"
        ,"Interval.in_monthly"
        ]
    df = pd.DataFrame(columns=['datetime', 'symbol','open','high','low','close','volume', 'TimeFrame'])

    done_timeframe = []
    done_symbol = [0] * len(TimeFrames)

    for idx, TimeFrame in enumerate(TimeFrames):
        if idx==0:
            df = get_df_daily_stock(TimeFrame=TimeFrame)
        else:
            df = get_df_daily_stock(TimeFrame=TimeFrame, df=df)
        print('>>> [status] length df = {}, \t TimeFrame={}'.format(len(df), TimeFrame))
    df.to_csv(r'df_all_timeframe.csv', index=False)
 
if __name__=="__main__":
    main()
