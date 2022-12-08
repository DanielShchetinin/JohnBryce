companies = {
    'Intel': 
        {
        'company_name': 'Intel',
        'ticker': 'INTC',
        'employees': 121100,
        'adress': '2200 Mission College Blvd, Santa Clara, CA',
        'CEO': 'Patrick P. Gelsinger',
        'stocks_data': {
            27_11_2022: { 
                'open_price': 29.10,
                'close price': 30.20,
                'volume': 3000
            },
            
             28_11_2022: {
                'open_price': 30.20,
                'close price': 32.50,
                'volume': 7000
            }
            
        }

    }
}

print(companies['Intel']['stocks_data'][27_11_2022]['volume'])