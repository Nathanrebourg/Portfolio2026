# portfolio-site

Site statique personnel (Portfolio) — copie locale du site HTML et des images.

Contenu:
- `Site.html` — page principale
- `assets/` — images (photos, captures)

Comment utiliser:
1. Ouvrir localement: double-cliquez sur `Site.html` pour l'ouvrir dans votre navigateur.
2. Pour versionner et pousser sur GitHub:
   - Créez un repo distant sur GitHub nommé `portfolio-site`.
   - Puis dans PowerShell depuis le dossier du projet:
     ```powershell
     cd "C:\Users\natha\Desktop\portfolio-site"
     git remote add origin https://github.com/<votre-nom-utilisateur>/portfolio-site.git
     git branch -M main
     git push -u origin main
     ```
   - Si vous avez la CLI GitHub (`gh`) installée, vous pouvez aussi faire:
     ```powershell
     gh repo create <votre-nom-utilisateur>/portfolio-site --public --source=. --remote=origin --push
     ```

Remarques:
- Le projet est volontairement minimal (HTML/CSS). Pour le servir localement via un petit serveur (utile pour fetch/paths), vous pouvez utiliser `python -m http.server 8000` puis ouvrir http://localhost:8000.
- N'oubliez pas de vérifier les chemins d'images relatifs si vous déplacez les fichiers.
