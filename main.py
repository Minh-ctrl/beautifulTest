# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
html = open('Tuan.html', 'r')
soup = BeautifulSoup(html, 'html.parser')
Sections = soup.find_all(
    'section', class_='artdeco-card ember-view relative break-words pb3 mt2')
relInfo = {}
experiences = {}
Languages = {}
Educations = {}
Skills = []

for x in Sections:
    if "About" in x.find('div', class_='pvs-header__top-container--no-stack').get_text():
        aboutOuter = x.find(
            'div', class_='inline-show-more-text')
        about = aboutOuter.find('span', class_="visually-hidden")
        relInfo.update({
            'About': about.get_text()
        })
    if "Experience" in x.find('div', class_='pvs-header__top-container--no-stack').get_text():
        # Titles = x.find_all(
        #     'div', class_='display-flex align-items-center')
        # Companies = x.find_all('span', class_='t-14 t-normal')
        # if len(Companies) == len(Titles):
        #     for f, b in zip(Companies, Titles):
        #         # clean repeatable
        #         company = f.find('span', class_='visually-hidden')
        #         title = b.find('span', class_='visually-hidden')
        #         experience = company.get_text() + ' ' + title.get_text()
        #         experiences.update({company.get_text(): title.get_text()})

        jobs = []
        blocks = x.find_all(
            'div', class_='pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested')
        for block in blocks:
            Titles = block.find_all(
                'div', class_='display-flex align-items-center')
            Companies = block.find_all('span', class_='t-14 t-normal')
            # Company = Companies.get_text()
            for company in Companies:
                name = company.find('span', class_='visually-hidden')
            if len(Titles) > 1:
                for title in Titles:
                    job = title.find('span', class_='visually-hidden')
                    jobs.append(job.get_text())
#       very lazy workaround
                popped = jobs.pop(0)
                experiences.update({popped: jobs})
            else:
                for title in Titles:
                    job = title.find(
                        'span', class_='visually-hidden').get_text()
                    experiences.update({name.get_text(): job})
        relInfo.update({
            'Experiences': experiences
        })

    if "Volunteering" in x.find('div', class_='pvs-header__top-container--no-stack').get_text():
        relInfo.update({
            'Volunteer': x.get_text(strip=True)
        })
    if "Skills" in x.find('div', class_='pvs-header__top-container--no-stack').get_text():
        skills = x.find_all(
            'div', class_="display-flex align-items-center")
        for skill in skills:
            talent = skill.find('span', class_='visually-hidden')
            Skills.append(talent.get_text())
        relInfo.update({
            'Skills': Skills
        })
    if "Languages" in x.find('div', class_='pvs-header__top-container--no-stack').get_text():
        languages = x.find_all('div', class_='display-flex align-items-center')
        levels = x.find_all('span', class_='t-14 t-normal t-black--light')
        for f, b in zip(languages, levels):
            level = b.find('span', class_='visually-hidden')
            language = f.find('span', class_='visually-hidden')
            Languages.update({language.get_text(): level.get_text()})
        relInfo.update({
            'Languages': Languages
        })
    if "Education" in x.find('div', class_='pvs-header__top-container--no-stack').get_text():
        Schools = x.find_all('div', class_='display-flex align-items-center')
        # Periods = x.find_all('span', class_='t-14 t-normal t-black--light')
        Types = x.find_all('span', class_='t-14 t-normal')
        for f, b in zip(Schools, Types):
            schools = f.find('span', class_='mr1 hoverable-link-text t-bold')
            school = schools.find('span', class_='visually-hidden')
            Type = b.find('span', class_='visually-hidden')
            Educations.update({school.get_text(): Type.get_text()})
        relInfo.update({
            'Educations': Educations
        })
        #         # clean repeatable
        #         company = f.find('span', class_='visually-hidden')
        #         title = b.find('span', class_='visually-hidden')
        #         experience = company.get_text() + ' ' + title.get_text()
        #         experiences.update({company.get_text(): title.get_text()})
res = json.dumps(relInfo, ensure_ascii=False)
file = open("test.json", "w")
file.write(res)
