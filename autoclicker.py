#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Windows Autoclicker - Kommandozeile
Drückt zwei Tasten dauerhaft im Wechsel
"""

import keyboard
import time
import sys

# Konfiguration
KEY1 = 'w'          # Erste Taste
KEY2 = 'space'      # Zweite Taste
DELAY = 0.05        # Verzögerung in Sekunden (50ms)

def main():
    print("=" * 50)
    print("Simple Windows Autoclicker")
    print("=" * 50)
    print(f"Taste 1: {KEY1}")
    print(f"Taste 2: {KEY2}")
    print(f"Verzögerung: {DELAY * 1000}ms")
    print("-" * 50)
    print("Drücke ESC um zu stoppen")
    print("=" * 50)
    print()
    print("▶️  Autoclicker läuft...")
    print()

    try:
        while True:
            # Prüfe ob ESC gedrückt wurde
            if keyboard.is_pressed('esc'):
                print("\n⏹️  ESC gedrückt - Stoppe...")
                break

            # Drücke Taste 1
            keyboard.press(KEY1)
            time.sleep(DELAY)
            keyboard.release(KEY1)
            time.sleep(DELAY)

            # Drücke Taste 2
            keyboard.press(KEY2)
            time.sleep(DELAY)
            keyboard.release(KEY2)
            time.sleep(DELAY)

    except KeyboardInterrupt:
        print("\n\n⏹️  Strg+C gedrückt - Stoppe...")
    except Exception as e:
        print(f"\n❌ Fehler: {e}")
    finally:
        print("✅ Autoclicker beendet")

if __name__ == "__main__":
    main()
