from selenium import webdriver
from selenium.webdriver.common.by import By
from jobs import Jobs
from JobsGeDatabase import JobDatabse


def jobs_ge_pars(num):
    driver = webdriver.Chrome()
    driver.get("https://jobs.ge/?page=1&q=&cid=6&lid=&jid=")

    everything = driver.find_elements(By.XPATH, '//*[@id="job_list_table"]/tbody/tr')

    if num > len(everything) or num < 0:
        print("Error")
    else:
        for i in range(2, num + 2):

            job_butn = driver.find_element(By.XPATH, f'//*[@id="job_list_table"]/tbody/tr[{i}]/td[2]/a[1]')
            job_butn.click()

            name = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[1]/td/b').text

            company = driver.find_element(By.XPATH,
                                          '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[2]/td/b').text

            desc = driver.find_element(By.XPATH, '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[4]/td').text

            published = driver.find_element(By.XPATH,
                                            '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[3]/td/b[1]').text

            last_date = driver.find_element(By.XPATH,
                                            '//*[@id="job"]/table/tbody/tr/td[1]/table[2]/tbody/tr[3]/td/b[2]').text

            for_money_email = desc.split()
            salary = None
            for i in range(len(for_money_email)):
                if 'ლარ' in for_money_email[i] and for_money_email[i - 1].isnumeric() or '₾' in for_money_email[i]:
                    salary = for_money_email[i - 1] + ' ' + for_money_email[i]

            email = None
            for i in range(len(for_money_email)):
                if '@' in for_money_email[i] and '.' in for_money_email[i]:
                    email = for_money_email[i]

            database = JobDatabse("job_data")
            job = Jobs(name, desc, company, published, last_date, salary, email)
            database.add_job(job)

            driver.back()
