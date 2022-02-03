-- a --
-- SELECT FName, LName
-- FROM employee, department, project,  works_on
-- Where SSN = ESSN and PNO = PNUMBER and DNO = DNUMBER and DNO = '4' and PNAME = 'Newbenefits' and HOURS > 12

-- b --
-- Select Fname, Lname
-- From employee, dependent
-- where SSN = ESSN and employee.sex = dependent.sex

-- c --
-- select E.Fname, E.Lname
-- From employee E, employee S
-- where E.SUPERSSN = S.SSN and S.FNAME = 'Jennifer' and S.LName = 'Wallace'

-- d --
-- Select PNAME, sum(Hours)
-- From project, works_on
-- where PNUMBER = PNO
-- group by PNAME

-- e --
-- select distinct Fname, lname
-- from employee, works_on
-- where ssn = essn

-- f --
-- Select Dname, Avg(SALARY)
-- from department, employee
-- where DNO = DNUMBER
-- group by DName

-- g --
-- select sex, avg(SALARY)
-- from employee
-- where sex = 'F'



