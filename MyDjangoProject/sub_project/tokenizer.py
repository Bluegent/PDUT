import re


def tokenize(input_string):
    # Define the regular expression
    regex = r'((?:MON|TUE|WED|THU|FRI|SAT|SUN)\s*,?\s*\d{1,2}\s*(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s*(?:\d{4}(?!-\d{4}))?)|(\d{1,2}\s*(?:JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)\s*(?:\d{4}(?!-\d{4}))?)|((?:MON|TUE|WED|THU|FRI|SAT|SUN))|(\d{4}-\d{4})|(CLSD)|(-)' 

    # Find all matches
    matches = re.findall(regex, input_string)
    # Filter out empty strings from tuplespython
    filtered_matches = [group.strip() for match in matches for group in match if group]

    return filtered_matches
