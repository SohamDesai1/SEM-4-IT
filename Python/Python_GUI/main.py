import sys
from PyQt5.QtWidgets import *
dic = {}

def main():
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(500,500)
    
    layout = QGridLayout()
    productLabel = QLabel("Item name:")
    costLabel = QLabel("Cost:")
    prodLine =  QLineEdit()
    costLine = QLineEdit()
    layout.addWidget(productLabel,1,1)
    layout.addWidget(prodLine,1,2)
    layout.addWidget(costLabel,2,1)
    layout.addWidget(costLine,2,2)
    
    def add():
        p =prodLine.text()
        c = costLine.text()
        dic[p] = float(c)
        print("item Added")
    
    def delete():
        if dic == {}:
            print("No record to delete")
        else:   
         dic.popitem()
         print("record deleted")  
        
    button = QPushButton("Add record")
    button.clicked.connect(add)        
    layout.addWidget(button,3,1)
    button1 = QPushButton("Show record")
    button1.clicked.connect(lambda:print(dic))        
    layout.addWidget(button1,3,2)
    button2 = QPushButton("delete Record")
    button2.clicked.connect(delete)      
    layout.addWidget(button2,3,3)  
    w.setLayout(layout)
    w.setWindowTitle("E Commerce")
    w.show()
    sys.exit(app.exec_()) 
if __name__ == "__main__":
    main()
