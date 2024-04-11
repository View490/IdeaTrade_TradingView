import mysql.connector
import csv

def main():
    # SELECT TABLE Program_Trading_SET_and_Mai >>> PRINT VALUES

    
    conn = mysql.connector.connect(
        host = 'ideatrade.serveftp.net',
        user = 'Sura@view',
        password = 'ZP6HpF-T04CGw_t(',
        database = 'db_ideatrade',
        port = 51410
        )

    # Create a cursor object using the cursor() method
    cursor = conn.cursor()

    # Define the table name with spaces
    table_name = "allsymbol_global"

    # Define your SQL query to select all rows from the table
    select_query = """
            SELECT Symbol, Exchange 
            FROM `{}` 
            # LIMIT 10
        """.format(table_name)

    # Execute the query
    cursor.execute(select_query)

    # Fetch all rows
    head = cursor.description
    print('head: ',[head_info[0] for head_info in head])
    rows = cursor.fetchall()

    # Close cursor and connection
    cursor.close()
    conn.close()

    ##################################


    def convert_to_csv(data, filename):
        with open(filename, 'w', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow(['symbol', 'exchange'])  # Write header
            csv_writer.writerows(data)

    # Sample list of tuples
    data = [
        ('AAPL', 'NASDAQ'),
        ('GOOGL', 'NASDAQ'),
        ('MSFT', 'NASDAQ'),
        ('AMZN', 'NASDAQ'),
        ('TSLA', 'NASDAQ')
    ]

    filename = "symbols_and_exchanges.csv"
    convert_to_csv(rows, filename)
    print(f"CSV file '{filename}' has been created.")



if __name__=="__main__":
    main()