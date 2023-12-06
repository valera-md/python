# humanity.py
# python > classes
# STATIC usage
class Humanity:
 people = 8_000_000_000
 planet = "earth"
# hm1: +4 properties
 countries = 195
 languages = 5500
 first_flight = 'Orville Wright'
 first_driver = 'Bertha Benz'
 def dailyBirth():
  return 400_000
 def dailyLeave():
  return 150_000
print('Humanity before 2050: ', Humanity.planet)
Humanity.planet = [Humanity.planet, 'Moon', 'Mars']
# hm2: add the 4th and 5th planets from keyboard sequentially
Humanity.planet.append(input('Enter the fourth planet that humanity will reach by 2050 year: '))
Humanity.planet.append(input('Enter the fifth planet that humanity will reach by 2050 year: '))
print('Humanity starting 2050: ', Humanity.planet)
# simulate 1 year of birth
print("people in 2022", Humanity.people)
# hm3: correct the algo that counts people growth over the year considering the daily leaving rate
# hm4: calculate only the increment
previous = Humanity.people
for day in range(365):
 Humanity.people += (Humanity.dailyBirth() - Humanity.dailyLeave())
print("people in 2023", Humanity.people)
current = Humanity.people
increment = current - previous
print("From 2022 to 2023", increment, "people were added on the earth.")