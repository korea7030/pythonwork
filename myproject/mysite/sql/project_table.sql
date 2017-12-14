create table BOOK_CATEGORY
(
    cate_id varchar(10) primary key ,
    cate_1 varchar(50),
    cate_2 varchar(50)
)

CREATE TABLE BOOK_INFO(
	book_sequence  varchar(10) primary key,
    book_title varchar(200),
    book_subtitle  varchar(300),
    author	varchar(100),
    translator varchar(100),
    publisher  varchar(100),
    publisher_date 	date,
    book_format   varchar(20),
    pages	integer,
    rating	integer,
    cate_id varchar(10),
    start_date date,
    end_date  date,
    reg_date  date,
    book_essay_url 	varchar(1000),
    poster_url   varchar(1000),
    read_status  varchar(10),
    borrowed_yn  char(2),
    -- docfile bytea
    book_essay varchar(4000)
);

create table READ_HIST(
    book_sequence  varchar(10) REFERENCES BOOK_INFO(book_sequence),
    start_read_time time,
    end_read_time time,
    read_place varchar(30),
    not_read_reason varchar(100),
    start_page_num integer,
    end_page_num integer,
    read_date date
);
