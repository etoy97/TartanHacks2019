import mintapi
mint = mintapi.Mint(
    'eiyou98@gmail.com',  # Email used to log in to Mint
    'Mint1234!!',  # Your password used to log in to mint
    # Optional parameters
    mfa_method='sms',  # Can be 'sms' (default) or 'email'.
                       # if mintapi detects an MFA request, it will trigger the requested method and prompt on the command line.
    headless=False,  # Whether the chromedriver should work without opening a
                     # visible window (useful for server-side deployments)
    mfa_input_callback=None,  # A callback accepting a single argument (the prompt)
                              # which returns the user-inputted 2FA code. By default
                              # the default Python `input` function is used.
    session_path=None, # Directory that the Chrome persistent session will be written/read from.
                       # To avoid the 2FA code being asked for multiple times, you can either set
                       # this parameter or log in by hand in Chrome under the same user this runs
                       # as.
  )

transactions = mint.get_transactions() # as pandas dataframe


export_csv = transactions.to_csv(r'C:\Users\ellio\Documents\TartanHacks2019\data.csv')

#print (len(transactions))
#mint.get_transactions_csv(include_investment=False) # as raw csv data

