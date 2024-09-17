import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col, udf
from snowflake.snowpark.types import StringType

def main(session: snowpark.Session):
  @udf(name="capitalize_first", is_permanent=True, stage_location="@my_stage", replace=True)
  def capitalize_first(s: str) -> str:
    return s.capitalize()

#Create a DataFrame with a sample string
df = session.create_dataframe([["hello testing]]).to_df("example_column")

#Apply the UDF to the DataFrame
df_with_udf = df.select(capitalize_first(col("example_column")))

#Display result
df_with_udf.show()
return df_with_udf



