#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simple Windows Autoclicker - Kommandozeile
Hält zwei Tasten dauerhaft gedrückt
"""

import keyboard
import time
import sys

# Konfiguration
KEY1 = 'w'          # Erste Taste
KEY2 = 's'          # Zweite Taste

def main():
    print("=" * 50)
    print("Simple Windows Autoclicker")
    print("=" * 50)
    print(f"Taste 1: {KEY1} (dauerhaft gedrückt)")
    print(f"Taste 2: {KEY2} (dauerhaft gedrückt)")
    print("-" * 50)
    print("Drücke ESC um zu stoppen")
    print("=" * 50)
    print()
    print("▶️  Tasten werden gedrückt...")
    print()

    try:
        # Beide Tasten drücken
        keyboard.press(KEY1)
        keyboard.press(KEY2)

        # Warte bis ESC gedrückt wird
        keyboard.wait('esc')
        print("\n⏹️  ESC gedrückt - Stoppe...")

    except KeyboardInterrupt:
        print("\n\n⏹️  Strg+C gedrückt - Stoppe...")
    except Exception as e:
        print(f"\n❌ Fehler: {e}")
    finally:
        # Tasten loslassen
        try:
            keyboard.release(KEY1)
            keyboard.release(KEY2)
        except:
            pass
        print("✅ Tasten losgelassen - Autoclicker beendet")

if __name__ == "__main__":
    main()
