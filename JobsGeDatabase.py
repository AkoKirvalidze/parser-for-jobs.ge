import sqlite3


class JobDatabse:
    def __init__(self, db_name):
        self.connect = sqlite3.connect(db_name)
        self.cursor = self.connect.cursor()
        self.cursor.execute("""
            create table if not exists Jobs(
                id integer primary key, 
                name text,
                desc text,
                company text,
                p_date text,
                d_date text,
                salary text,
                email text
            )
        """)

    def add_job(self, job):
        self.cursor.execute("""
            insert into jobs(name, desc, company, p_date, d_date, salary, email)
            values (?,?,?,?,?,?,?)
        """, (job.name, job.desc, job.company, job.p_date, job.d_date, job.salary, job.email))
        self.connect.commit()

    def jobs_salaries(self):
        self.cursor.execute("""
            select name, salary from jobs;
        """)
        return self.cursor.fetchall()
