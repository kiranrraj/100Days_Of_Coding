persons = {'John': {'Age': '55', 'Gender': 'Male'}, 
'Toney': {'Age': '23', 'Gender': 'Male'}, 
'Karin': {'Age': '42', 'Gender': 'Female'}, 
'Cathie': {'Age': '29', 'Gender': 'Female'}, 
'Rosalba': {'Age': '12', 'Gender': 'Female'}, 
'Nina': {'Age': '50', 'Gender': 'Female'}, 
'Burton': {'Age': '16', 'Gender': 'Male'}, 
'Joey': {'Age': '90', 'Gender': 'Male'}}

def write_person_data(data_dict,filename):
    with open(filename, 'w') as f_out:
        for k, v in data_dict.items():
            print('{}, {}, {}'.format(k, v['Age'], v['Gender']), file=f_out)

write_person_data(persons, 'data.txt')