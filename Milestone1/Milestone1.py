#a python program to find the locations of mainfields and subfields

import csv

def generate_fields(careareas, mainfield_len, subfield_len):
    mainfields = []
    subfields = []
    mf_id = 0
    for carearea in careareas:
        
        id, x1, x2, y1, y2 = carearea
        id = int(id)
        
        #print(f"Care Area: id={id}, x1={x1}, x2={x2}, y1={y1}, y2={y2}")
        
        #generating the mainfields for the carearea
        mainfield_x1 = x1
        mainfield_y1 = y1

        mainfield_x2 = mainfield_x1 + mainfield_len
        mainfield_y2 = mainfield_y1 + mainfield_len
        mainfields.append([mf_id, mainfield_x1, mainfield_x2, mainfield_y1, mainfield_y2])
        mf_id += 1
        
    #generating the subfields for each mainfield
    sf_id = 0
    for carea in careareas:
        ca_id, ca_x1, ca_x2, ca_y1, ca_y2 = carea
        
        #print(f"Mainfield: id={mf_id}, x1={mf_x1}, x2={mf_x2}, y1={mf_y1}, y2={mf_y2}")
        
        subfield_x1 = ca_x1
        while (subfield_x1) <= ca_x2:
            #print(f"Processing subfield_x1={subfield_x1}")
            subfield_y1 = ca_y1
            while (subfield_y1) <= ca_y2:
                #print(f"Processing subfield_y1={subfield_y1}")
                subfield_x2 = subfield_x1 + subfield_len
                subfield_y2 = subfield_y1 + subfield_len
                subfields.append([sf_id, subfield_x1, subfield_x2, subfield_y1, subfield_y2, ca_id])
                subfield_y1 += subfield_len
                sf_id += 1
            subfield_x1 += subfield_len
        
    return mainfields, subfields


#reading the data from CareAreas CSV file
careareas = []
with open('C:\\Users\\Admin\\Desktop\\KLA\\Validator\\Validator\\Students\\71762231014\\Milestone1\\CareAreas.csv', mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] != 'id':  # Skip header if present
            careareas.append([float(value) if i > 0 else int(value) for i, value in enumerate(row)])



#reading the data from MetaData CSV file
with open('C:\\Users\\Admin\\Desktop\\KLA\\Validator\\Validator\\Students\\71762231014\\Milestone1\\metadata.csv', mode='r') as file:
    reader = csv.reader(file)
    metadata = list(reader)    

    if len(metadata) < 2 or len(metadata[1]) < 2:
        raise ValueError("Metadata file does not have the expected format.")
    mainfield_len = float(metadata[1][0])  # Main Field Length
    subfield_len = float(metadata[1][1])   # Sub Field Length

#generating the fields for mainfields and subfields by calling the function
mainfields, subfields = generate_fields(careareas, mainfield_len, subfield_len)

#writing the output values to the mainfieldop.csv
with open('C:\\Users\\Admin\\Desktop\\KLA\\Validator\\Validator\\Students\\71762231014\\Milestone1\\mainfields.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    #writer.writerow(['id', 'x1', 'x2', 'y1', 'y2'])
    writer.writerows(mainfields)

#writing the output values to the subfieldop.csv
with open('C:\\Users\\Admin\\Desktop\\KLA\\Validator\\Validator\\Students\\71762231014\\Milestone1\\subfields.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    #writer.writerow(['id', 'x1', 'x2', 'y1', 'y2', 'MFid'])
    writer.writerows(subfields)

print("The values of the locations of the mainfields as well as the subfields have been found!!")