# Search and replace a pattern in a string

text = "Salamenta na pimenta, que ta tenga na selenta."
# Using 'replace' for simple substitution
new_text = text.replace("pimenta", "polenta")
print(new_text)

# For more complicated patterns, use 'sub' from the 're' module (regular expressions)
import re

text1 = "My date Birthday is in 20/02/2003"
# Modify: change DD/MM/YYYY to YYYY-MM-DD
result = re.sub(r"(\d+)/(\d+)/(\d+)", r"\3-\1-\2", text1)
print(result)

# Compiling a pattern for reuse
pat = re.compile(r"(\d+)/(\d+)/(\d+)")
result2 = re.sub(pat, r"\2*\3*\1", text1)
print(result2)
# The first argument to 'sub' is the pattern (can be a string or a compiled pattern)

# Substituting text ignoring case (case-insensitive)
text2 = "JaVa, Java, JAva"

# Case-sensitive replacement:
case_sensitive = re.sub("java", "python", text2)
print(case_sensitive)

# Case-insensitive replacement:
case_insensitive = re.sub("java", "python", text2, flags=re.IGNORECASE)
print(case_insensitive)

# Removing unwanted characters from a string:
# Whitespace:
text3 = "      python      "
print(f"'{text3}' before strip")
print(f"'{text3.strip()}' after strip")

# Removing specific characters using strip():
text4 = "-----python-----"
print(f"'{text4.strip('-')}' after strip('-')")

# More on strip, lstrip, rstrip:
text5 = "$$$$$DecaDuratestonTrembolin-----"
print(f"'{text5.strip('-$')}' after strip('-$')")      # Remove both '-' and '$'
print(f"'{text5.lstrip('-$')}' after lstrip('-$')")    # Remove from left
print(f"'{text5.rstrip('-$')}' after rstrip('-$')")    # Remove from right
