from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Scannable(ABC):
    @abstractmethod
    def scan(self):
        pass

class Photocopier(Printable, Scannable):
    def print(self):
        print("Printing...")

    def scan(self):
        print("Scanning...")

class Printer(Printable):
    def print(self):
        print("Printing...")
        class Scanner(Scannable):
    def scan(self):
        print("Scanning...")

def print_document(printable: Printable):
    printable.print()

def scan_document(scannable: Scannable):
    scannable.scan()

photocopier = Photocopier()
printer = Printer()
scanner = Scanner()

print_document(photocopier)  
scan_document(photocopier)  
print_document(printer)  
scan_document(scanner)  
