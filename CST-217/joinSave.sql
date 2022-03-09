-- professor and their number of students --
-- select P.fname As "Professor FirstName", P.lname As "Professor LastName" , 
-- count(SC.Students_ID) As "Number Of Students"
-- from 
-- professor P left join class C on P.ID = C.professor_ID
-- left join students_classes SC on C.Courses_ID = SC.Classes_Courses_ID
-- left join students S on SC.Students_ID = S.ID
-- group by P.ID

-- Given student ID, get class times and location
-- select C.Courses_ID as 'Course ID', C.Class_Time AS 'Class Time', 
-- C.Class_Start_Date as 'Class Start Date', C.Class_End_Date as 'Class End Date', 
-- C.Class_Meeting_Days AS 'Class Meeting Day(s)', 
-- C.rooms_Buildings_Building_Number as 'Building Number', 
-- C.rooms_Room_Number as 'Room Number',
-- B.Name as 'Building Name'
-- from students S left join students_classes SC on S.ID = SC.Students_ID
-- left join Class C on   SC.Classes_Courses_ID = C.Courses_ID
-- left join Buildings B on C.rooms_Buildings_Building_Number = B.Building_Number 
-- where S.ID = 15940 -- this is where the user would pass in their ID

-- Given professor ID, get class times and location
-- select C.Courses_ID as 'Course ID', C.Class_Time AS 'Class Time', 
-- C.Class_Start_Date as 'Class Start Date', C.Class_End_Date as 'Class End Date', 
-- C.Class_Meeting_Days AS 'Class Meeting Day(s)', 
-- C.rooms_Buildings_Building_Number as 'Building Number', 
-- C.rooms_Room_Number as 'Room Number',
-- B.Name as 'Building Name'
-- from professor P left join Class C on C.Professor_ID = P.ID
-- left join Buildings B on C.rooms_Buildings_Building_Number = B.Building_Number
-- where P.ID = 98670 -- this is where the user would pass in their ID

-- list Students and activities they participate in as well as budget
-- SELECT S.lname, S.fname, A.Name, A.Budget
-- FROM students_has_activities HA 
-- LEFT JOIN students S ON HA.Students_ID = S.ID
-- LEFT JOIN activities A ON HA.Activities_ID = A.ID;

-- contact info for a professors students based on class id --
-- SELECT S.fName, S.lName, S.Email, S.Phone
-- FROM students_classes SC LEFT JOIN students S ON SC.Students_ID = S.ID
-- LEFT JOIN class C ON SC.Classes_Courses_ID = C.Courses_ID
-- WHERE C.ID = 1251; -- Enter class ID Here

-- contact info for students who attended and activity by name --
-- SELECT S.Email, S.fName, S.lName
-- FROM students_has_activities HA LEFT JOIN students S ON HA.Students_ID = S.ID
-- LEFT JOIN activities A ON HA.Activities_ID = A.ID
-- WHERE A.Name = 'Soccer'; -- Enter activity name

-- search occupancy of building by name --
-- SELECT B.Name, B.Building_Number, sum(R.occupancy) AS 'Total Occupants'
-- FROM buildings B LEFT JOIN rooms R ON B.Building_Number = R.Buildings_Building_Number
-- WHERE B.Name = 'Prescott'; -- enter building number

-- List of professors and the classes that they teach as well as when they occur
-- select P.lname, P.fname, CR.Name, CR.Description, Class_Meeting_Days, Class_Time
-- from Courses CR 
-- left join Class C on C.courses_ID = CR.ID 
-- left join Professor P on C.professor_ID = P.ID

-- List of students and the buildings they live in 
-- select S.fname, S.lname, B.Name, S.rooms_Room_Number, R.Occupancy
-- from team_4.students S 
-- left join team_4.buildings B on S.rooms_Buildings_Building_Number = B.Building_Number
-- left join team_4.rooms R on S.rooms_Buildings_Building_Number = R.Buildings_Building_Number and S.rooms_Room_Number = R.Room_Number