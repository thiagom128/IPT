
class Morse:
    def __init__(self): # inicializa a Arvore Morse
        self.__arvoreMorse = []
        self.__textoConvertido = ''

    def adiciona_no(self, texto):
        self.__arvoreMorse.append(texto.replace('\n', '').split(";"))

    def monta_grade_morse(self, location_search):
        try:
            conteudo = ''
            search_str = f"{location_search}"
            with open(search_str) as f:
                conteudo = f.readlines()

            if conteudo:
                for linha in conteudo:
                    self.adiciona_no(linha)

            return True
        except Exception as e:
            print("[ERRO get_lines_archive ] => " + str(e))
            return False

    def imprimir_arvore_morse(self):
        print("Arvore Morse:")
        for item in self.__arvoreMorse:
            print(f"""{item[1]} {item[0]}""")

    def encode_decode_texto(self, location_search):
        conteudo = ''
        texto_convertido = ''
        search_str = f"{location_search}"
        with open(search_str) as f:
            conteudo = f.readlines()

        if conteudo:
            for linha in conteudo:
                self.__textoConvertido = ''
                arrayAux = linha.replace('\n', '').split(":")
                if arrayAux[0] == "decode":
                    for texto in arrayAux[1].split(' '):
                        if texto == '/':
                            self.__textoConvertido += ' '
                        else:
                            for item in self.__arvoreMorse:
                                if item[1] == texto.upper():
                                    self.__textoConvertido += item[0]
                                    break

                    print(f"""Original: {arrayAux[1]}""")
                    print(f"""Decode: {self.__textoConvertido}""")

                elif arrayAux[0] == "encode":
                    for texto in arrayAux[1]:
                        if texto == ' ':
                            self.__textoConvertido += ' / '
                        else:
                            for item in self.__arvoreMorse:
                                if item[0] == texto.upper():
                                    self.__textoConvertido += item[1] + ' '
                                    break

                    print(f"""Original: {arrayAux[1]}""")
                    print(f"""Encode Morse: {self.__textoConvertido}""")




# Chamada Main
def main():
    morse = Morse()

    caminho_morse = input("Informe o caminho do Codigo Morse:\n")
    caminho_texto = input("Informe o caminho dos texto a ser convertido:\n")
    morse.monta_grade_morse(caminho_morse) # C:\python\matrizMorse.txt
    morse.imprimir_arvore_morse()

    morse.encode_decode_texto(caminho_texto)  # C:\python\conversao.txt

if __name__ == "__main__":
    main()
