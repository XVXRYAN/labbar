from data import create_data
from diagram import show_histogram

analyze_data = create_data()

print("Antal värden:", len(analyze_data))
print("Första tio värdena:", analyze_data[:10])

show_histogram(analyze_data)