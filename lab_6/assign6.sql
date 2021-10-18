1) select * from student CROSS JOIN marks_sem1 ON student.rollno=marks_sem1.rollno;

2) select student.name,marks_sem1.sports from student CROSS JOIN marks_sem1 ON student.rollno=marks_sem1.rollno;

3) select student.name,Marks_sem1.math,student.rollno from student CROSS JOIN marks_sem1 ON student.rollno=marks_sem1.rollno cross join campus on student.cid=campus.cid where law=1; 

4)select * from student left join campus on student.cid=campus.cid;

  select * from student right join campus on student.cid=campus.cid;