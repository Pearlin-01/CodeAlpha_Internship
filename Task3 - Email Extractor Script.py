import re

# Function to extract emails from a text file
def extract_emails(input_file, output_file):
    try:
        with open(input_file, 'r') as file:
            text = file.read()

        # Regex pattern for emails
        email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
        emails = re.findall(email_pattern, text)

        # Save unique emails to a new file
        with open(output_file, 'w') as out_file:
            for email in sorted(set(emails)):
                out_file.write(email + '\n')

        print(f"✅ Extracted {len(set(emails))} emails and saved to '{output_file}'")

    except FileNotFoundError:
        print("❌ Input file not found.")
    except Exception as e:
        print(f"⚠️ Error: {e}")

# Example usage
input_path = 'sample.txt'     # Input file containing text
output_path = 'emails.txt'    # Output file for extracted emails
extract_emails(input_path, output_path)
