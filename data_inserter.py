import pandas as pd
from schools.models import  *

df = pd.read_excel('data.xlsx','Berkeley')
df[['Class Number ','Class Size']] = df[['Class Number ','Class Size']].fillna(0).astype('double')
for _,i in df.fillna('').iterrows():
    i = i.to_dict()
    try:
        school = School(school=i['School '])
        school.save()
    except:

        school = School.objects.get(school=i['School '])

    try:
        subject = Subject(school=school,subject=i['Subject'])
        subject.save()
    except Exception as e:
        subject = Subject.objects.get(school=school,subject=i['Subject'])

    try:
        classdata = ClassData(subject=subject,class_number=i['Class Number '],class_size=i['Class Size'])
        classdata.save()
    except:
        classdata = ClassData.objects.get(subject=subject,class_number=i['Class Number '],class_size=i['Class Size'])

    try:
        fname = i['Professor First Name']
        lname = i['Professor Last Name']
        email = i['Email']
        professordata = ProfessorData(classData=classdata,first_name=fname,last_name=lname,email=email)
        professordata.save()
    except Exception as e:
        print(e)