

ACTIONS = (
    "INSERT",
    "SEARCH"
)

user_words = list()

def main():
    
    while True:
        user_action = getActionFromUser()
        user_action_result = action_execute(user_action)
    
        if not user_action_result:
            continue
        
    return 1
    
def getActionFromUser() -> int:
    action = None
    action_list_str = "\n".join(f"{idx + 1}. {act}" for idx, act in enumerate(ACTIONS))

    while True:
        print('\n')
        print("| ---------- Avaliable actions ---------- |:\n")
        print(action_list_str)
        
        action = input("> Enter action number: ")
        
        if not action.isnumeric():
            print("\n[ERROR] Invalid input: you can only enter a number.")
            continue
        
        action = int(action)
        if action > len(ACTIONS):
            print("\n[ERROR] Invalud input: action does not exists.")
            continue
        
        else:
            break
    
    return (action - 1)

def action_execute(action: int) -> bool:
    if action < 0:
        print("\n[ERROR] Action number can not be lower than 1.")
        return False

    if action == 0:
        action_execute_insert()

    if action == 1:
        if not len(user_words):
            print("\n[ERROR] Words list is empty.")
            return False
            
        action_execute_search()
        
    return True
        
def action_execute_insert():
    print("\n")
    print("| ----- Action: Insert ----- |:")
    
    word = None
    
    while True:
        word = input("\n[STOP COMMAND] Insert Stop to stop adding words.\n> Enter a word you want to add to the list: ")
        
        if word == "stop" or word == "Stop":
            break
        
        if len(word) == 0:
            continue
        
        if word.count(' ') > 0:
            print("\n[ERROR] You can insert only 1 word (without spaces).")
            continue
        user_words.append(word)
        print(f"Word '{word}' was added to words list.")
    
def action_execute_search():
    letter = None
    count = None
    
    while True:
        letter = input("> Enter a letter for search: ")

        if not len(letter):
            continue
        
        if len(letter) > 1:
            print("\n[ERROR]: Invalid input: You cant enter only 1 letter.")
            continue

        break
    
    while True:
        count = (input("> Enter count for letter: "))
        if not count.isnumeric():
            print("\n[ERROR] Invalid input: you can only enter a number.")
            continue
        count = int(count)
        
        break

    
    result = []
    for word in user_words:
        if word.count(letter) == count:
            result.append(word)

    if len(result) == 0:
        print("No words were founded.")
    else:
        print(f"\n| Words with {count} letter(s) '{letter}': ")
        print('\n'.join(result))
        
if __name__ == '__main__':
    main()