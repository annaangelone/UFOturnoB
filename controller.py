import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model
        self._listYear = []
        self._listShape = []

    def handle_graph(self, e):
        anno = self._view.txt_anno.value
        giorni = self._view.txt_giorni.value

        if anno is None:
            self._view.create_alert("Nessun anno selezionato, per favore selezionare un anno")
            return

        if giorni is None:
            self._view.create_alert("Nessun giorno selezionato, per favore selezionare un giorno")
            return

        try:
            annoInt = int(anno)

        except ValueError:
            self._view.create_alert("Inserire un valore intero di anno")
            return

        try:
            giorniInt = int(giorni)

        except ValueError:
            self._view.create_alert("Inserire un valore intero di giorni")
            return

        if annoInt < 1906 or annoInt > 2014:
            self._view.create_alert("Inserire un anno compreso tra il 1906 e il 2014 (inclusi)")
            return

        if giorniInt < 1 or giorniInt > 180:
            self._view.create_alert("Inserire un giorno compreso tra 1 e 180 (inclusi)")
            return


        self._model.buildGraph(annoInt, giorniInt)

        self._view.txt_result.controls.append(ft.Text(f"Grafo creato con {self._model.getNumNodes()} nodi e "
                                                      f"{self._model.getNumEdges()} archi"))

        vicini = self._model.stampaPesiVicini()

        for v in vicini:
            self._view.txt_result.controls.append(ft.Text(f"Stato={v[0]}; peso archi adiacenti={v[1]}"))

        self._view.update_page()

