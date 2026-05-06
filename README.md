# Street Lighting Policies Vault

Інтерактивна mind map по політиках вуличного освітлення семи європейських міст.

## Запуск сайту локально

Сайт — це SPA, що читає `.md` файли через `fetch()`. Браузери блокують `fetch` для `file://`, тому треба запустити локальний HTTP-сервер.

### Найшвидший спосіб (Python)

```bash
cd StreetLighting_Vault
python3 -m http.server 8000
```

Потім відкрийте http://localhost:8000 у браузері.

### Альтернативи

```bash
# Node.js
npx serve

# PHP
php -S localhost:8000

# Будь-який інший статичний хостинг (GitHub Pages, Netlify, Vercel, S3)
# просто завантажте папку StreetLighting_Vault як статичний сайт
```

## Структура файлів

```
StreetLighting_Vault/
├── index.html           ← сайт-візуалізатор
├── _manifest.json       ← список усіх .md файлів (для динамічного завантаження)
├── Mind_Map.canvas      ← Obsidian Canvas (візуальна мапа)
├── Sources.md           ← повна бібліографія
├── 00_Index.md          ← головний MOC
├── 01_Методологія_дослідження.md
├── 02_Cross-city_синтез.md
├── 10_Наукове_підґрунтя.md
├── 11_Законодавчі_рамки.md
├── 12_Технічні_стандарти.md
├── 13_Інструменти_та_методології.md
├── cities/              ← по 4 файли на місто (7 × 4 = 28)
│   ├── Lyon_Огляд.md
│   ├── Lyon_Процес_створення.md
│   ├── Lyon_Логіка_рішень.md
│   ├── Lyon_Технічні_рішення.md
│   └── ... (Zürich, Vienna, Geneva, Amsterdam, Copenhagen, Madrid)
└── concepts/            ← наскрізні концепти (12)
    ├── Trame_noire.md
    ├── ALAN_та_біорізноманіття.md
    └── ...
```

## Як редагувати

1. Відредагуйте будь-який `.md` файл у звичайному редакторі (Obsidian, VS Code тощо).
2. **Якщо ви додали або видалили файл**, перегенеруйте маніфест:
   ```bash
   python3 regenerate_manifest.py
   ```
3. Оновіть сторінку в браузері — зміни підхопляться автоматично (Ctrl+Shift+R щоб обійти кеш).

## Як це використати в Obsidian

Відкрийте папку `StreetLighting_Vault` як Obsidian vault:
1. Obsidian → File → Open vault → Open folder as vault → виберіть папку `StreetLighting_Vault`
2. Усі wiki-посилання `[[...]]` працюють з коробки
3. Запустіть Graph view (`Ctrl/Cmd+G`) для мережі зв'язків
4. Відкрийте `Mind_Map.canvas` для візуальної мапи

## Деплой на хостинг

Усе, що потрібно — це папка з:
- `index.html`
- `_manifest.json`
- `Mind_Map.canvas`
- усі `.md` файли

Завантажте на будь-який статичний хостинг (Netlify drag-and-drop, GitHub Pages, Vercel, Cloudflare Pages). Більше нічого не потрібно — сайт повністю клієнтський.
