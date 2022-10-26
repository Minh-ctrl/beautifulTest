# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import json
html = open('Munekane.html', 'r')
soup = BeautifulSoup(html, 'html.parser')
Sections = soup.find_all(
    'section', class_='artdeco-card ember-view relative break-words pb3 mt2')
relInfo = {}
experiences = {}
Languages = {}
Skills = []
for x in Sections:
    if "AboutAbout" in x.get_text():
        aboutOuter = x.find(
            'div', class_='inline-show-more-text inline-show-more-text--is-collapsed')
        about = aboutOuter.find('span', class_="visually-hidden")
        print(about.get_text())
        relInfo.update({
            'About': about.get_text()
        })
    if "ExperienceExperience" in x.get_text():
        Titles = x.find_all(
            'div', class_='display-flex align-items-center')
        Companies = x.find_all('span', class_='t-14 t-normal')
        if len(Companies) == len(Titles):
            for f, b in zip(Companies, Titles):
                # clean repeatable
                company = f.find('span', class_='visually-hidden')
                title = b.find('span', class_='visually-hidden')
                experience = company.get_text() + ' ' + title.get_text()
                experiences.update({company.get_text(): title.get_text()})
        relInfo.update({
            'Experience': experiences
        })
    if "VolunteeringVolunteering" in x.get_text(strip=True):
        relInfo.update({
            'Volunteer': x.get_text(strip=True)
        })
    if "SkillsSkills" in x.get_text():
        skills = x.find_all(
            'div', class_="display-flex align-items-center")
        for skill in skills:
            talent = skill.find('span', class_='visually-hidden')
            Skills.append(talent.get_text())
        relInfo.update({
            'Skills': Skills
        })
    if "LanguagesLanguages" in x.get_text():
        languages = x.find_all('div', class_='display-flex align-items-center')
        levels = x.find_all('span', class_='t-14 t-normal t-black--light')
        for f, b in zip(languages, levels):
            level = b.find('span', class_='visually-hidden')
            language = f.find('span', class_='visually-hidden')
            Languages.update({language.get_text(): level.get_text()})
        relInfo.update({
            'Languages': Languages
        })
res = json.dumps(relInfo, ensure_ascii=False)
file = open("test.json", "w")
file.write(res)
