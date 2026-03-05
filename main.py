import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile


class MaschieneApp:
    def __init__(self, ui_file_path):
        # 1. Loader und File-Handling
        loader = QUiLoader()
        file = QFile(ui_file_path)

        if not file.open(QFile.ReadOnly):
            print(f"Konnte {ui_file_path} nicht öffnen")
            sys.exit(-1)

        # 2. Das UI laden und als 'ui' speichern
        self.ui = loader.load(file)
        file.close()

        if not self.ui:
            print(loader.errorString())
            sys.exit(-1)

        # 3. Signale (Buttons) mit Funktionen verbinden
        self.setup_connections()

        # 4. Fenster anzeigen
        self.ui.show()

    def setup_connections(self):
        """Hier verbinden wir alle Knöpfe mit ihrer Logik."""
        self.ui.OnButton.clicked.connect(self.start_maschiene)
        self.ui.OffButton.clicked.connect(self.stop_maschiene)

    def start_maschiene(self):
        print("Maschiene läuft...")
        # Hier kannst du später die Werte aus den SpinBoxen auslesen:
        stammlaenge = self.ui.input_stamm_laenge.value()
        schnittgut_laenge = self.ui.input_schnittgut_laenge.value()
        geschwindigkeit = self.ui.input_foerderband_geschw.value()
        print(f"Geschwindigkeit: {geschwindigkeit} cm/min")
        print(f"Stammlänge: { stammlaenge} cm")
        print(f"Schnittgut länge: {schnittgut_laenge} cm")
        # Ein kleiner visueller Test:
        self.ui.progressBar.setValue(50)

    def stop_maschiene(self):
        print("Maschiene gestoppt.")
        self.ui.progressBar.setValue(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    # Hier gibst du einfach den Namen deiner .ui Datei an
    maschiene = MaschieneApp("ui_die_maschiene.ui")

    sys.exit(app.exec())