# Build-Anleitung: EXE-Datei erstellen

Diese Anleitung zeigt Ihnen, wie Sie aus dem Python-Skript eine ausführbare Windows .exe-Datei erstellen, die ohne Python-Installation funktioniert.

## Voraussetzungen

Sie benötigen einen **Windows-Computer** mit:
- Windows 7 oder höher
- Internetverbindung (für den Download der Abhängigkeiten)

## Option 1: Automatischer Build (Empfohlen)

### Schritt 1: Python installieren (falls nicht vorhanden)

1. Besuchen Sie https://www.python.org/downloads/
2. Laden Sie die neueste Python-Version herunter (z.B. Python 3.11 oder höher)
3. **WICHTIG:** Aktivieren Sie während der Installation die Option "Add Python to PATH"
4. Installieren Sie Python mit den Standardeinstellungen

### Schritt 2: Repository herunterladen

Laden Sie dieses Repository herunter:
- Klicken Sie auf GitHub auf "Code" → "Download ZIP"
- Entpacken Sie die ZIP-Datei in einen Ordner Ihrer Wahl

### Schritt 3: Build-Skript ausführen

1. Öffnen Sie den Ordner mit den entpackten Dateien
2. Doppelklicken Sie auf `build.bat`
3. Das Skript wird automatisch:
   - Python und pip überprüfen
   - Alle benötigten Abhängigkeiten installieren
   - PyInstaller installieren
   - Die .exe-Datei erstellen

### Schritt 4: EXE-Datei finden

Nach erfolgreichem Build finden Sie die fertige .exe-Datei unter:
```
dist/SimpleWindowsAutoclicker.exe
```

Diese Datei können Sie auf jeden Windows-Computer kopieren und ausführen - **ohne Python-Installation**!

## Option 2: Manueller Build

Falls das automatische Skript nicht funktioniert, können Sie die .exe manuell erstellen:

### Schritt 1: Kommandozeile öffnen

1. Drücken Sie `Win + R`
2. Geben Sie `cmd` ein und drücken Sie Enter
3. Navigieren Sie zum Projektordner:
   ```cmd
   cd C:\Pfad\zu\SimpleWindowsAutoclicker
   ```

### Schritt 2: Abhängigkeiten installieren

```cmd
pip install -r requirements.txt
```

### Schritt 3: PyInstaller installieren

```cmd
pip install pyinstaller
```

### Schritt 4: EXE erstellen

```cmd
pyinstaller --onefile --console --name "SimpleWindowsAutoclicker" autoclicker.py
```

### Schritt 5: Fertig!

Die .exe-Datei befindet sich jetzt in `dist/SimpleWindowsAutoclicker.exe`

## Verteilung

Die erstellte .exe-Datei (`SimpleWindowsAutoclicker.exe`) kann auf jedem Windows-Computer ausgeführt werden, ohne dass Python installiert sein muss. Sie können die Datei einfach kopieren und weitergeben.

## Hinweise

- Die .exe-Datei ist ca. 10-15 MB groß (sie enthält alle notwendigen Python-Bibliotheken)
- Beim ersten Start kann Windows SmartScreen eine Warnung anzeigen (da die Datei nicht signiert ist)
  - Klicken Sie auf "Weitere Informationen" und dann auf "Trotzdem ausführen"
- Die Anwendung benötigt Administrator-Rechte, um Tasteneingaben zu simulieren

## Build-Dateien aufräumen

Nach dem Build werden folgende Ordner erstellt:
- `build/` - Temporäre Build-Dateien (kann gelöscht werden)
- `dist/` - Enthält die fertige .exe-Datei (NICHT löschen!)
- `*.spec` - PyInstaller-Konfigurationsdatei (kann behalten werden für wiederholte Builds)

Sie können den `build/` Ordner und die `.spec` Datei löschen, wenn Sie möchten. Die wichtige Datei ist `dist/SimpleWindowsAutoclicker.exe`.

## Fehlerbehebung

### "Python ist nicht installiert"
- Installieren Sie Python von https://www.python.org/
- Stellen Sie sicher, dass "Add Python to PATH" während der Installation aktiviert war

### "pip ist nicht installiert"
- pip wird normalerweise mit Python installiert
- Versuchen Sie `python -m ensurepip` in der Kommandozeile

### "Build fehlgeschlagen"
- Stellen Sie sicher, dass alle Befehle als Administrator ausgeführt werden
- Prüfen Sie, ob Antivirus-Software den Build blockiert
- Versuchen Sie, PyInstaller auf die neueste Version zu aktualisieren: `pip install --upgrade pyinstaller`

### Windows SmartScreen Warnung
- Dies ist normal für nicht signierte .exe-Dateien
- Klicken Sie auf "Weitere Informationen" → "Trotzdem ausführen"
- Optional: Sie können die .exe mit einem Code-Signatur-Zertifikat signieren (kostet Geld)
