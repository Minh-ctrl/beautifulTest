from bs4 import BeautifulSoup
html = open('Max.html', 'r')
soup = BeautifulSoup(html, 'html.parser')

Sections = soup.find_all(
    'section', class_='artdeco-card ember-view relative break-words pb3 mt2')
relInfo = []
for x in Sections:
    if "AboutAbout" in x.get_text():
        About = x.get_text()
        relInfo.append(About)
    if "ExperienceExperience" in x.get_text():
        Experience = x.get_text()
        relInfo.append(Experience)
    if "VolunteeringVolunteering" in x.get_text():
        Volunteer = x.get_text()
        relInfo.append(Volunteer)
    if "SkillsSkills" in x.get_text():
        Skills = x.get_text()
        relInfo.append(Skills)
    if "LanguagesLanguages" in x.get_text():
        Languages = x.get_text()
        relInfo.append(Languages)
print(About)
