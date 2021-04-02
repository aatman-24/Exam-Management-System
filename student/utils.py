def pick(queryDict):
    query = dict(queryDict)
    options, filter = dict(), dict()
    order_by_options = ['fullName', 'rollNumber', 'admissionYear', 'id']
    options_choices = ['limit','order_by']
    filters_choices = ['std','div']

    for key in query:
        if(key in options_choices):
            if(key == "order_by" and query[key][0] in order_by_options):
                options[key] = query.get(key)[0]
            else:
                options[key] = int(query.get(key)[0])
        
        if(key in filters_choices):
            filter[key] = query[key][0]
    

    if('limit' not in options): 
        options['limit'] = 10

    return options,filter