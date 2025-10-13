# Real Estate Web Platform

This is a real estate web project I'm building with Django and a custom design system.
The idea is to create a clean, modern interface for exploring premium properties, managing listings, and helping agents work more efficiently.

---

## 🛠️ Stack

- Backend: Django (Python)
- Frontend: Django templates + bespoke CSS theme (`theme/static/css/base.css`)
- Progressive enhancement with a lightweight navigation helper (`theme/static/js/base.js`).

---

## 📌 Features (in progress)

- User registration & profile pages  
- Property listings and detail pages  
- Agent cards with contact info  
- Custom property collections ("Favorites")  
- Clean UI based on a Figma mockup  

This is still early work — parts of the project are being redesigned and tested. The styles and layout are gradually moving toward the final look.

---

## ⚙️ Setup

If you want to run the project locally:

1. Clone the repo
2. Set up a virtual environment
3. Install Django (pip install django)
4. Run the server:  
   `bash
   python manage.py runserver

5. If you need to rebuild the legacy Tailwind bundle, run `npx tailwindcss -i theme/static_src/styles.css -o theme/static/css/dist/styles.css --watch`.

New pages should extend `theme/templates/base.html`, which already loads the bespoke CSS/JS bundle. You can keep existing Tailwind-driven pages working by leaving the compiled file in place until everything is migrated.

---

## 🌿 Working with branches

Use a dedicated feature branch (for example, `work`) while experimenting:

```bash
git checkout -b work        # создать ветку, если её ещё нет
git status                  # убедиться, что вы в нужной ветке
# ... изменения и коммиты ...
git push -u origin work     # первый пуш создаёт ветку на GitHub
```

После первого `git push -u` ветка появится и в IDE (в списке `origin/work`), и на GitHub в разделе **Branches**. Дальше достаточно обычного `git push`/`git pull`.

> 💡 Столкнулись с ошибкой `src refspec work does not match any`? Это значит, что текущая ветка не создана или в ней нет коммитов. Убедитесь, что вы переключились на `work` (`git checkout -b work`) и сделали хотя бы один коммит перед пушем.

### Автоматизировать пуш ветки

Если хочется сократить количество команд, можно воспользоваться вспомогательным скриптом:

```bash
./scripts/push_work_branch.sh          # создаст ветку work (если её ещё нет) и отправит её на origin
./scripts/push_work_branch.sh feature  # то же самое, но для ветки feature
```

Скрипт проверит, что настроен `origin`, переключит вас на нужную ветку и подсказует, если перед пушем остались незафиксированные изменения.


---

🔄 Status

Still in development.
Some pages may be missing or incomplete. The frontend is being gradually adapted to the Figma design.


---

💬 Notes

This project is part of my learning journey and portfolio.
I'm planning to deploy it later and connect the backend to a more structured frontend.
