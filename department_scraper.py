from bs4 import BeautifulSoup
import requests

html_text = requests.get('http://catalog.rpi.edu/content.php?catoid=24&navoid=601').text
soup = BeautifulSoup(html_text,'lxml')

text = soup.find("td", class_ = 'block_content')

school_data = {}
department_data = {}
schools = text.find_all('h3')
for school in schools: 
    departments = school.find_next('div').find_all('h4')
    school_data[school.text] = {
        "school_link": "catalog.rpi.edu/" + school.find_next('a')['href'],
        "departments": [dep.text for dep in departments],
    }
    for dep in departments:
        department_data[dep.text] = {
            "department_link": "catalog.rpi.edu/" + dep.find_next('a')['href'],
        }


for school_ in school_data:
    print(school_ + ":")
    print(school_data[school_]["school_link"])
    for department in school_data[school_]["departments"]:
        print("\t" + department)
        print("\t" + department_data[department]["department_link"]+"\n")
    
