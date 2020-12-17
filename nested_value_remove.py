students = [
    {
        "name" : "Poonam",
        "class" : "12th",
        "subject" : {
            "sub1" : [
                {
                    "Bio1" : "Zoologi",
                    "Bio2" : "Botany"
                },
                "Crazypooh"
            ],
            "sub2" : "Physics",
            "sub3" : "Chemistry",
            "sub4" : "Maths"
        }
    },
     {
        "name" : "Jyoti",
        "class" : "12th",
        "subject" : {
            "sub2" : "Physics",
            "sub3" : "Chemistry",
            "sub4" : "Maths"
        }
    }
]
del(students[0]['subject']['sub1'][0]['Bio2'])
print(students)