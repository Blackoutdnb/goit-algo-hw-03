я попробую выслать тебе весь код целиком
def read_text_file(path):
try:
withopen(path, encoding="utf-8") as f:
path = f.read()
except (UnicodeDecodeError, FileNotFoundError): 
path = ""
return path