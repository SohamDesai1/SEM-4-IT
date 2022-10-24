import sys, pickle
from PyQt5.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QTableWidget, \
    QTableWidgetItem, QMessageBox


class dictionary(dict):
    def init(self):
        self = dict()

    def add(self, key, value):
        self[key] = value

    def delete(self, key):
        self.pop(key)

    def main(self):
        s = dictionary()

        def add():
            name = nameLine.text()
            price = priceLine.text()
            s.add(name, price)

            print(s)

            row = table.rowCount()
            table.setRowCount(row + 1)
            namecell = QTableWidgetItem(name)
            pricecell = QTableWidgetItem(price)
            table.setItem(row, 0, namecell)
            table.setItem(row, 1, pricecell)

        def delete(self):
            selected = table.selectedItems()
            name = selected[0].text()
            selectedIndex = table.selectedIndexes()
            rowNo = selectedIndex[0].row()
            table.removeRow(rowNo)
            s.delete(name)
            print(s)

        def save(self):
            file = open("shopping.pickle", "wb")
            pickle.dump(s, file)
            file.close()
            print("Data saved!")

        def upload(self):
            file = open("shopping.pickle", "rb")
            temp = pickle.load(file)
            for name, price in temp.items():
                print(name, price)
            s.add(name, price)
            row = table.rowCount()
            table.setRowCount(row + 1)
            namecell = QTableWidgetItem(name)
            pricecell = QTableWidgetItem(price)
            table.setItem(row, 0, namecell)
            table.setItem(row, 1, pricecell)
            file.close()

        def bill():
            file = open("shopping.pickle", "rb")
            temp = pickle.load(file)
            sum = 0
            for Name, price in temp.items():
                print(Name, price)
                sum += float(price)
            msg = QMessageBox()
            msg.setWindowTitle("Cash Invoice")
            msg.setText("Your bill amount is " + str(sum))
            x = msg.exec_()
            file.close()

        app = QApplication(sys.argv)
        w = QWidget()
        layout = QGridLayout()
        nameLabel = QLabel()
        nameLabel.setText("Name of Product :")
        nameLine = QLineEdit()
        priceLabel = QLabel()
        priceLabel.setText("Price :")
        priceLine = QLineEdit()
        emptyLabel = QLabel()
        emptyLabel.setText("***Product Names And Prices****")
        addButton = QPushButton()
        addButton.setText("Add Record")
        delButton = QPushButton()

        delButton.setText("Delete Record")
        saveButton = QPushButton()
        saveButton.setText("Save Record")
        uploadButton = QPushButton()
        uploadButton.setText("Upload Record")
        billButton = QPushButton()
        billButton.setText("View bill")
        billButton.clicked.connect()
        table = QTableWidget()
        table.setColumnCount(2)
        table.setHorizontalHeaderLabels(["Name of Product", "Price"])
        table.resizeColumnToContents(0)
        table.resizeColumnToContents(1)
        table.setWordWrap(True)
        addButton.clicked.connect(add)
        delButton.clicked.connect(delete)
        saveButton.clicked.connect(save)
        uploadButton.clicked.connect(upload)
        w.resize(550, 350)
        w.setWindowTitle("Shopping List")
        layout.addWidget(nameLabel, 1, 1)
        layout.addWidget(nameLine, 1, 2)
        layout.addWidget(priceLabel, 2, 1)
        layout.addWidget(priceLine, 2, 2)
        layout.addWidget(addButton, 3, 1)
        layout.addWidget(delButton, 3, 2)
        layout.addWidget(saveButton, 3, 3)
        layout.addWidget(uploadButton, 3, 4)
        layout.addWidget(billButton, 3, 5)
        layout.addWidget(emptyLabel, 4, 2)
        layout.addWidget(table, 5, 2)
        w.setLayout(layout)
        w.show()
        sys.exit(app.exec_())


if __name__ == " main ":
    d = dictionary()
    d.main()
