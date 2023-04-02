# python3

class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def add_contact(contacts, query):
    contacts[query.number] = query.name

def remove_contact(contacts, query):
    contacts.pop(query.number, None)

def find_contact(contacts, query):
    if query.number in contacts:
        return contacts[query.number]
    else:
        return 'not found'

def process_queries(queries):
    result = []
    # Keep dictionary of all existing contacts with phone number as key.
    contacts = {}
    for query in queries:
        if query.type == 'add':
            add_contact(contacts, query)
        elif query.type == 'del':
            remove_contact(contacts, query)
        else:
            response = find_contact(contacts, query)
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

