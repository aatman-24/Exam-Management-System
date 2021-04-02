URL:
student ->
student/create/ -> GET POST
student/sid/ -> GET PATCH DELETE

fullName
slug
rollNumber
std
div
emailId
parentEmailId
admissionYear

Student.objects.create(
fullName = "Prince Dhaduk",
slug = "prince-dhaduk",
rollNumber = 8,
std = 12,
div = "A",
emailId = "hasuss22@gmail.com",
parentEmailId = "atmanpanseriyasss@gmail.com",
admissionYear = 2016
)

birthDate = '2001-08-11'
slug = 'prince-panseriya-profile'
gender = 'M'
phoneNumber = '9727954346'
previousSchool = 'RISEN'
student = prince

Profile.objects.create(
birthDate = '2000-07-24',
slug = 'aatman-panseriya-profile',
gender = 'M',
phoneNumber = '9925193729',
previousSchool = 'SSASIT',
student = atman
)

Profile.objects.create(
birthDate = '2000-07-24',
slug = 'aatman-panseriya-profile',
gender = 'M',
phoneNumber = '9925193729',
previousSchool = 'SSASIT',
student = atman
)

Profile.objects.create(
birthDate = '1999-08-24',
slug = 'dixit-savani-profile',
gender = 'M',
phoneNumber = '9925190000',
previousSchool = 'SVNIT',
student = dixit
)


ParentProfile.objects.create(
student = atman,
slug = 'aatman-parent' ,
fatherName = 'Jitendrabhai' ,
motherName = 'Nanynaben',
fatherBussiness = 'Diamond',
motherBussiness = 'Housekeeper',
fatherStudy = '10th pass',
motherStudy = '12th pass',
phoneNumber = '9429864807',
)

