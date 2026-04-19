# ================================
# PYTHON STRING METHODS COMPLETE
# ================================

text = "  hello world python 123  "

# 1. CASE METHODS
print("Lower:", text.lower())
print("Upper:", text.upper())
print("Title:", text.title())
print("Capitalize:", text.capitalize())
print("Swapcase:", text.swapcase())

# 2. ALIGNMENT
print("Center:", text.center(50, '*'))
print("Left Justify:", text.ljust(50, '-'))
print("Right Justify:", text.rjust(50, '-'))
print("Zero Fill:", "42".zfill(5))

# 3. FIND METHODS
print("Find 'world':", text.find("world"))
print("RFind 'o':", text.rfind("o"))

try:
    print("Index 'python':", text.index("python"))
except ValueError:
    print("Substring not found")

# 4. COUNT
print("Count 'o':", text.count('o'))

# 5. REPLACE & STRIP
print("Replace:", text.replace("world", "universe"))
print("Strip:", text.strip())
print("LStrip:", text.lstrip())
print("RStrip:", text.rstrip())

# 6. SPLIT & JOIN
words = text.split()
print("Split:", words)

lines = "one\ntwo\nthree"
print("Splitlines:", lines.splitlines())

joined = "-".join(words)
print("Join:", joined)

# 7. CHECK METHODS
print("Is Alpha:", "abc".isalpha())
print("Is Digit:", "123".isdigit())
print("Is Alnum:", "abc123".isalnum())
print("Is Space:", "   ".isspace())
print("Is Lower:", "abc".islower())
print("Is Upper:", "ABC".isupper())
print("Is Title:", "Hello World".istitle())

# 8. STARTS / ENDS
print("Startswith:", text.startswith("  hello"))
print("Endswith:", text.endswith("123  "))

# 9. PARTITION
sample = "apple-banana-orange"
print("Partition:", sample.partition("-"))
print("RPartition:", sample.rpartition("-"))

# 10. ENCODE
print("Encode:", text.encode())

# 11. EXPAND TABS
tab_text = "Hello\tWorld"
print("Expand Tabs:", tab_text.expandtabs(10))