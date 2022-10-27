# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
html = open('Minh.html', 'r')
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
        jobs = []
        periods = []
        about = None
        blocks = x.find_all(
            'div', class_='pvs-entity pvs-entity--padded pvs-list__item--no-padding-when-nested')
        for block in blocks:
            Titles = block.find_all(
                'div', class_='display-flex align-items-center')
            Times = block.find_all(
                'span', class_='t-14 t-normal t-black--light'
            )
            Descriptions = block.find_all(
                'div', class_='inline-show-more-text')
            Companies = block.find_all('span', class_='t-14 t-normal')
            for Description in Descriptions:
                about = Description.get_text()
            for company in Companies:
                name = company.find('span', class_='visually-hidden')
            if len(Titles) > 1:
                for Time in Times:
                    period = Time.find(
                        'span', class_='visually-hidden').get_text()
                    periods.append(period + ' ')
                workPeriod = ''.join(periods)
                for title in Titles:
                    job = title.find('span', class_='visually-hidden')
                    jobs.append(job.get_text())
#       very lazy workaround
                popped = jobs.pop(0)
                experiences.update(
                    {popped: [{'roles': jobs, 'Periods': workPeriod, 'Description': about}]})
            else:
                for title in Titles:
                    for Time in Times:
                        period = Time.find(
                            'span', class_='visually-hidden').get_text()
                        periods.append(period + ' ')
                    workPeriod = ''.join(periods)
                    job = title.find(
                        'span', class_='visually-hidden').get_text()
                    experiences.update(
                        {name.get_text(): [{'role': job, 'Period': workPeriod, 'Description': about}]})
                    periods = []

                    # workPeriod = ''
        relInfo.update({
            'Experiences': experiences
        })

    # if "Volunteering" in x.find('div', class_='pvs-header__top-container--no-stack').get_text():
    #     relInfo.update({
    #         'Volunteer': x.get_text(strip=True)
    #     })
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
        # zip data structure might not be appropriate here
        for f, b in zip(Schools, Types):
            schools = f.find('span', class_='mr1 hoverable-link-text t-bold')
            school = schools.find('span', class_='visually-hidden')
            Type = b.find('span', class_='visually-hidden')
            Educations.update({school.get_text(): Type.get_text()})
        relInfo.update({
            'Educations': Educations
        })

res = json.dumps(relInfo, ensure_ascii=False)
file = open("test.json", "w")
file.write(res)
