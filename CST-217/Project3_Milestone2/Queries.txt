-- 1. Show all the books in your bookstore sorted by cost of the book.
Select * from book_info order by cost ASC;

-- 2. Show how many books of each genre in your bookstore.
Select genre, count(book_id) from book_info group by genre;

-- 3. Show all the poetry books in your store that cost more than average cost of books.
Select *, (select avg(cost) from book_info) from book_info
where genre = 'poetry' and cost > (select avg(cost) from book_info);

-- 4. Show all the authors in your bookstore and the number of books they have.
select AI.*, count(AI.author_id) as 'Number_of_books_published' from author_info AI
left join book_info_has_author_info BIHAI on AI.author_id = BIHAI.author_info_author_id
group by AI.author_id;

-- 5. Show all the unique publishers in your bookstore with the number of authors they work with.
select BI.publisher_name, count(Distinct BIHAI.author_info_author_id) as 'Authors Worked With'
from book_info BI
left join book_info_has_author_info BIHAI on BI.book_id = BIHAI.book_info_book_id
group by BI.publisher_name;

-- 6. What is the total value of all the books put together in your bookstore based on authors sorted in descending order.
select AI.fname, AI.lname, sum(cost) as Book_Cost_Total
from author_info AI
left join book_info_has_author_info BIHAI on AI.author_id = BIHAI.author_info_author_id
left join book_info BI on BIHAI.book_info_book_id = BI.book_id
group by author_id
order by Book_Cost_Total Desc;

-- ex 1. Which author has the maximum number of books in your store and what is the total value of all the books from that author alone.
select *
from(
select AI.author_id ,AI.fname, AI.lname, sum(cost) as Book_Cost_Total, count(BIHAI.book_info_book_id) as Number_of_Books
from author_info AI
left join book_info_has_author_info BIHAI on AI.author_id = BIHAI.author_info_author_id
left join book_info BI on BIHAI.book_info_book_id = BI.book_id
group by author_id
)
As SubQuery
where Number_of_Books = (select max(Number_of_Books) 
						 from (select AI.author_id ,AI.fname, AI.lname, sum(cost) as Book_Cost_Total, 
									  count(BIHAI.book_info_book_id) as Number_of_Books
							   from author_info AI
							   left join book_info_has_author_info BIHAI on AI.author_id = BIHAI.author_info_author_id
							   left join book_info BI on BIHAI.book_info_book_id = BI.book_id
							   group by author_id
							   )
							   As SubQuery2
							   );

-- ex 2. In which year was the maximum number of books published (from the books stored in your database).
select *
from(
select BI.published_year, count(BI.book_id) as Books_Per_Year
from book_info BI
group by BI.published_year
)
As SubQuery
where Books_Per_Year = (select max(Books_Per_Year)
						from(select BI.published_year, count(BI.book_id) as Books_Per_Year
							 from book_info BI
							 group by BI.published_year
							 )
							 As SubQuery2
                        );