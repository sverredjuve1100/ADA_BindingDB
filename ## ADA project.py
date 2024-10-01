## ADA project.py
import pandas as pd
import sqlite3 as sql
import csv
import matplotlib.pyplot as plt

### Change this path to and the script should run
file_path = '/Users/sverredjuve/Downloads'

conn = sql.connect(file_path + '/BindingDB_all.db')

cursor = conn.cursor()

# Execute the query
# cursor.execute("""
#     SELECT DISTINCT "Target Source Organism According to Curator or DataSource"
#     FROM ada_table
#     WHERE "Target Source Organism According to Curator or DataSource" IS NOT NULL
#     ORDER BY "Target Source Organism According to Curator or DataSource"
# """)

# target = "Institution"
# target = "Target Name"
# target = "Number of Protein Chains in Target (>1 implies a multichain complex)"

# cursor.execute("""
#     SELECT DISTINCT "Target Name"
#     FROM ada_table
#     WHERE "Target Name" IS NOT NULL
#     ORDER BY "Target Name"
# """)

# # Fetch and print the results
# for row in cursor.fetchall():
#     print(row[0])

# conn.close()

query = """
SELECT "pH", COUNT(*) as count
FROM ada_table
WHERE "pH" IS NOT NULL
GROUP BY "pH"
ORDER BY count DESC
"""

# Execute the query and load results into a pandas DataFrame
df = pd.read_sql_query(query, conn)
#df = df.sort_values(by="pH")

# Close the database connection
conn.close()
print(df.head(55))
# Create the log plot
plt.figure(figsize=(10, 6))
plt.bar(range(len(df)), df['count'])
plt.yscale('log')
plt.xlabel('Target Names (sorted by frequency)')
plt.ylabel('Count (log scale)')
plt.title('Distribution of Target Name Frequencies')
plt.tight_layout()
plt.show()