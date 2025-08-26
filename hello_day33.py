from datetime import date

DAY = 33
today = date.today().isoformat()

msg = f"Day {DAY} — keep the streak alive! ({today})"
border = "-" * len(msg)

print(border)
print(msg)
print(border)

mkdir day-33-human-passport && cd day-33-human-passport

# створюємо файли
printf '%s\n' '# placeholder' > .gitignore
# встав у файли контент з цього повідомлення
# README.md
# day-33-progress.md
# hello_day33.py

git init
git add .
git commit -m "Day 33: init repo + notes + mini-task"
git branch -M main
git remote add origin <ТВОЯ_URL_.git>
git push -u origin main
