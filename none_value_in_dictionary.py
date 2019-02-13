def dup(data):
    for key, value in list(data.items()):
        if isinstance(value, dict):
            value=dup(value)
        else:
            if value==None:
                data.pop(key)
    return data


a={
    3:{
        'name':None, 'dept_id': 343,'address':{'City':None,'pincode':541283}
       }
    
    }
d=dup(a)
print(d)


