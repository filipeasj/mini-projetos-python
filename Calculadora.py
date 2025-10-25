# São necessários venv e kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput


class MainApp(App):
    def build(self):
        self.operacoes = ["/", "*", "+", "-"]
        self.ultima_operacao = None
        self.ultimo_botao = None

        layout_principal = BoxLayout(orientation="vertical")

        # Campo de texto da solução
        self.solucao = TextInput(
            multiline=False,
            readonly=True,
            halign="right",
            font_size=55
        )
        layout_principal.add_widget(self.solucao)

        # Botões da calculadora
        botoes = [
            ["7", "8", "9", "C"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "/", "+"],
        ]

        for row in botoes:
            h_layout = BoxLayout()
            for label in row:
                botao = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                )
                botao.bind(on_press=self.on_botao_press)
                h_layout.add_widget(botao)
            layout_principal.add_widget(h_layout)

        # Botão de igual
        botao_igual = Button(
            text="=",
            pos_hint={"center_x": 0.5, "center_y": 0.5}
        )
        botao_igual.bind(on_press=self.on_solucao)
        layout_principal.add_widget(botao_igual)

        return layout_principal

    def on_botao_press(self, instance):
        atual = self.solucao.text
        texto_botao = instance.text

        if texto_botao == "C":
            # Limpa a tela
            self.solucao.text = ""
        else:
            # Impede operadores duplicados ou iniciais
            if atual and (self.ultima_operacao and texto_botao in self.operacoes):
                return
            elif atual == "" and texto_botao in self.operacoes:
                return
            else:
                new_text = atual + texto_botao
                self.solucao.text = new_text

        # Atualiza os controles de estado
        self.ultimo_botao = texto_botao
        self.ultima_operacao = self.ultimo_botao in self.operacoes

    def on_solucao(self, instance):
        texto = self.solucao.text
        if texto:
            try:
                # Avalia a expressão e mostra o resultado
                solucao = str(eval(texto))
                self.solucao.text = solucao
            except Exception:
                self.solucao.text = "Erro"


if __name__ == "__main__":
    app = MainApp()
    app.run()
