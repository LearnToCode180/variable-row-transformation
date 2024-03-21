# Transforming Column Variables to Rows

In some scientific projects, collecting data is founded on both observations and measurement taken from sites within various ecosystems. This data is gathered mostly in **CSV tables**. Each table may contain diverse information and caracteristics about the measurements conducted, which describe the context where variables have been measured. Common contexts include *date*, *time*, *site*, *block*, *plot*, *trial*, *treatment*... The variables measured are represented as columns within these tables alongside their contextual information. Consequently, each row in the table represents the values of variables as well as the their respective contextual details.

Sometimes, depending on requirements, it's preferable having two columns '**variable**' and '**value**' instead of having all variables in separate columns. This arrangement can facilitate certain tasks,  where filtering on variable names in **SQL queries**. When a variable name is passed as a parameter in queries, it cannot directly function as a column, it can only be used within a *WHERE clause*. Therefore, having a column 'variable' that encompasses all  variables in the table enables filtering based on variable names.

After this transformation, the number of rows will be multipliyed by the number of variables, but dynamically passing the names of variables to queries won't pose any problem.

The script used for that was written in Python-3 using the **Pandas** library.

You have a CSV file *test_data.csv* which you can download and try the code on it. It contains three variables *precip_cum*, *air_temp_avg*, and *wind_speed* with arbitrary values.

You should precise in the command the **CSV file** as the first parameter, the **separator employed** as the second one, and finally the **names of variables** existed in the file. An error is raised if one of the variables provided is incorrect. Don't forget to put the separator between a single quotes so that it'll not be considered as a special caracter.

Here is the command to run for this file:

```
foo@bar:~$ python3 variableRow_Transformation.py test_data.csv , precip_cum air_temp_avg wind_speed
```

A new file is generated in the same directory, and it has the same name of the original file preceeded by 'new' thus 'new_test_data.csv'.