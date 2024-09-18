https://learn.snowflake.com/courses/course-v1:snowflake+LVLUP-307+A/courseware/fbda2df3329e4e53b9fa427c5980ce0d/f3f35ff5033e4f738af23663fa547a31/?child=first

Knowledge Check:
https://learn.snowflake.com/courses/course-v1:snowflake+LVLUP-307+A/course/
######################################################################################
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

######################################################################################
import snowflake.snowpark as snowpark
from snowflake.snowpark.functions import col, udf
from snowflake.snowpark.types import StringType

def main(session: snowpark.Session):

  #Create an anonymous UDF
  capitalize_udf = udf(lambda s: s.capitalize(), return_type=StringType(), input_types=[StringType()])

  #Create a DataFrame with a sample string
  df = session.create_dataframe([["hello testing]]).to_df("example_column")
  #Apply the anomymous UDF to the DataFrame
  df_with_udf = df.select(capitalize_udf(col("example_column)).alias("capitalize column"))
  
                                  
   #Display result
  df_with_udf.show()
  return df_with_udf

