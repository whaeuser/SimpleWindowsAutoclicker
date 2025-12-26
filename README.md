# Simple Windows Autoclicker

Ein minimalistisches Python-Tool für Windows, das zwei Tasten dauerhaft im Wechsel drückt.

## Features

- ⌨️ Drückt zwei konfigurierbare Tasten im Wechsel
- ⚡ Einstellbare Verzögerung
- 🛑 Stoppen mit ESC oder Strg+C
- 🐍 Einfaches Python-Script ohne GUI

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
KEY2 = 'space'      # Zweite Taste
DELAY = 0.05        # Verzögerung in Sekunden (50ms)
```

### Verfügbare Tasten
- Buchstaben: `'a'`, `'b'`, `'w'`, etc.
- Zahlen: `'0'`, `'1'`, `'2'`, etc.
- Spezialstasten: `'space'`, `'enter'`, `'shift'`, `'ctrl'`, `'alt'`
- Funktionstasten: `'f1'`, `'f2'`, etc.

Siehe [keyboard Dokumentation](https://github.com/boppreh/keyboard#api) für alle Tasten.

## Beispiele

### Gaming: W + Space
```python
KEY1 = 'w'
KEY2 = 'space'
DELAY = 0.05
```

### Farming: Left Click + E
```python
KEY1 = 'left'      # Linke Maustaste
KEY2 = 'e'
DELAY = 0.1
```

### Auto-Jump: Space dauerhaft
```python
KEY1 = 'space'
KEY2 = 'space'
DELAY = 0.5
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
