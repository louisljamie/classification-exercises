import pandas as pd


# Make a function named get_titanic_data that returns the titanic data from the codeup data science database
# as a pandas data frame. Obtain your data from the Codeup Data Science Database.

def get_titanic_data():
    sql_query = 'SELECT * FROM passengers'
    return pd.read_sql(sql_query, get_db_url('titanic_db'))


# Make a function named get_iris_data that returns the data from the iris_db on the codeup data science database
# as a pandas data frame. The returned data frame should include the actual name of the species in addition to the
# species_ids. Obtain your data from the Codeup Data Science Database.

def get_iris_data():
    sql_query = 'SELECT * FROM measurements JOIN species USING(species_id)'
    return pd.read_sql(sql_query, get_db_url('iris_db'))


# Make a function named get_telco_data that returns the data from the telco_churn database in SQL. In your SQL,
# be sure to join contract_types, internet_service_types, payment_types tables with the customers table, so that
# the resulting dataframe contains all the contract, payment, and internet service options. Obtain your data from
# the Codeup Data Science Database.

def get_telco_data():
    sql_query = 'SELECT * FROM telco_churn'
    return pd.read_sql(sql_query, get_db_url('telco_churn_db'))



# Once you've got your get_titanic_data, get_iris_data, and get_telco_data functions written, now it's time to add
# caching to them. To do this, edit the beginning of the function to check for the local filename of telco.csv,
# titanic.csv, or iris.csv. If they exist, use the .csv file. If the file doesn't exist, then produce the SQL and
# pandas necessary to create a dataframe, then write the dataframe to a .csv file with the appropriate name.

def get_titanic_data():
    sql_query = 'SELECT * FROM telco_churn'
    return pd.read_sql(sql_query, get_db_url('titanic_db'))
