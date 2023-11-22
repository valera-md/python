# calculate.balance.3.months.py
# HW1: Calculate balance for 3 months
money = {
 'Jan': {
  'salary': 1500,
  'expense': 500,
  # 'balance'
  },
 'Feb': {
  'salary': 1200,
  'expense': 1700,
  },
 'Mar': {
  'salary': 1700,
  'expense': 700,
  }
}
# print(money['Feb']['expense'])
savings = 0
for month in money:
 money[month]['balance'] =  money[month]['salary'] -  money[month]['expense']
 savings += money[month]['balance']
 print(month, money[month]['salary'], money[month]['expense'], "===>", money[month]['balance'])
print("saved", savings)