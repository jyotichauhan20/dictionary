#replace Jyoti's sub1 with computer science 

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
students[1]["subject"]["sub1"]="bio"
print(students)
print(students[0]["subject"]["sub1"][0]["Bio2"])
print(students[0]["subject"]["sub1"][1])
