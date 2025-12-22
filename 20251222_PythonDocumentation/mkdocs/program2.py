class Calculator:
    """
    Klasa kalkulator sadrzi metode osnovnih aritmetickih operacija
    """
    def __init__(self, a, b):
        """
       Args:
       a: Prvi broj
       b: Drugi broj

       Returns:
        Kreiran kalkulator
        """
        self.a = a
        self.b = b
    
    def saberi(self):
        """
        Metod za sabiranje
        
        :return: Zbir
        :rtype: int
        """
        return self.a + self.b
    

    def oduzmi (self):
        """
        Metod za oduzimanje
        
        :return: Zbir
        :rtype: int
        """
        return self.a - self.b
    
    def pomnozi (self):
        """
        Metod za mnozenje
        
        :return: Zbir
        :rtype: int
        """
        return self.a * self.b
    
    def podeli (self):
        return self.a / self.b
