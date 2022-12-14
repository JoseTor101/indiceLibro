class pTerminos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izq = None
        self.der = None
        self.subT = sTerminos("")
        self.pags = numPaginas("")

    def insertarSterminos(self,nodo, palabra,lista):
            
        if self:
            if self.nombre == nodo:
               self.subT.insertarElemento(palabra,lista)
            elif nodo < self.nombre:
                self.izq.insertarSterminos(nodo,palabra,lista)
            elif nodo > self.nombre:
                self.der.insertarSterminos(nodo,palabra,lista)    
            
            
    def insertarElemento(self, nombre,valores):
        if self:
            if self.nombre == "":
               self.nombre = nombre
               insertarPaginas(self, valores) 
             #  self.insertarSterminos(self)
            elif nombre < self.nombre:
                if self.izq is None:
                    self.izq = pTerminos(nombre)
                    insertarPaginas(self.izq, valores)
                    #self.insertarSterminos(self.izq)
                else:
                    self.izq.insertarElemento(nombre,valores)
            elif nombre > self.nombre:
                if self.der is None:
                    self.der = pTerminos(nombre)
                    insertarPaginas(self.der, valores)
                   # self.insertarSterminos(self.izq)
                else:
                    self.der.insertarElemento(nombre,valores)
        else:
            self.nombre = nombre
            self.insertarPaginas(self.der, valores)
    def printy (self):
            if self.nombre is None:
                print("-1")
            else:
                if self.izq is None:
                    if self.der is None:
                     print(self.nombre,"  ",end="")
                     self.pags.printy()
                     self.subT.printy()
                     print()
                    else:
                      print(self.nombre," ",end="")
                      self.pags.printy()
                      self.subT.printy()
                      print()
                      self.der.printy()  
                else:
                    if self.der is None:
                        self.izq.printy()    
                        print(self.nombre,"  ",end="")
                        self.pags.printy()
                        self.subT.printy()
                        print()
                    else:   
                        self.izq.printy()    
                        print(self.nombre,"  ",end="") 
                        self.pags.printy()
                        self.subT.printy()
                        print()
                        self.der.printy()    
            
class sTerminos:
    def __init__(self, nombre):
        self.nombre = nombre
        self.izq = None
        self.der = None
        self.pags = numPaginas("")      
    def insertarElemento(self, nombre,valores):
        if self:
            if nombre < self.nombre:
                if self.izq is None:
                    self.izq = sTerminos(nombre)
                    insertarPaginas(self.izq,valores)
                else:
                    self.izq.insertarElemento(nombre,valores)
            elif nombre > self.nombre:
                if self.der is None:
                    self.der = sTerminos(nombre)
                    insertarPaginas(self.der,valores)
                else:
                    self.der.insertarElemento(nombre,valores)
        else:
            self.nombre = nombre
            insertarPaginas(self,valores)
    def printy (self):
            if self.nombre is None:
                print("-1")
            else:
                if self.izq is None:
                    if self.der is None:
                     print("\t",self.nombre,"  ",end="")
                     self.pags.printy()
                     print()
                    else:
                      print("\t",self.nombre,"  ",end="")
                      self.pags.printy()
                      print()
                      self.der.printy()  
                else:
                    if self.der is None:
                        self.izq.printy()    
                        print("\t",self.nombre,"  ",end="")
                        self.pags.printy()
                        print()
                    else:   
                        self.izq.printy()    
                        print("\t",self.nombre,"  ",end="") 
                        self.pags.printy()
                        print()
                        self.der.printy()    

class numPaginas:
    def __init__(self, numPag):
        self.numPag = numPag
        self.izq = None
        self.der = None
    
    def insertarPag(self, numPag):
        if self:
            if self.numPag == "":
               self.numPag = numPag  
            elif numPag < self.numPag:
                if self.izq is None:
                    self.izq = numPaginas(numPag)
                else:
                    self.izq.insertarPag(numPag)
            elif numPag > self.numPag:
                if self.der is None:
                    self.der = numPaginas(numPag)
                else:
                    self.der.insertarPag(numPag)
        else:
            self.numPag = numPag

    def printy (self):
            if self.numPag is None:
                print("-1")
            else:
                if self.izq is None:
                    if self.der is None:
                     print(self.numPag,"  ",end="")
                    else:
                      print(self.numPag,"  ",end="")
                      self.der.printy()  
                else:
                    if self.der is None:
                        self.izq.printy()    
                        print(self.numPag,"  ",end="")
                    else:   
                        self.izq.printy()    
                        print(self.numPag,"  ",end="") 
                        self.der.printy()    

def separarDigitos(lineaPaginas,digitos):
        act = int(digitos+1)
        next1 = act + 2
        digitos= []
        for digitosPag in range(act,len(lineaPaginas),2):
            digitos.append(lineaPaginas[act:next1])
            act += 2
            next1 += 2
        return digitos
def digito(cadena):
    digito = 0
    while cadena:
        if(cadena[digito].isdigit()):
             break
        else: 
             digito += 1
    return digito

def insertarPaginas(nodo, listapagina): #metodo para insertar las paginas una vez creado el nodo
    for i in listapagina:
        nodo.pags.insertarPag(i)
        
def main():
    root = pTerminos("")

    with open('datos.txt') as datos:
        for linea in datos:
            if linea[0] == "m":
                digit = digito(linea)
                lista_pag = separarDigitos(linea,digit)
                lista_pag.sort()

                if lista_pag[0] == "\n" or " \n":
                 lista_pag.pop(0) 
                termino = linea[2:digit] 
                root.insertarElemento(linea[2:digit],lista_pag)
            elif linea[0] == "s":
                digit = digito(linea)
                lista_pag = separarDigitos(linea,digit)
                lista_pag.sort()
                if lista_pag[0] == "\n" or " \n":
                 lista_pag.pop(0) 
                root.insertarSterminos(termino,linea[2:digit],lista_pag)
    print(root.printy())
        
main()