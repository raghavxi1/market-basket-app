import pandas as pd
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import apriori, association_rules

# Sample transaction data (more varied and larger dataset)
transactions = [
    ['Milk', 'Bread', 'Butter'],
    ['Beer', 'Bread'],
    ['Milk', 'Bread'],
    ['Beer', 'Diapers'],
    ['Milk', 'Diapers', 'Bread', 'Butter'],
    ['Bread', 'Butter'],
    ['Milk', 'Diapers', 'Beer', 'Cola'],
    ['Milk', 'Bread', 'Butter'],
    ['Cola', 'Beer'],
    ['Milk', 'Diapers', 'Bread'],
    ['Milk', 'Bread', 'Butter'],
    ['Diapers', 'Beer'],
    ['Milk', 'Cola'],
    ['Bread', 'Butter'],
    ['Diapers', 'Bread', 'Beer'],
    ['Milk', 'Beer', 'Diapers', 'Cola'],
]

# Convert to one-hot encoded format
te = TransactionEncoder()
te_ary = te.fit(transactions).transform(transactions)
df = pd.DataFrame(te_ary, columns=te.columns_)

# Generate frequent itemsets with a reasonable support threshold
frequent_itemsets = apriori(df, min_support=0.2, use_colnames=True)

# Generate association rules from the frequent itemsets
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

# Check if the rules dataframe is empty, if so print a message
if rules.empty:
    print("No rules generated. Consider adjusting support and lift thresholds.")
else:
    print(f"Generated {len(rules)} association rules.")

# Save the rules to a CSV file
rules.to_csv("association_rules.csv", index=False)
print("✅ association_rules.csv generated successfully.")
