-- active professor to student ratio -- 
-- select count(distinct S.ID) as 'Number Of Active Students', 
-- count(distinct P.ID) as 'Number Of Active Professors'
-- from team_4.students as S, 
-- team_4.professor as P, 
-- team_4.class as C,
-- team_4.students_classes as SC
-- where P.ID = C.Professor_ID and S.ID = SC.Students_ID 

-- professor and their number of students --
-- select P.fName As "Professor FirstName",
-- P.lName As "Professor LastName",
-- count(SC.Students_ID) As "Number Of Students"
-- from team_4.professor As P, 
-- team_4.students as S, 
-- team_4.students_classes as SC,
-- team_4.class as C
-- where P.ID = C.Professor_ID 
-- and S.ID = SC.Students_ID 
-- and C.Courses_ID = SC.Classes_Courses_ID
-- group by P.ID

-- Given student ID, get class times and location
-- select C.Courses_ID as 'Course ID', C.Class_Time AS 'Class Time', 
-- C.Class_Start_Date as 'Class Start Date', C.Class_End_Date as 'Class End Date', 
-- C.Class_Meeting_Days AS 'Class Meeting Day(s)', 
-- C.rooms_Buildings_Building_Number as 'Building Number', 
-- C.rooms_Room_Number as 'Room Number',
-- B.Name as 'Building Name'
-- from team_4.students as S, 
-- team_4.students_classes as SC,
-- team_4.class as C,
-- team_4.buildings as B
-- where S.ID = SC.Students_ID
-- and C.Courses_ID = SC.Classes_Courses_ID
-- and B.Building_Number = C.rooms_Buildings_Building_Number
-- and S.ID = 15940 -- this is where the user would pass in their ID


-- Given professor ID, get class times and location
-- select C.Courses_ID as 'Course ID', C.Class_Time AS 'Class Time', 
-- C.Class_Start_Date as 'Class Start Date', C.Class_End_Date as 'Class End Date', 
-- C.Class_Meeting_Days AS 'Class Meeting Day(s)', 
-- C.rooms_Buildings_Building_Number as 'Building Number', 
-- C.rooms_Room_Number as 'Room Number',
-- B.Name as 'Building Name'
-- from team_4.professor as P, 
-- team_4.class as C,
-- team_4.buildings as B
-- where P.ID = C.Professor_ID
-- and B.Building_Number = C.rooms_Buildings_Building_Number
-- and P.ID = 98670 -- this is where the user would pass in their ID

-- students in a given course ID
-- select S.fName, S.lName
-- from team_4.students as S, 
-- team_4.students_classes as SC,
-- team_4.class as C
-- where S.ID = SC.Students_ID
-- and C.Courses_ID = SC.Classes_Courses_ID
-- and SC.Classes_Courses_ID = 'MAT-345' -- input for course ID

-- 6 --
-- list of all current classes and start times and locations
-- select C.Courses_ID as 'Course ID', 
-- C.Class_Time as 'Class Time', 
-- B.Name as 'Building Name', 
-- B.Building_Number as 'Building Number',
-- R.Room_Number as 'Room Number'
-- from  team_4.class as C, 
-- team_4.rooms as R,
-- team_4.buildings As B
-- where B.Building_Number = R.Buildings_Building_Number 
-- and C.rooms_Room_Number = R.Room_Number
-- and C.rooms_Buildings_Building_Number = R.Buildings_Building_Number
-- 6 --

-- list Students and activities they participate in as well as budget
-- select S.lName, S.fName, A.Name, A.Budget
-- from team_4.students As S, team_4.students_has_activities AS HA, team_4.activities as A
-- where HA.Students_ID = S.ID And HA.Activities_ID = A.ID;  

-- List of professors and the classes that they teach as well as when they occur
-- select professor.lname, professor.fname, courses.Name, courses.Description, Class_Meeting_Days, Class_Time
-- from team_4.courses, team_4.class, team_4.professor
-- where courses.ID = class.Courses_ID AND professor.ID = class.professor_ID;

-- shows which students are living in which rooms/buildings
-- select b.Name, room_number, s.fname, s.lname
-- from team_4.buildings as b, team_4.rooms as r, team_4.students as s
-- where r.room_number = s.rooms_Room_Number and r.Buildings_Building_Number = s.rooms_Buildings_Building_Number 
-- and b.building_number = r.buildings_building_number
-- order by b.name

-- search occupancy of building by name
-- select B.Name, B.Building_Number, sum(occupancy) As 'Total Occupancy'
-- from team_4.buildings as B, team_4.rooms as R
-- where B.Building_Number = R.Buildings_Building_Number
-- and B.Name = 'Prescott' -- enter building name here
-- group by B.Building_Number

-- contact info for students who attended activity by name
-- select S.Email, S.fName, S.lName
-- from team_4.students as S, team_4.activities as A, team_4.students_has_activities as HA
-- where S.ID = HA.Students_ID and HA.Activities_ID = A.ID
-- and A.Name = 'Soccer' -- enter activity name

-- contact info for a professors students based on class ID
-- select S.fName, S.lName, S.Email, S.Phone
-- from team_4.students as S, 
-- team_4.students_classes as SC,
-- team_4.class as C
-- where S.ID = SC.Students_ID
-- and C.Courses_ID = SC.Classes_Courses_ID
-- and C.ID = 1251 -- input for class ID











