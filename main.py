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

def delete_contact(contacts, query):
    contacts.pop(query.number, None)

def find_contact(contacts, query):
    response = contacts.get(query.number, 'not found')
    return response

def process_queries(queries):
    result = []
    contacts = {}
    for cur_query in queries:
        if cur_query.type == 'add':
            add_contact(contacts, cur_query)
        elif cur_query.type == 'del':
            delete_contact(contacts, cur_query)
        else:
            response = find_contact(contacts, cur_query)
            result.append(response)
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))

