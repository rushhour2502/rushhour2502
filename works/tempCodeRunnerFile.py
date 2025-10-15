# Extract table data (details about the system)
# table = soup.find('table')
# rows = table.find_all('tr')

# # Create a dictionary to store the details
# details = {}

# # Extract key-value pairs from the table rows
# for row in rows:
#     cols = row.find_all('td')
#     if len(cols) == 2:
#         key = cols[0].text.strip()
#         value = cols[1].text.strip()
#         details[key] = value

# # Print system details in a clean format
# for key, value in details.items():
#     print(f"{key}: {value}")

# # Extract the Errors section
# errors_section = soup.find('h4', text="Errors")
# error_logs = errors_section.find_next('div', class_="error-log-entry")

# # Clean and display the error logs
# error_header = error_logs.find('div', class_="log-entry-header").text.strip()
# error_description = error_logs.find('div', class_="log-entry-description").text.strip()
# error_table = error_logs.find('table').find_all('tr')

# # Display the error details
# print(f"\nError: {error_header}")
# print(f"Description: {error_description}")

# # Display error device details
# for row in error_table:
#     cols = row.find_all('td')
#     if len(cols) == 2:
#         key = cols[0].text.strip()
#         value = cols[1].text.strip()
#         print(f"{key}: {value}")