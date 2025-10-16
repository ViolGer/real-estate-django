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

## ⚙️ Local setup

1. Clone the repo and create a virtual environment.
2. Copy `.env.example` to `.env` and fill in the secrets (for local development you can keep `DJANGO_DEBUG=True`).
3. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations and load initial data if needed:

   ```bash
   python manage.py migrate
   ```

5. Install Node dependencies if you plan to work on the legacy Tailwind bundle (optional):

   ```bash
   npm install
   npx tailwindcss -i theme/static_src/styles.css -o theme/static/css/dist/styles.css --watch
   ```

6. Start the development server:

   ```bash
   python manage.py runserver
   ```

New pages should extend `theme/templates/base.html`, which already loads the bespoke CSS/JS bundle. You can keep existing Tailwind-driven pages working by leaving the compiled file in place until everything is migrated.

Run the full automated test-suite any time with `pytest`.

---

## 🚀 Deployment checklist

The repository now contains the configuration required for a container/Heroku-style deployment:

- `.env` file sourced automatically via `python-dotenv`; make sure to set production values for `DJANGO_SECRET_KEY`, `DJANGO_ALLOWED_HOSTS`, `DJANGO_CSRF_TRUSTED_ORIGINS`, and the `DATABASE_URL` of your managed PostgreSQL instance.
- Static assets are served with WhiteNoise; collect them before deploying:

  ```bash
  python manage.py collectstatic --noinput
  ```

- Use the provided `Procfile` to launch the app with Gunicorn: `web: gunicorn global_estate.wsgi:application`.
- `runtime.txt` pins Python 3.11.12 for platforms that read it (Heroku, Railway, etc.).
- Security hardening toggles automatically when `DJANGO_DEBUG` is false (HSTS, secure cookies, SSL redirect).
- Set `DJANGO_USE_MANIFEST_STATIC=True` in production to switch on hashed static assets before running `collectstatic` (local development and tests fall back to the simple storage backend).

After configuring the environment variables, a typical release command looks like:

```bash
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn global_estate.wsgi:application
```

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
