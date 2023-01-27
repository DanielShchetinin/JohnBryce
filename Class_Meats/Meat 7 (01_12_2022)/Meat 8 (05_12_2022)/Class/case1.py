from typing import Any 
code = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

db = {}

for key, info in code:
    if key not in db:
        db[key] = []
    db[key].append(info)    
    
print(db)