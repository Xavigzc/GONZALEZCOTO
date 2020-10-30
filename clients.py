import var
class Clientes():
    def ValidarDNI(dni):
        '''
        codigo que controla si el DNI es correcto
        :return:
        '''
        try:
            tabla = 'TRWAGMYFPDXBNJZSQVHCKE'
            dig_ext = 'XYZ'
            reem_dig_xt = {'X': '0', 'Y': '1', 'Z': '2'}
            numeros = '0123456789'
            dni = dni.upper()
            print(dni)
            if len(dni) == 9:
                dig_control = dni[8]
                dni = dni[:8]
                if dni[0] in dig_ext:
                    dni = dni.replace(dni[0],reem_dig_xt[dni[0]])
                return len(dni) == len([n for n in dni if n in numeros])  and tabla[int(dni) % 23] == dig_control
            return False



        except:
            print('Error módulo validar DNI')
            return None
    def validoDni():
        '''
        Muestra mensaje de validación del DNI
        :return:
        '''
        try:
           dni = var.ui.EditDNI.text()
           if Clientes.ValidarDni(dni):
               var.ui.lblValidar.setStyleSheet('QLabel {color: green;}')
               var.ui.lblValidar.setText('V')
               var.ui.EditDNI.setText(dni.upper())
           else:
               var.ui.lblValidar.setStyleSheet('QLabel {color: red;}')
               var.ui.lblValidar.setText('X')
               var.ui.EditDNI.setText(dni.upper())

        except:
            print('Error módulo escribir DNI')
            return None

    def selSexo():
        try:
            if var.ui.rbtFem.isChecked():
                print('Has elegido Femenino')
            if  var.ui.rbtMas.isChecked():
                print('Has elegido Masculino')

        except Exception as error:
            print('Error %s' % str(error))

        def selPago():
            try:
                if var.ui.chkEfect.isChecked():
                    print('Pagas con efectivo')
                if var.ui.chkTar.isChecked():
                    print('Pagas con Tarjeta')
                if var.ui.chkTran.isChecked():
                    print('Pagas con Transferencia')


            except Exception as error:
                print('Error %s' % str(error))

        def selProv(prov):
            try:
               print('Has seleccionado la provincia de ' + prov)
               return prov
            except Exception as error:
                print('Error %s' % str(error))