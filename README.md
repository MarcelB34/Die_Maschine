Mein erstes richtiges Anfänger Projekt! Würde mich über feedback freuen

Die Maschiene – Ein digitaler Zwilling in Python
Dieses Projekt ist eine Echtzeit-Simulation einer industriellen Sägestraße. Das Ziel ist es, eine physische Maschine als „digitalen Zwilling“ in Python abzubilden, um logische Abläufe, Sensorsteuerungen und Materialfluss zu simulieren, bevor sie auf echter Hardware laufen würden.

🚀 Das Konzept
Im Gegensatz zu einer rein mathematischen Berechnung nutzt dieses Projekt einen objektorientierten Ansatz (OOP). Jedes Bauteil der Maschine (Förderbänder, Sensoren, Sägeblatt und das Werkstück selbst) existiert als eigenständiges Objekt im Code.

Die Kernlogik
Globales Koordinatensystem: Die gesamte Produktionsstraße ist auf einer Y-Achse von 0 bis 1300 cm kartografiert.

Passive Objekte: Der „Baumstamm“ ist ein reines Datenobjekt, das seine Position kennt, aber von der Maschine bewegt wird.

Aktive Sensorik: Sensoren reagieren autark auf die Position des Werkstücks im Koordinatensystem (Lichtschranken-Prinzip).

Zustandsmaschine (State Machine): Die Steuerung der Maschine wechselt zwischen verschiedenen Zuständen (Transport, Stopp, Sägevorgang), basierend auf den Sensorsignalen.

🛠 Technischer Stack
Sprache: Python 3.x

UI-Framework: PySide6 (Qt for Python)

Design: Qt Designer (Einsatz von dynamischem UI-Loading via .ui-Files)

Architektur: Trennung von UI-Logik und Simulations-Physik.

📈 Aktueller Entwicklungsstand: Phase 1
Momentan ist die physikalische Basisschicht implementiert:

[x] Dynamisches Laden des UI-Interfaces.

[x] Klasse Baumstamm mit automatischer Berechnung von Vorder- und Hinterkante.

[x] Bewegungssimulation über Ticks (Zeitabschnitte).

[ ] Implementierung der Sensor-Logik (in Arbeit).

[ ] Integration der Ablaufsteuerung (State Machine).

📖 Lernziele dieses Projekts
Dieses Repository dient der Vertiefung folgender Konzepte:

Kapselung: Trennung von Daten (Baumstamm) und Logik (Maschine).

Simulationstechnik: Arbeiten mit Zeit-Delta und diskreten Simulationsschritten.

UI-Integration: Kopplung von Backend-Simulationen an ein grafisches Interface in Echtzeit.
