#objekt Baumstamm
class Baumstamm:
    def __init__(self, stammlaenge):
        self.stammlaenge = stammlaenge
        self.pos_y_vorderkante = stammlaenge

    def pos_stamm_anfang(self):
        pos_y_vorderkante = self.pos_y_vorderkante
        return pos_y_vorderkante

    @property
    def pos_stamm_ende(self):
        pos_y_hinterkante = self.pos_y_vorderkante - self.stammlaenge
        return pos_y_hinterkante

    def stamm_bewegung(self, bewegung_y):
        self.pos_y_vorderkante = self.pos_y_vorderkante + bewegung_y
        return self.pos_y_vorderkante


stammlaenge = int(input("Wie lang ist der Baumstamm?"))
baumstamm = Baumstamm(stammlaenge)
bewegung =  int(input("Wie viel cm hat er sich pro tick bewegt?"))
tick_anzahl = int(input("Wie viele ticks hat er gemacht?"))
print("\n")
print(f"Start_pos.vorderkante: {baumstamm.pos_y_vorderkante}")
print(f"Start_pos.hinterkante: {baumstamm.pos_stamm_ende}")
print(f"Stammlaenge: {baumstamm.stammlaenge}")

print(f"*" * 30)
for i in range(tick_anzahl):
    print(f"Tick: {i+1}")
    print(f"pos.vorderkante: {baumstamm.stamm_bewegung(bewegung)}")
    print(f"pos.hinterkante: {baumstamm.pos_stamm_ende}")
    print(f"*" * 30)

print(f"Insgesamt hat der Baumstamm: {tick_anzahl * bewegung} cm Bewegt! ")