import sys
import pandas as pd

csv_file = sys.argv[1]
sep = sys.argv[2]
try:
    df = pd.read_csv(csv_file, sep=sep, dtype=object)
    if len(df.columns) > 1:
        vars = {}
        for i in range(3, len(sys.argv)):
            try:
                vars[sys.argv[i]] = df[sys.argv[i]]
            except KeyError as e:
                print(f"ERROR: This column name {e} doen't exist or it's incorrect! \n\
       The transformation cannot be done\n \n ********************************* \n ")
                sys.exit(1)

        df = df.drop(vars.keys(), axis=1)
        df['variable'], df['valeur'] = pd.Series(), pd.Series()

        for var,val in vars.items():
            if pd.isna(df['valeur'][0]):
                df['variable'] = var
                df['valeur'] = val
            else:
                df_copy = df.copy()
                df_copy['variable'] = var
                df_copy['valeur'] = val
                df = pd.concat([df, df_copy], axis=0, ignore_index=True)

        df.columns = map(str.lower, df.columns)
        df.to_csv('new_'+csv_file, index=False)

        print('The new table was generated successfully! You can find it in the same directory of the old one.\n')
        print('Here is the top part of the table:\n')
        print(df.head())
        print('\nAnd here is the end of the file:\n')
        print(df.tail())
    else:
        print("ERROR: The separator provided is incorrect! Make sure to provide the good one.")

except pd.errors.ParserError:
    print("ERROR: The separator provided is incorrect! Make sure to provide the good one.")