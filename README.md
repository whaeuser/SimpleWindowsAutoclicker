# Simple Windows Autoclicker

Ein minimalistisches Python-Tool für Windows, das zwei Tasten dauerhaft gedrückt hält.

## Features

- ⌨️ Hält zwei konfigurierbare Tasten dauerhaft gedrückt
- 🛑 Stoppen mit ESC oder Strg+C
- 🐍 Einfaches Python-Script ohne GUI
- ✅ Tasten werden automatisch losgelassen beim Beenden

## Installation

### Voraussetzungen
- Python 3.7 oder höher
- Windows OS

### Schritt 1: Repository klonen
```bash
git clone https://github.com/IHR_USERNAME/SimpleWindowsAutoclicker.git
cd SimpleWindowsAutoclicker
```

### Schritt 2: Dependencies installieren
```bash
pip install -r requirements.txt
```

**WICHTIG für Windows:** Das `keyboard` Modul benötigt Administrator-Rechte!

## Verwendung

### Autoclicker starten
```bash
python autoclicker.py
```

**Als Administrator ausführen** (empfohlen):
- Rechtsklick auf `cmd` oder PowerShell
- "Als Administrator ausführen"
- Dann `python autoclicker.py`

### Stoppen
- Drücke **ESC**
- Oder **Strg+C**

## Konfiguration

Öffne `autoclicker.py` und ändere diese Zeilen:

```python
KEY1 = 'w'          # Erste Taste
KEY2 = 's'          # Zweite Taste
```

### Verfügbare Tasten
- Buchstaben: `'a'`, `'b'`, `'w'`, `'s'`, etc.
- Zahlen: `'0'`, `'1'`, `'2'`, etc.
- Spezialstasten: `'space'`, `'enter'`, `'shift'`, `'ctrl'`, `'alt'`
- Funktionstasten: `'f1'`, `'f2'`, etc.

Siehe [keyboard Dokumentation](https://github.com/boppreh/keyboard#api) für alle Tasten.

## Beispiele

### Standard: W + S (vorwärts + rückwärts)
```python
KEY1 = 'w'
KEY2 = 's'
```

### Gaming: W + Space (vorwärts + springen)
```python
KEY1 = 'w'
KEY2 = 'space'
```

### Strafing: A + D (links + rechts)
```python
KEY1 = 'a'
KEY2 = 'd'
```

### Shift-Laufen: W + Shift
```python
KEY1 = 'w'
KEY2 = 'shift'
```

## Troubleshooting

### "Access Denied" Fehler
→ Als Administrator ausführen

### Tasten werden nicht erkannt
→ Prüfe Tastennamen in der [keyboard Dokumentation](https://github.com/boppreh/keyboard#api)

### Script lässt sich nicht stoppen
→ Drücke ESC mehrmals oder beende das Fenster

## Lizenz

MIT License - Siehe [LICENSE](LICENSE)

## Haftungsausschluss

Dieses Tool ist nur für legale und autorisierte Zwecke gedacht. Die Verwendung von Autoclickern kann gegen die Nutzungsbedingungen von Spielen oder Anwendungen verstoßen. Verwende es auf eigene Verantwortung.

## Credits

- Erstellt mit [keyboard](https://github.com/boppreh/keyboard)
- Python 3
