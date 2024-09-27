#--------------------------------------------
# Step 1 - Creating Dataframe  (Snowpark)
#--------------------------------------------
# Session object as a parameter
# Table method in our session class to generate our dataframe, to connection of Snowflake database, calling existing table in Snowflake

#Create Function to create session object
def create_dataframe(session):

  #Use variable to define the session's method to retrieve Snowflake API table connectivity to an existing table
  df_table = session.table("SAMPLE_TABLE")

#Actions - show() and collect()
#Transformations 

#count method
df_table.count()
print(df_table.count())

#show method
df_table.show()

#collect method
df_result = df_tabke.collect()
print(df_results)

#TRANSOFRMATIONS
df_filtered = df_table.filter(col("AGE") >30)
