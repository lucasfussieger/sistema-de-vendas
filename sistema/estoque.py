def retirada(self,produto, quantprod):
    while True:
        if produto in estoqueprod:
            estoqueprod -= quantprod
