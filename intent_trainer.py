import json

data = {
    "rasa_nlu_data": {
        "common_examples": [],
        "regex_features" : [],
        "entity_synonyms": []
        }
    }


def validate_intent(intent: str):
    list = ['greeting', 'select_company', 'revise_query', 'save_results', 'sentiment', 'data_viz']
    if intent not in list:
        raise TypeError("Not a possible intent")
    return True

def validate_entities(entities: list):
    if entities == None:
        return True
    pass

def validate_example(example):
    '''Checks for invalid & duplicate examples.'''
    
    if example == None:
        return TypeError('invalid example')

    # find if there are any common_examples with the same text. 
    # use a generator approach
    existing_texts = (existing_ex for existing_ex in data['rasa_nlu_data']['common_examples'])
    for existing_ex in existing_texts:
        if example['text'] == existing_ex['text']:
            #if both text & intent are the same, the example is invalid
            if example['intent'] == existing_ex['intent']:
                raise Exception('Duplicate example.')
            # if intent is not the same, the user must choose to keep or replace the old intent  
            if example['intent'] != existing_ex['intent']:
                raise Exception(f'DIFFERENT INTENTS: {example["intent"]} to be replaced by {existing_ex["intent"]}')
    return True

def example(text_: str, intent_: str, entities_: list = []):
    try:
        validate_intent(intent_)
        validate_entities(entities_)
    except TypeError as e:
        print(e)
        return None
    else:
        if entities_ == None:
            return dict(text = text_, intent = intent_)
        return dict(text = text_, intent = intent_, entities = entities_)

def add_example(example):
    try: 
        validate_example(example)
    except TypeError as te:
        print(te)
        return None
    except Exception as e:
        print(e)
        return None 
    else: 
        data['rasa_nlu_data']['common_examples'].append(example)
        return example

def create_entity(value_, entity_, text):
    start_ = text.find(value_)
    if start_ == -1:
        return None
    end_ = start_ + len(value_)
    ent = dict(start = start_, end = end_, value = value_, entity = entity_)
    return ent

# dump the current data.json into data, assuming a valid file.
with open('data\data.json', mode = 'r', encoding = 'utf-8') as f: 
    data = json.load(f)

# add more common examples via command line interface.
print("Welcome to the chatbot trainer. Add common examples and the intents they signify.")
quit = ('quit', 'end', 'done', 'stop')

while True:
    input_text = input('Input an example text:\n> ')
    if input_text in quit: 
        print("Your previous inputs will be saved.")
        break

    input_intent = input("Possible intents: 'greeting', 'select_company', 'revise_query', 'save_results', 'sentiment', 'data_viz'.\nInput the text\'s intent:\n> ")
    if input_intent in quit:
        print("Your previous inputs will be saved.")
        break

    input_entities_num = input('How many entities in the text? > ')
    if int(input_entities_num) != 0:
        input_entities = []
        for i in range(int(input_entities_num)):
            input_entity_value = input("What is the entity value? Type exactly how it appears in the text. > ")
            input_entity_type = input("What is the type? > ")
            ent = create_entity(input_entity_value, input_entity_type, input_text)
            if ent == None:
                print("Entity not valid. ")
            input_entities.append(ent)
            print(f"entity {ent} added")
        
        if None not in input_entities: 
            ex = add_example(example(input_text, input_intent, input_entities))
            print(f"Example added with text {input_text}, intent {input_intent}, and entities {input_entities}")            
        else:
            print("No example added due to invalid entity.")

    else:
        ex = add_example(example(input_text, input_intent))
        print(f"Example added with text {input_text} and intent {input_intent}")
    if ex == None:
        print("Example not added.")
    

f = open('data.json', mode = 'w', encoding = 'utf-8')
json.dump(data, f, indent=4)